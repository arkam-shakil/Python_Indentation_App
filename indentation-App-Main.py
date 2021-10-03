'''
  This program automatically adds indentation to meet the requirements
  of python interpreter for identifying code blocks  
  The script was tested with Python 2.7.16
__author__= "Arkam, Rohit, Santosh "
'''

import sys
import indentationlib

def main(argv):
#If the length is less than 2, then that mean, user is using an python IDE to exicute the program.
	if len(argv) < 2:
		try:
			command = input("Please enter the command: ")
			cmd = command.split()
			if cmd[0].lower() == "-h" or cmd[0].lower() == "help":
				indentationlib.display_help()
#				sys.exit()
			else:
				indentationlib.verification(cmd)
				indentationlib.performing_operations(cmd)
		except:
			sys.exit()
#If the length is greater than 2 then that mean, user have exicuted the program on CMD with other parameters
	else:
		del(argv[0])
		if "-h" in argv:
			indentationlib.display_help()
#			sys.exit()
		else:
			indentationlib.verification(argv)
			indentationlib.performing_operations(argv)



if  __name__ == "__main__":
	main(sys.argv)