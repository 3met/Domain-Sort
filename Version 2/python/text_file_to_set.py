
import os

def text_file_to_set(input_location=os.path.join(
		os.path.dirname(os.path.realpath(__file__)),
		'input.txt'),
		sep='\n'):
	
	"""
		Reads a text file into a set

		Allows different seperation methods but defaults to '\n'
	"""

	with open(input_location, 'r') as input_file:
		output = set(input_file.read().strip().split(sep))

	return output
