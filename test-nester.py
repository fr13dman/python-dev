"""This is the "test-nester.py" module and it provides one function called the print_nest() which prints lists that may or may not include nested lists"""

def print_nest(the_list):
	"""This function takes one positional argument called "the list", which is any Python list (of - possibly - nested lines). Each data item in the provided list is (recursively) printed to the screen on it's own line."""
	
	for item in the_list:
		if isinstance(item,list):
			print_nest(item)
		else:
			print(item)

	
