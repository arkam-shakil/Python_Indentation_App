'''
  This program automatically adds indentation to meet the requirements
  of python interpreter for identifying code blocks  
  The script was tested with Python 2.7.16
__author__= "Arkam, Rohit, Santosh "
'''

import sys
import os
import subprocess as sp
import branchlib as bch

#Name: find_function
#Purpose: Open a file and verify whether the given function exist in the file. If yes, then it tells from which line it is starting
#Return: Nothing
def find_function(fname, function):
	found = 0
	notfound = 0
	for i in function:
		funcName = "def " + i + "("
		functionName = funcName.strip()
		try:
			fh = open(fname)
			count = 0
			for line in fh:
				count += 1
				lines = line.strip()
				if lines.startswith(functionName):
					print("Yes, a function named '" + i + "' is available in '" + fname + "' file and it is located at line " + str(count) + ".")
					print('"' + lines + '"')
					found = 1
					try:
						fileOpen = input("Would you like to open '" + fname + "' file? \n Y/N: ")
						if fileOpen.lower() == 'y':
							programName = "notepad.exe"
							fileName = fname
							sp.Popen([programName, fileName])
					except:
						print("")
				else:
					notfound = 1
					continue
			if found == 0 and notfound == 1:
				print("Can not find a function named '" + i + "' in '" + fname + "' file.")
			fh.close()
		except:
			print("Not able to open '" + str(fname) + "' file.")


# name=verification
#this function is for verifying symbols 
def verification(input):
	s = ["-i", "-o", "-aw", "-f", "-d", "-c", "-func", "-b", "-m"]
	lst = []
	flag = False
	for i in input:
		if i.startswith("-"):
			j = i.lower()
			lst.append(j)

	if len(lst) == 0:
		print("No commands given.\nTo know more about the application, use: 'py indentation.py -h'")
		flag = True
	else:
		for i in lst:
			if i in s:
				continue
			else:
				print("Unknown command:", i)
				flag = True

	if flag == True:
		sys.exit()


#name=display_help
#this function will provide a brief user manual
def display_help():
	help = """This tool adds indentation to the block of python code that starts with #{ symbol and ends with #} symbol\n
	Usage:\n
	py indentation.py -I inputfile: indents input file\n
	py indentation.py -I inputfile1,inputfile2,etc. : Can give more than one input file and indents them all\n
	py indentation.py -I inputfile -o outputfile : indented input file is stored in the outputfile. Inputfile is not changed\n
	py indentation.py -i InputFile -Aw word: To create a new outputfile, with a suffix added to the inputfile name.\n
	py indentation.py -I inputfile1,inputfile2, etc. -o outputfile1,outputfile2,etc.: At a time, can give many input files and output files, however number of output files should match the number of input files\n
	py indentation.py -F InputDirectory: Indents the .PY files present inside the given directory\n
	py indentation.py -F InputDirectory -D OutputDirectory: indented input file from the InputDirectory are stored in the OutputDirectory. Inputfiles are not changed\n
	py indentation.py -C StartingSymbol EndingSymbol: Changes the by defauld '#{' and '#}' symbols\n
	py indentation.py -FUNC FunctionName -F FolderName: Checks whether a function defined with the given name exist in any of the files of given directory\n
	py indentation.py -B FolderName: Creates a branch where a user can then edit the code\n
	py indentation.py -M FolderName: Merges a folder with the main folder\n
	py indentation.py -S: Presents a search field to the user.
"""
	print(help)


#name=add_indentation
#this function will  indent the code present in a file and then it will save and return it as a string
#It will take 2 parameters: inputfile and symbols
def add_indentation(inputfile, symbols):
#an empty string veriable to contain the indented code
	indentedcode = ""
	count1 = 0
	count2 = 0
	try:
		fh = open(inputfile, "r")
		for i in fh:
			i = i.strip("\n")
			if i.endswith(symbols[0]):
				count1 += 1
			if i.endswith(symbols[1]):
				count2 += 1

		if count1 >= 1:
			if count1 == count2:
				line = ""
				space = "    "
				level = 0
				line = (space * level) + line
				fh.seek(0)
				for line in fh:
					line = line.strip(" \t\n\r")
					line = (space * level) + line
					if line.endswith(symbols[0]):
						level = level + 1
					elif line.endswith(symbols[1]):
						level = level - 1
					l=line+"\n"
					indentedcode += l
				fh.close()
			else:
				print("Please review the file	", inputfile)
				print("It seems that the file doesn't mentain's a proper structure of", symbols[0], "&", symbols[1], "symbols.")
		else:
			print("Please review the file	", inputfile)
			print("It seems that it doesn't contain ", symbols[0], "&", symbols[1], "symbols.")
	except:
		print("Either the file name is incorrect or file doesn't exist.", inputfile)
	return indentedcode


#name=copy_code
#this function will copy the code from string Variable  to output file
def copy_code(outputfile, indentedcode):
	if len(indentedcode) > 0:
		fh = open(outputfile, "w")
#writing back the indented code in the given output file
		fh.write(indentedcode)
		fh.close()
		print(outputfile, "is indented")


#name=add_prefix
#if a user gives a word for creating new output files, then this function will take that word, add it as a prefix to the input file  and create the output files 
def add_prefix(inputfile, word):
	a = inputfile.split(".")
#Adding a a prefix to the input file names and then appending them to the list
	x = a[0] + word[0] + ".py"
	return x


#name=path
#this function will check whether the given path is in the same working directory or in another one
def path(a):
#going through each list element and comparing that the 2nd item of that element is ':' or not.
#if the 2nd item is ':', then it means that user have provided a path
#else the user have given a folder name. So we are taking the current working directory and then adding the folder name in order to get a proper path
#Then we are appending them in a list
	if a[1] == ":":
		x = a
	else:
		cwd = os.getcwd()
		x = cwd + "\\" + a
	return x


#name=path_verification
#this function will check the path is Correct  or not
def path_verification(a):
	b = path(a)
#going through each path given in the list and checking whether the path exist or not
	try:
		os.chdir(a)
		x = b
	except:
		print("Folder not found in the following directory:", b)
	return x

#name=make_dir
#this will creating the new directory  which user gives
def make_dir(a):
	b = path(a)
#going through each path given in the list and creating a new directory over there
#it will throw an exception if the path is wrong or if a folder with same name already exist.
	try:
		os.mkdir(b)
		x = b
	except:
			print("Either the path is incorrect or a folder with the same name already exist:", b)
	return x


def symbols_verification(symbols):
	if len(symbols) != 2:
		print("You should provide only 2 symbols, first one to indicate the starting symbol and the second one to indicate the ending symbol")
		sys.exit()
	for i in symbols:
		if not i.startswith("#"):
			print(i,"Symbols should starts with '#' sign")
			sys.exit()
		if len(i) < 2:
			print(i,"Your symbol must contain atleast 2 charectors")
			sys.exit()

#name=splitting_elements
#this function will create the list of different element for input file or output file and symbols etc
def splitting_elements(command):
	symbols = ["#{", "#}"]
	ifiles = []
	ofiles = []
	word = []
	ifolder = []
	ofolder = []
	function = []
	branch = []
	merge = []
	space = "    "
	b = ""
#creating a string by adding all the list elements into it.
	for i in command:
		if i.startswith("-"):
			i = "!" + i
		j = i.lower()
		b = b + " " + j
#splitting the string on the basis of '!', to get a proper list for each symbols.
	c = b.split("!")
	if not c[0].startswith("-"):
		del(c[0])
#Running a for loop and comparing all the list elements to put them in their respected pre defined lists.
	for i in c:
		if i.startswith("-i"):
			x= i.split()
			del(x[0])
			for j in x:
				ifiles.append(j)
			if "*.py" in ifiles:
				x = os.listdir()
				for i in x:
					if i.endswith(".py"):
						ifiles.append(i)
				ifiles.remove("*.py")
		if i.startswith("-o"):
			x= i.split()
			del(x[0])
			for j in x:
				ofiles.append(j)
		if i.startswith("-aw"):
			x= i.split()
			del(x[0])
			for j in x:
				word.append(j)
		if i.startswith("-f "):
			x= i.split()
			del(x[0])
			for j in x:
				ifolder.append(j)
		if i.startswith("-d"):
			x= i.split()
			del(x[0])
			for j in x:
				ofolder.append(j)
		if i.startswith("-c"):
			symbols = i.split()
			del(symbols[0])
			symbols_verification(symbols)
		if i.startswith("-t"):
			space = "	"
		if i.startswith("-func"):
			x= i.split()
			del(x[0])
			for j in x:
				function.append(j)
		if i.startswith("-b"):
			x= i.split()
			del(x[0])
			for j in x:
				branch.append(j)
		if i.startswith("-m"):
			x= i.split()
			del(x[0])
			for j in x:
				merge.append(j)

	if len(ifiles) == 0 and len(ifolder) == 0 and len(branch) == 0 and len(merge) == 0:
		print("Inorder to use the application, you need to use '-i' or '-f' command.")
		sys.exit()
	if len(ofiles) > 0 and len(word) > 0:
		print("You can't use '-o' and '-aw' commands together")
		sys.exit()
	if len(ifolder) == 0 and len(function) > 0:
		print("You can not use '-func' command without '-f' command")
		sys.exit()
	if len(branch) > 1:
		print("You can not branch two folders together.")
		sys.exit()
	if len(merge) > 1:
		print("You can not merge more than one branch at a time.")
		sys.exit()
	return ifiles, ofiles, word, ifolder, ofolder, symbols, function, branch, merge


def performing_operations(command):
#calling functions which will return a tuple containing lists for every initiallized symbols
	a = splitting_elements(command)
	ifiles = a[0]
	ofiles = a[1]
	word = a[2]
	ifolder = a[3]
	ofolder = a[4]
	symbols = a[5]
	function = a[6]
	branch = a[7]
	merge = a[8]

#checking the 'ifiles' length to ensure that the user have given file name(s)
	if len(ifiles) > 0:
		for i in range(0, len(ifiles)):
			if ifiles[i].endswith(".py"):
#Taking a file from 'ifiles' list, indenting the code and then returning it into a string
				x = add_indentation(ifiles[i], symbols)
#Copying the code in a seperate file, incase user have given '-o' symbol followed by output file names
				if len(ofiles) > 0:
					if len(ofiles) >= len(ifiles):
						copy_code(ofiles[i], x)
					else:
						print("Insufficient output file names")
						exit()
#creating new files and Copying the code in that file, incase user have given '-aw' symbol followed by the word to be added as a prefix in the new file names
				elif len(word) > 0:
					addword = add_prefix(ifiles[i], word)
					y = copy_code(addword, x)
#Copying the code in the same file
				else:
					y = copy_code(ifiles[i], x)
			else:
				print("The file name must contain '.py' extention", ifiles[i])
	if len(ifolder) > 0 and len(ofolder) == 0 and len(function) == 0:
		for i in range(0, len(ifolder)):
			try:
				folder = path_verification(ifolder[i])
#changing current working directory to the folder given by the user and listing all the files present over there.
				os.chdir(folder)
				flst = os.listdir()
			except:
				continue
			for j in range(0, len(flst)):
				if flst[j].endswith(".py"):
					os.chdir(folder)
					x = add_indentation(flst[j], symbols)
#Copying the code in a seperate file, incase user have given '-o' symbol followed by output file names
					if len(ofiles) > 0:
						if len(ofiles) >= len(flst):
							y = copy_code(ofiles[j], x)
						else:
							print("Insufficient output file names")
							exit()
#creating new files and Copying the code in that file, incase user have given '-aw' symbol followed by the word to be added as a prefix in the new file names
					elif len(word) > 0:
						addword = add_prefix(flst[j], word)
						y = copy_code(addword, x)
#Copying the code in the same file
					else:
						y = copy_code(flst[j], x)
				else:
					print("Your file name must contain '.py' extention", flst[j])
#To ensure that the user wants to work on a folder and they want their indented files in a new folder
	if len(ifolder) > 0 and len(ofolder) > 0 and len(function) == 0:
		for i in range(0, len(ifolder)):
			try:
				folder = path_verification(ifolder[i])
				os.chdir(folder)
				flst = os.listdir()
			except:
				continue
			try:
				newdir = make_dir(ofolder[i])
			except:
				continue

			for j in range(0, len(flst)):
				if flst[j].endswith(".py"):
					os.chdir(folder)
					x = add_indentation(flst[j], symbols)
#Copying the code in a seperate file, incase user have given '-o' symbol followed by output file names
					if len(ofiles) > 0:
						if len(ofiles) >= len(flst):
							os.chdir(newdir)
							y = copy_code(ofiles[j], x)
						else:
							print("Insufficient output file names")
							exit()
#creating new files and Copying the code in that file, incase user have given '-aw' symbol followed by the word to be added as a prefix in the new file names
					elif len(word) > 0:
						addword = add_prefix(flst[j], word)
						os.chdir(newdir)
						y = copy_code(addword, x)
#Copying the code in the same file
					else:
						os.chdir(newdir)
						y = copy_code(flst[j], x)
				else:
					print("Your file name must containg '.py' extention", flst[j])
#Code block for searching perticular function in a file(s)
	if len(ifolder) > 0 and len(ofolder) == 0 and len(function) >= 0:
		for i in range(0, len(ifolder)):
			try:
				folder = path_verification(ifolder[i])
#changing current working directory to the folder given by the user and listing all the files present over there.
				os.chdir(folder)
				flst = os.listdir()
			except:
				continue
			for j in range(0, len(flst)):
				if flst[j].endswith(".py"):
					os.chdir(folder)
					find_function(flst[j], function)
				else:
					print("Your file name must contain '.py' extention", flst[j])
#Code for creating a branch
	if len(branch) == 1:
		bch.create_branch(branch)
#Code for merging a branch
	if len(merge) == 1:
		bch.merge_branch(merge)
