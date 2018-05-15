import sys
from cx_Freeze import setup, Executable

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

print("\n#######################################\nNOTE: main.gsc has to exist\n#######################################\n")
packages = ["idna", "sys"]

path = input("Path to file: ")
if(empty(path) or path.endswith('.py') is False):
	sys.exit("You must enter the proper path (relative or absolute)")

pkg = input("Add packages (seperate with ','): ").split(',')
if(',' in pkg):
	pkg = pkg.split(',')
packages.extend(pkg)

version = input("Version: ")
if(empty(version)):
	version = '1.0'

base = None
executables = [Executable(path, base = base)]
options = {
    'build_exe': {
        'packages':packages,
    },
}

setup(
    name = "py2exe",
    options = options,
    version = version,
    description = '',
    executables = executables
)
print('Success!')
quit = input("Press any key to quit")
exit()