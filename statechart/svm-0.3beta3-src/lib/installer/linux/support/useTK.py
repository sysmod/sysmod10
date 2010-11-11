import os, sys
try:
    basedir = os.environ['_MEIPASS2']
except KeyError:
    basedir = sys.path[0]
tcldir = os.path.join(basedir, '_MEI', 'tcl8.3')
tkdir = os.path.join(basedir, '_MEI', 'tk8.3')
os.environ["TCL_LIBRARY"] = tcldir
os.environ["TK_LIBRARY"] = tkdir
os.putenv("TCL_LIBRARY", tcldir)
os.putenv("TK_LIBRARY", tkdir)
