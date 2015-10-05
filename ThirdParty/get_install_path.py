
def find_module(modulename, filename=None):
    """Finds a python module or package on the standard path.
       If a filename is specified, add its containing folder
       to the system path.

       Returns a string of the full path to the module/package."""
    import importlib.util
    import sys
    import os

    full_path = []
    if filename:
        full_path.append(os.path.dirname(os.path.abspath(filename)))
    full_path += sys.path
    fname = importlib.util.find_spec(modulename, full_path)
    return fname

print( find_module( "PIL" ) )
a = input()