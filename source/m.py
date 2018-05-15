import pyperclip
import os
from os import listdir
from os.path import isfile, join

class _file:
	def __init__(self, path):
		if(os.path.isfile(path) is False or (".gsc" in path or ".gsh" in path) is not True):
			sys.exit("Wrong file format")
		self.path = path
		self.filename = os.path.basename(path)
		self.size = str(os.stat(path).st_size) + ' Kilobytes'
		self.content = getfilecontent(path)

def empty(var):
	if(var is ''):
		var = None
		return True
	try:
		var
	except NameError:
		var = None
		return True
	return False

def getfilecontent(path):
	file = open(path, "r")
	content = file.read()
	file.close
	return content

def output(content, path = '_clientids'):
	if(empty(path)):
		path = '_clientids'
	path += '.gsc'
	file = open(path, "w+")
	file.write(content)
	file.close

# Set name of _subdir
_subdir = input("Path to files: ")

if(empty(_subdir)):
	sys.exit("You must enter the proper path (relative or absolute)")

# add backslash if needed
if((_subdir.endswith('/') or _subdir.endswith('\\')) is False):
	_subdir += '\\'

files = [f for f in listdir(_subdir) if isfile(join(_subdir, f))]

content = getfilecontent(_subdir + 'main.gsc') + '\n'
for x in range(1, len(files)):
	if(files[x] != 'main.gsc' and files[x].endswith('.gsc')):
		file = _file(_subdir + files[x])
		content = content + '\n//' + file.filename + ' [' + file.size + ']\n' + file.content

# copy output to clipboard
copy = input("Copy to clipboard? (y/n)")
if(copy is 'y'):
	pyperclip.copy(content)
	print("\nCopied to clipboard!")
quit = input("Press any key to quit")
exit()