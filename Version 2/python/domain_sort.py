'''
	Domain Sort (Version 2)

	By: Emet Behrendt
'''

from datetime import datetime

from dictionary import Dictionary
from set_to_text_file import set_to_text_file
from text_file_to_set import text_file_to_set

import os

# --- File Globals ---
FILE_DIR = os.path.dirname(os.path.realpath(__file__))
# Input file location globals
DOMAIN_FILE_LOCATION = os.path.join(FILE_DIR, "input-domains.txt")
SKIP_LIST_FILE_LOCATION = os.path.join(FILE_DIR, "input-skiplist.txt")
# Output file location globals
ONE_WORD_DOMAIN_OUTPUT_FILE = os.path.join(FILE_DIR, "output-oneword.txt")
TWO_WORD_DOMAIN_OUTPUT_FILE = os.path.join(FILE_DIR, "output-twoword.txt")
THREE_LETTER_DOMAIN_OUTPUT_FILE = os.path.join(FILE_DIR, "output-threeletter.txt")

# --- Other Globals ---
# List of keywords to avoid
SKIP_LIST = text_file_to_set(SKIP_LIST_FILE_LOCATION)

# Main Function
def main():
	print('Initializing...', end='')

	dictionary = Dictionary()
	domain_set = text_file_to_set(DOMAIN_FILE_LOCATION)
	skip_list = text_file_to_set(DOMAIN_FILE_LOCATION)

	print('\r******************************')
	print('***** Word Domain Filter *****')
	print('******************************')
	print('By Emet Behrendt')

	# Menu loop
	while True:
		# List actions for user
		print("\nAvailable Actions:")
		print("[1] Check for one word domains")
		print("[2] Check for two word domains")
		print("[3] Check for three letter domains")
		print("[4] Exit")
		# Gets user input for action
		action = int(input("\nPlease select an action: "))
		# Executes action as requested by user
		if action == 1:
			one_word_filter(domain_set, dictionary)
		elif action == 2:
			two_word_filter(domain_set, dictionary)
		elif action == 3:
			num_letter_filter(domain_set, 3)
		elif action == 4:
			break
		# Informs user in their action was not valid
		else:
			print(f"Action '{action}' not found. Please try again.")


# Filters one word domains out of domain list
def one_word_filter(domain_set, dictionary, verbose=True):
	start_time = datetime.now()

	if verbose:
		print('\n------------------------------')
		print('Searching for one word domains...')
		print('------------------------------')
		
	output = set()

	for domain in domain_set:
		if check_valid(domain):
			cleaned_domain = clean_domain(domain)
			# Checks if the cleaned domain is a valid word
			if cleaned_domain in dictionary.words:
				output.add(domain)
				print(domain)

	set_to_text_file(output, ONE_WORD_DOMAIN_OUTPUT_FILE)

	end_time = datetime.now()

	if verbose:
		print('------------------------------')
		print('Results:\n')
		print(f'{len(output)} out of {len(domain_set)} valid results', end='')
		print(f'({round((len(output)/len(domain_set))*100, 2)}%)')
		print(f'Total Duration: {end_time-start_time}')
		print('------------------------------')

	return output


# Filters two word domains out of domain list
def two_word_filter(domain_set, dictionary, verbose=True):
	start_time = datetime.now()

	if verbose:
		print('\n------------------------------')
		print('Searching for two word domains...')
		print('------------------------------')

	output = set()

	with open(TWO_WORD_DOMAIN_OUTPUT_FILE, 'w') as results:
		for domain in domain_set:
			if check_valid(domain):
				cleaned_domain = clean_domain(domain)

				# Calculate the min and max possible lengths of the first word
				min_len = len(dictionary.shortest_word)
				max_len = min(len(dictionary.longest_word), 
					len(cleaned_domain)-min_len)

				# Loops through all possible first words and checks
				# if the word is valid
				for sub_len in range(min_len, max_len):
					if cleaned_domain[:sub_len] in dictionary.words:
						# Derives a possible second word from first word
						second_word = cleaned_domain[sub_len:]
						# Checks if the second word is valid
						if second_word in dictionary.words:
							results.write(domain + '\n')
							if verbose:
								print(domain)
							output.add(domain)

	end_time = datetime.now()

	if verbose:
		print('------------------------------')
		print('Results:\n')
		print(f'{len(output)} out of {len(domain_set)} valid results', end='')
		print(f'({round((len(output)/len(domain_set))*100, 2)}%)')
		print(f'Total Duration: {end_time-start_time}')
		print('------------------------------')

	return output


# Filters the domain list based on a given domain length
def num_letter_filter(domain_set, num_letters):
	# Opens output file
	with open(THREE_LETTER_DOMAIN_OUTPUT_FILE, 'w') as results:
		# Runs through all domains in domain list
		for domain in domain_set:
			if check_valid(domain):
				cleaned_domain = clean_domain(domain)
				# Checks if the length of the cleaned domain matches the length requested
				if len(cleaned_domain) == num_letters:
					# Checks if the string only contains letters and not number
					if not any(char.isdigit() for char in cleaned_domain):
						results.write(domain + '\n')
						print(domain)


# Checks if the domain contains and of the keywords in the skip list
# Returns False if domain contains keyword, else returns true
def check_valid(domain):
	for keyword in SKIP_LIST:
		if keyword in domain:
			return False
	return True


# Returns the main domain name ('site.com' ==> 'site')
def clean_domain(domain):
	return domain.split(".", 1)[0]


if __name__ == "__main__":
	main()
