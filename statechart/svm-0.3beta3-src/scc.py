#---------------------------------------------------------------------
#      SCC (StateChart Compiler)
#           -- a compiler for an extended statechart formalism
#---------------------------------------------------------------------
#
# Copyright (C) 2003 Thomas Huining Feng
#
#---------------------------------------------------------------------
# Address:      MSDL, SOCS, McGill Univ., Montreal, Canada
# HomePage:     http://msdl.cs.mcgill.ca/people/tfeng/
# SCC HomePage: http://msdl.cs.mcgill.ca/people/tfeng/?research=scc
# Download:     http://savannah.nongnu.org/files/?group=svm
# CVS:          :pserver:anoncvs@subversions.gnu.org:/cvsroot/svm
#               (projects "svm" and "jsvm")
# Email:        hfeng2@cs.mcgill.ca
#---------------------------------------------------------------------
#
# This file is part of SCC.
#
#---------------------------------------------------------------------
# SCC is free software; you can redistribute it and/or modify it under
# the terms of the GNU General Public License as published by the Free
# Software Foundation; either version 2 of the License, or (at your
# option) any later version.
#
# SCC is distributed in the hope that it will be useful, but WITHOUT
# ANY WARRANTY; without even the implied warranty of MERCHANTABILITY
# or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public
# License for more details.
#
# You should have received a copy of the GNU General Public License
# along with SCC; if not, write to the Free Software Foundation, Inc.,
# 59 Temple Place, Suite 330, Boston, MA 02111-1307 USA
#---------------------------------------------------------------------


import sys
import os
import string
from StringUtil import *
from Debugger import Debugger
from Exception import *
from EventHandler import EventHandler
import time
import distutils.sysconfig

# modify macros in StringUtil
EVENT_MACRO['[EVENT]'][1]="eventhandler.event([ev], [p], [lock])"

def print_usage():
  print '=================================================='
  print '|  Python Implementation of Statechart Compiler  |'
  print '|               Version 0.3 Beta3                |'
  print '|       Presented by Thomas Feng, Nov. 2003      |'
  print '=================================================='
  print ''
  print 'Usage: scc [options...] <.des file> [parameters...]'
  print '       options:'
  print '           -l <lang>: generate code in language <lang>'
  print '                      supported languages: java (default), cpp, csharp, python'
  print '           -i <file>: include a file (to the head)'
  print '           -I <file>: include a file (to the tail)'
  print '           -q:        quiet'
  print '           -c:        print out the command only (do not generate output)'
  print '       language-specific options:'
  print '         cpp:'
  print '           --head:    generate head file'
  print '           --ext:     include extensions for actions (require Python dynamic library)'
  print '           --gnu:     print only GNU C++ related commands (default)'
  print '           --vc:      print only Visual C++ related commands'
  print '         csharp:'
  print '           --mono:    print only Mono related commands (default)'
  print '           --dotnet:  print only .Net related commands'
  print '         python:'
  print '           --ext:     include extensions for actions'
  print '       parameters:'
  print '           "name=value"'

def print_info(info, desc):
  for d in desc:
    if d==[]:
      print "-"*5
    elif info.has_key(d[0]) and info[d[0]]:
      print d[1], info[d[0]]

sys.path=[""]+sys.path

try:
  if len(sys.argv)<2:
    print_usage()
  else:
    argn=1
    is_param=1
    use_gui=0
    haddition=[]
    taddition=[]
    code_type="java"

    # Defaint options
    need_cpp_head=0
    action_ext=0
    quiet=0
    command_only=0
    gnu_only=1
    mono_only=1
    vc_only=0
    dotnet_only=0

    # Check options here.
    while is_param and argn<len(sys.argv):
      arg=sys.argv[argn]
      if startswith(arg, '-l'):
        argn=argn+1
        if arg=='-l':
          if argn<len(sys.argv)-1:
	    code_type=sys.argv[argn]
            argn=argn+1
        else:
          code_type=arg[2:]
      elif arg=='-i' and argn<len(sys.argv)-1:
        argn=argn+1
        haddition.append(sys.argv[argn])
        argn=argn+1
      elif arg=='-I' and argn<len(sys.argv)-1:
        argn=argn+1
        taddition.append(sys.argv[argn])
        argn=argn+1
      elif arg=='--head':
        need_cpp_head=1
        argn=argn+1
      elif arg=='--ext':
        action_ext=1
        argn=argn+1
      elif arg=='-q':
        quiet=1
        argn=argn+1
      elif arg=='-c':
        command_only=1
        argn=argn+1
      elif arg=='--gnu':
        gnu_only=1
        vc_only=0
        argn=argn+1
      elif arg=='--vc':
        gnu_only=0
        vc_only=1
        argn=argn+1
      elif arg=='--mono':
        mono_only=1
        dotnet_only=0
        argn=argn+1
      elif arg=='--dotnet':
        mono_only=0
        dotnet_only=1
        argn=argn+1
      else:
        is_param=0

    if argn>=len(sys.argv):
      print_usage()
      exit

    desc=arg
    argn=argn+1
    path_name=os.path.split(desc)
    addpath=path_name[0]
    name=path_name[1]
    if len(addpath)>0:
      sys.path=[addpath]+sys.path

    params={}
    while argn<len(sys.argv):
      arg=sys.argv[argn]
      argn=argn+1
      param=ParseOption(arg)
      if param!=None:
        par=ParseParameter(param[0])
        params[par[0]]=[par[1], param[1]]

    if command_only:
      if len(name)>4 and string.upper(name[len(name)-4:])==".DES":
        model_name=name[:len(name)-4]
      else:
        model_name=name
    else:
      eventhandler=EventHandler(name, None, params, use_gui, 1, haddition, taddition, 0)
      model_name=eventhandler.options[MODEL_NAME]

    code_type=string.lower(code_type)
    info={"time":None, "compile":None, "run":None, "file":None}
    desc=[[],
          ["time",    "Time spent on compilation:        "],
          ["file",    "File(s) generated:                "],
          [],
          ["compile", "Command to compile the source:    "],
          ["run",     "Command to run the compiled code: "],
          []]

    starttime=time.time()
    if code_type=="java":
      if not command_only:
        from JavaGenerator import JavaGenerator
        g=JavaGenerator(eventhandler)
        g.generate()
      info["file"]="%s.java" % model_name
      info["compile"]="javac %s.java" % model_name
      info["run"]="java %s" % model_name
    elif code_type=="python":
      if not command_only:
        from PythonGenerator import PythonGenerator
        g=PythonGenerator(eventhandler, action_ext)
        g.generate()
      info["file"]="%s.py" % model_name
      info["compile"]="(N/A)"
      info["run"]="python %s.py" % model_name
    elif code_type=="cpp":
      if not command_only:
        from CppGenerator import CppGenerator
        g=CppGenerator(eventhandler, action_ext)
      if need_cpp_head:
        if not command_only:
          jf_h=open(g.eventhandler.options[MODEL_NAME]+".h", "w")
          jf=open(g.eventhandler.options[MODEL_NAME]+"."+g.postfix, "w")
          code=g.generate_code(separate_interface=1, need_include=1)
          jf_h.write(code[0])
          jf.write(code[1])
          jf_h.close()
          jf.close()
        info["file"]="%s.h, %s.cpp" % (model_name, model_name)
      else:
        if not command_only:
          g.generate()
        info["file"]="%s.cpp" % model_name
      if action_ext:
        if os.name=="posix":  # Unix/FreeBSD/SunOS/Linux
          LINKFORSHARED=string.join(distutils.sysconfig.get_config_vars("LINKFORSHARED"), " ")
          LIBPL=string.join(distutils.sysconfig.get_config_vars("LIBPL"), " -L")
          INCLUDEPY=string.join(distutils.sysconfig.get_config_vars("INCLUDEPY"), " ")
          LIBS=string.join(distutils.sysconfig.get_config_vars("LIBS"), " ")
          LIBM=string.join(distutils.sysconfig.get_config_vars("LIBM"), " ")
          VERSION=sys.version[:3]
          if string.find(LIBS, "-lpthread")<0 and string.find(LIBS, "-pthread")<0:
            LIBS=LIBS+" -pthread"
          info["compile"]="g++ -I%s -L%s %s %s.cpp -lpython%s %s %s -o %s (with GNU C++ only)" % (INCLUDEPY, LIBPL, LINKFORSHARED, model_name, VERSION, LIBM, LIBS, model_name)
          info["run"]="./%s (in Linux or Unix only)" % model_name
        else:  # Windows based
          LIBS=os.path.join(distutils.sysconfig.get_config_vars("prefix")[0], "libs")
          INCLUDEPY=string.join(distutils.sysconfig.get_config_vars("INCLUDEPY"), " ")
      if gnu_only:
        if action_ext:
          info["compile"]="g++ -I%s -L%s %s %s.cpp -lpython%s %s %s -o %s" % (INCLUDEPY, LIBPL, LINKFORSHARED, model_name, VERSION, LIBM, LIBS, model_name)
        else:
          info["compile"]="g++ -o %s %s.cpp" % (model_name, model_name)
        info["run"]="./%s" % model_name
      elif vc_only:
        if action_ext:
          info["compile"]="cl /GX /I%s %s.cpp /link /LIBPATH:%s" % (INCLUDEPY, model_name, LIBS)
        else:
          info["compile"]="cl /GX %s.cpp" % model_name
        info["run"]="%s" % model_name
    elif code_type=="csharp":
      if not command_only:
        from CSharpGenerator import CSharpGenerator
        g=CSharpGenerator(eventhandler)
        g.generate()
      info["file"]="%s.cs" % model_name
      if mono_only:
        info["compile"]="mcs -main:%s %s.cs" % (model_name, model_name)
        info["run"]="mono %s.exe" % model_name
      elif dotnet_only:
        info["compile"]="csc /main:%s %s.cs" % (model_name, model_name)
        info["run"]="%s.exe" % model_name
    else:
      print 'Language "%s" is not supported.' % code_type
      sys.exit(1)

    info["time"]="%0.3f (sec)" % (time.time()-starttime)

    if not quiet and not command_only:
      print_info(info, desc)
    elif not quiet and command_only:
      print info["compile"]
    
except FileNotFound, e:
  print e
  raise SystemExit
