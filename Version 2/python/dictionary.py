
import os 

class Dictionary():
	"""
		A class to store the dictionary and related information
	"""


	DICTIONARY_FILE_LOCATION = os.path.join(
		os.path.dirname(os.path.realpath(__file__)),
		"dictionary.txt")

	def __init__(self, generate=True,
		dictionary_file_location=DICTIONARY_FILE_LOCATION):
		"""
			Reads dictionary file if generate is true
		"""

		if generate:
			self._generate(dictionary_file_location=dictionary_file_location)


	def _generate(self, 
		dictionary_file_location=DICTIONARY_FILE_LOCATION):
		"""
			Fetches and returns words from dictionary file
		"""

		with open(dictionary_file_location, 'r') as dictionary:
			words = dictionary.read().strip().split('\n')
			self.words = set(words)

		self.shortest_word = len(min(self.words, key=len))
		self.longest_word = len(max(self.words, key=len))
