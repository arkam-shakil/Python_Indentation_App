'''
  This program automatically adds indentation to meet the requirements
  of python interpreter for identifying code blocks  
  The script was tested with Python 2.7.16
__author__= "Arkam, Rohit, Santosh "
'''

import sys
import indentationlib
import searchlib as search

def main(argv):
#If the length is less than 2, then that mean, user is using an python IDE to exicute the program.
	if len(argv) < 2:
		try:
			command = input("Please enter the command: ")
			cmd = command.split()
			if "-h" in cmd or "-H" in cmd:
				indentationlib.display_help()
			elif "-s" in cmd or "-S" in cmd:
				search.perform_search()
			else:
				indentationlib.verification(cmd)
				indentationlib.performing_operations(cmd)
		except:
			sys.exit()
#If the length is greater than 2 then that mean, user have exicuted the program on CMD with other parameters
	else:
		del(argv[0])
		if "-h" in argv or "-H" in argv:
			indentationlib.display_help()
		elif "-s" in argv or "-S" in argv:
			search.perform_search()
		else:
			indentationlib.verification(argv)
			indentationlib.performing_operations(argv)



if  __name__ == "__main__":
	main(sys.argv)