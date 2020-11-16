
import os

def set_to_text_file(source, output_location=os.path.join(
		os.path.dirname(os.path.realpath(__file__)),
		'output.txt'), sep='\n'):
	
	"""
		Writes a set into a text file

		Allows different seperations types but defaults to using '\n'
	"""

	with open(output_location, 'w') as output:
		for x in source:
			output.write(x + sep)
