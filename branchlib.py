'''
  This program automatically adds indentation to meet the requirements
  of python interpreter for identifying code blocks  
  The script was tested with Python 2.7.16
__author__= "Arkam, Rohit, Santosh "
'''

import os
import shutil
import indentationlib as ind


def create_branch(mainFile):
	for i in mainFile:
		src = ind.path(i)
		try:
			os.chdir(src)
		except:
			print("Can not access the given folder at: ", src)
		try:
			dst = src + "-Branch"
			destination = shutil.copytree(src, dst)
			print("Created a branch at: ", destination)
		except:
			print("Not able to branch the given folder at: ", dst)


def merge_branch(mainFile):
	for i in mainFile:
		src = i.split("-branch")
		if src[0].endswith("-branch"):
			try:
				shutil.rmtree(src[0])
				os.rename(i, src[0])
				print("The branch got merged!")
			except:
				print("Can not merge the folder")
		else:
			print("Please verify the folder.\nIt does not seems to be a branched folder.")