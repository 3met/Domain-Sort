
from set_to_text_file import set_to_text_file
from text_file_to_set import text_file_to_set

import os

class Dictionary():
	"""
		A class to store the dictionary and related information

		Utilities:
		- 
		- Adding words
		- Removing words
		- Saving to text file after updating
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


	def __len__(self):
		return len(self.words)


	def _generate(self, 
		dictionary_file_location=DICTIONARY_FILE_LOCATION):
		"""
			Fetches and returns words from dictionary file
		"""
		self.source = dictionary_file_location
		self.words = text_file_to_set(dictionary_file_location)
		self.shortest_word = min(self.words, key=len)
		self.longest_word = max(self.words, key=len)


	def add(self, word):
		self.words.add(word)


	def remove(self, word):
		self.words.remove(word)


	def save(self):
		"""
			Updates dictionary's original text file
		"""
		return set_to_text_file(self.words, self.source)
