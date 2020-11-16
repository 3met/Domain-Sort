'''
	Domain Sort (Version 2)

	By: Emet Behrendt
'''

# List of keywords to avoid
skipList = ('.me', '.org', "-")
# Input file location globals
DICTIONARY_FILE_LOCATION = "dictionary.txt"
DOMAIN_FILE_LOCATION = "domains.txt"
# Output file location globals
ONE_WORD_DOMAIN_OUTPUT_FILE = "results-oneword.txt"
TWO_WORD_DOMAIN_OUTPUT_FILE = "results-twoword.txt"
THREE_LETTER_DOMAIN_OUTPUT_FILE = "results-threeletter.txt"

# Main Function
def main():
	print("******************************")
	print("***** Word Domain Filter *****")
	print("******************************")
	print("By Emet Behrendt")

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
			print("\nLooking for one word domains...")
			one_word_filter()
		elif action == 2:
			two_word_filter()
		elif action == 3:
			num_letter_filter(3)
		elif action == 4:
			break
		# Informs user in their action was not valid
		else:
			print(f"Action '{action}' not found. Please try again.")


# Filters one word domains out of domain list
def one_word_filter():
	dictionary = get_dictionary()
	domains = get_domains()
	with open(ONE_WORD_DOMAIN_OUTPUT_FILE, 'w') as results:
		for domain in domains:
			if check_valid(domain):
				cleaned_domain = clean_domain(domain)
				# Checks if the cleaned domain is a valid word
				if cleaned_domain in dictionary:
					print(domain)
					results.write(domain + '\n')


# Filters two word domains out of domain list
def two_word_filter():
	dictionary = get_dictionary()
	domains = get_domains()
	with open(TWO_WORD_DOMAIN_OUTPUT_FILE, 'w') as results:
		for domain in domains:
			if check_valid(domain):
				cleaned_domain = clean_domain(domain)
				# Cycles through words in dictionary
				for word in dictionary:
					# Checks if domain starts with first word
					if word == cleaned_domain[:len(word)]:
						second_word = cleaned_domain[len(word):]
						# Checks if the new domain is composed of both first and second words
						if second_word in dictionary:
								results.write(domain + '\n')
								print(domain)


# Filters the domain list based on a given domain length
def num_letter_filter(num_letters):
	# Fetches domain list
	domains = get_domains()
	# Opens output file
	with open(THREE_LETTER_DOMAIN_OUTPUT_FILE, 'w') as results:
		# Runs through all domains in domain list
		for domain in domains:
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
	for keyword in skipList:
		if keyword in domain:
			return False
	return True


# Returns the main domain name ('site.com' ==> 'site')
def clean_domain(domain):
	return domain.split(".", 1)[0]


# Fetches and returns domains from domain list text file
def get_domains():
	with open(DOMAIN_FILE_LOCATION, 'r') as domainFile:
		domains = domainFile.read().strip().split('\n')
	return tuple(domains)


# Fetches and returns words from dictionary file
def get_dictionary():
	with open(DICTIONARY_FILE_LOCATION, 'r') as dictionary:
		words = dictionary.read().strip().split('\n')
	return set(words)


if __name__ == "__main__":
	main()
