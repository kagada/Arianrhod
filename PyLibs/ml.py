import sys

if sys.winver == '2.7':
    from immdbg import *
else:
    from MyPyLibrary.MyLibrary import *

sys.dont_write_bytecode = True
