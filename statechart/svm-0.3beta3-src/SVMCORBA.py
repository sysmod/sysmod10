#---------------------------------------------------------------------
#    SVM (Statechart Virtual Machine)
#         -- an interpreter for an extended statechart formalism
#---------------------------------------------------------------------
#
# Copyright (C) 2003 Thomas Huining Feng
#
#---------------------------------------------------------------------
# Address:      MSDL, SOCS, McGill Univ., Montreal, Canada
# HomePage:     http://msdl.cs.mcgill.ca/people/tfeng/
# SVM HomePage: http://msdl.cs.mcgill.ca/people/tfeng/?research=svm
# Download:     http://savannah.nongnu.org/files/?group=svm
# CVS:          :pserver:anoncvs@subversions.gnu.org:/cvsroot/svm
#               (projects "svm" and "jsvm")
# Email:        hfeng2@cs.mcgill.ca
#---------------------------------------------------------------------
#
# This file is part of SVM.
#
#---------------------------------------------------------------------
# SVM is free software; you can redistribute it and/or modify it under
# the terms of the GNU General Public License as published by the Free
# Software Foundation; either version 2 of the License, or (at your
# option) any later version.
#
# SVM is distributed in the hope that it will be useful, but WITHOUT
# ANY WARRANTY; without even the implied warranty of MERCHANTABILITY
# or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public
# License for more details.
#
# You should have received a copy of the GNU General Public License
# along with SVM; if not, write to the Free Software Foundation, Inc.,
# 59 Temple Place, Suite 330, Boston, MA 02111-1307 USA
#---------------------------------------------------------------------


from StringUtil import *
import random
import os
import re
import code
import sys
import ThreadUtil

RESULT_OK                   = 0
RESULT_FNORB_NOT_INSTALLED  = 7001
RESULT_FNORB_NOT_STARTED    = 7002
RESULT_SERVICE_NOT_FOUND    = 7003

NAME_SERVICE='NameService'
INTERFACE_REPOSITORY='InterfaceRepository'
REQUIRED_SERVICES=[NAME_SERVICE, INTERFACE_REPOSITORY]

REMOVE_ON_EXIT=0

FNORB_PARAMETERS=[]  # ['--ORBthreading-model=Threaded']

class SVMCORBA_RECORD:
  fnorb_installed=0
  fnorb_started=0
  init_succ=0
  orb=None
  work_path=None
  module_name=None
  module_num=None
  nctx=None
  ifctx=None
  ports=None
  impl=None
  eh=None
  stub_path=None
  found_comps={}
  stub_generated=[]

try:
  from Fnorb.orb import CORBA, BOA
  from Fnorb.cos.naming import CosNaming
  SVMCORBA_RECORD.fnorb_installed=1
except:
  pass

def generate_idl():
  idl_content ='\
//---------------------------------------------\n\
// IDL interface description generated by SVM  \n\
// Thomas Huining Feng                         \n\
//---------------------------------------------\n\n'
  idl_content=idl_content+'#pragma prefix "msdl.cs.mcgill.ca"\n\n'
  idl_content=idl_content+'// Module namespace shared by all SVM models\n\n'
  idl_content=idl_content+'module %s\n' % SVM_MODULE
  idl_content=idl_content+'{\n'
  idl_content=idl_content+'    module %s\n' % SVMCORBA_RECORD.module_name
  idl_content=idl_content+'    {\n'
  idl_content=idl_content+'        typedef sequence<any> param_list;\n'
  idl_content=idl_content+'        typedef sequence<string> port_list;\n'
  idl_content=idl_content+'        typedef sequence<string> comp_list;\n'

  idl_content=idl_content+'        interface inf_%d\n' % SVMCORBA_RECORD.module_num
  idl_content=idl_content+'        {\n'
  for pn in SVMCORBA_RECORD.ports.keys():
    if SVMCORBA_RECORD.ports[pn]['in']:
      idl_content=idl_content+'            void %s(in string event, in param_list params);\n' % pn
  idl_content=idl_content+'            void svm_module_add_connection(in port_list pserver, in port_list pclient, in comp_list components);\n'
  idl_content=idl_content+'        };\n'

  idl_content=idl_content+'    };\n'
  idl_content=idl_content+'};\n'

  return idl_content

def generate_stub():
  path=os.path.join(SVMCORBA_RECORD.work_path, 'serverif')
  interface_name=SVMCORBA_RECORD.module_name+'_'+str(SVMCORBA_RECORD.module_num)
  try:
    os.mkdir(path)
  except:
    1
  p=os.path.join(path, interface_name)
  try:
    os.mkdir(p)
  except:
    1  
  idl=generate_idl()
  idl_file=os.path.join(p, interface_name+'.idl')
  idlf=open(idl_file, 'w')
  idlf.write(idl)
  idlf.close()
  os.spawnvp(os.P_WAIT, 'fnidl', ['fnidl', idl_file, '--directory='+p])
  return idl_file

def generate_link_stub(links):
  path=os.path.join(SVMCORBA_RECORD.work_path, 'linkstub')
  try:
    os.mkdir(path)
  except:
    1
  SVMCORBA_RECORD.stub_path=path
  for lk in links.keys():
    path=os.path.join(SVMCORBA_RECORD.stub_path, links[lk][0])
    try:
      os.mkdir(path)
    except:
      1
    p=os.path.join(path, links[lk][1])
    try:
      os.mkdir(p)
    except:
      1
    idl_file=os.path.join(p, '%s_%d_link.idl' % (SVMCORBA_RECORD.module_name, SVMCORBA_RECORD.module_num))
    if not idl_file in SVMCORBA_RECORD.stub_generated:
      SVMCORBA_RECORD.stub_generated.append(idl_file)
      idl=links[lk][2]
      idlf=open(idl_file, 'w')
      idlf.write(idl)
      idlf.close()
      os.spawnvp(os.P_WAIT, 'fnidl', ['fnidl', idl_file, '--directory='+p])

def create_link_table(links):
  ctx=SVMCORBA_RECORD.orb.resolve_initial_references("NameService")
  table={}

  ii=code.InteractiveInterpreter(locals())
  
  for lk in links.keys():
    path=os.path.join(SVMCORBA_RECORD.stub_path, links[lk][0])
    path=os.path.join(path, links[lk][1])
    path=os.path.join(path, SVM_MODULE)
    
    sys.path=[path]+sys.path
    ii.runsource('import %s'%links[lk][0])

    cpath=[CosNaming.NameComponent('SVM', ''), CosNaming.NameComponent(SVM_MODULE, ''),
	   CosNaming.NameComponent(links[lk][0], ''), CosNaming.NameComponent(links[lk][1], '')]
    links[lk].append(ctx.resolve(cpath))

    if table.has_key(lk):
      table[lk].append(eval('links[lk][4].%s'%links[lk][3]))
    else:
      table[lk]=[eval('links[lk][4].%s'%links[lk][3])]

  return table

def locate_components(links):
  ctx=SVMCORBA_RECORD.orb.resolve_initial_references("NameService")

  for lk in links.keys():
    path=os.path.join(SVMCORBA_RECORD.stub_path, links[lk][0])
    path=os.path.join(path, links[lk][1])
    path=os.path.join(path, SVM_MODULE)
  
    sys.path=[path]+sys.path

    cpath=[CosNaming.NameComponent('SVM', ''), CosNaming.NameComponent(SVM_MODULE, ''),
	   CosNaming.NameComponent(links[lk][0], ''), CosNaming.NameComponent(links[lk][1], '')]

    links[lk].append(ctx.resolve(cpath))

def notify_components(links):
  for lk in links.keys():
    try:
      links[lk][4].svm_module_add_connection([links[lk][3]], [lk], [SVMCORBA_RECORD.module_name, "inf_%d"%SVMCORBA_RECORD.module_num])
    except:
      print 'WARNING: An incoming connection cannot be established.'

def limit_names(mflist, name):
  result=[]
  for mf in mflist:
    if '_get_name' in dir(mf) and re.match(name, mf._get_name()):
      result.append(mf)
  return result

def lookup_interfaces(infdict):
  orb=SVMCORBA_RECORD.orb
  ctx=orb.resolve_initial_references('InterfaceRepository')
  cnts=limit_names(ctx.contents(CORBA.dk_Module, 0), SVM_MODULE_RE)
  if not cnts:
    return None
  else:
    mdl=cnts[0]  # at most 1 module found
  result={}
  for cname in infdict.keys():
    mdl2=mdl.contents(CORBA.dk_Module, 0)
    props=infdict[cname]
    for prop in props:
      if not mdl2:
	break
      pname=prop[0]
      pvalue=prop[1]
      if pname=='name':
	mdl2=limit_names(mdl2, pvalue)
      elif pname=='type':
	pass  # not implemented
      elif pname=='keys':
	pass  # not implemented
    if mdl2:
      mdlc=random.choice(mdl2)  # randomly choose a module
      result[cname]=[mdlc, mdlc.contents(CORBA.dk_Interface, 0)]
    else:
      print 'WARNING: Component with restriction %s cannot be found.' % str(props)
  return result

def parse_ports(ports):
  if len(ports)!=2:
    return None
  pos1=find(ports[0], '.')
  pos2=find(ports[1], '.')
  if (pos1>=0 and pos2>=0) or (pos1<0 and pos2<0):
    return None
  if pos1>=0:
    comp=ports[0][:pos1]
    pcomp=ports[0][pos1+1:]
    pself=ports[1]
  else:
    comp=ports[1][:pos2]
    pcomp=ports[1][pos2+1:]
    pself=ports[0]
  return [comp, pcomp, pself]

def link_ports(conn, interfaces, inport=0):
  ports=SVMCORBA_RECORD.eh.ports
  links={}
  foundcomp=SVMCORBA_RECORD.found_comps
  for con in conn:
    pts=parse_ports(con)
    if not pts:
      print 'WARNING: Ignoring invalid connection %s.' % str(con)
      continue
    [comp, pcomp, pself]=pts
    if not comp in interfaces.keys():
      print 'WARNING: Component with identifier "%s" is not available.'%comp
    else:
      if not pself in ports.keys():
	print 'WARNING: Ignoring unrecognized port "%s".'%pself
      else:
	if (not inport and ports[pself][PORT_OUT]) or (inport and ports[pself][PORT_IN]):  # deal with out-ports
	  mdln=interfaces[comp][0]._get_name()
	  inf=random.choice(interfaces[comp][1])  # randomly choose an interface
	  infn=inf._get_name()
	  if not inport:
	    des=inf.describe_interface()
	    for op in des.operations:
	      if pcomp==op.name\
		     and len(op.parameters)==2\
		     and op.parameters[0].type.kind()==CORBA.tk_string\
		     and op.parameters[0].mode==CORBA.PARAM_IN\
		     and op.parameters[1].type.kind()==CORBA.tk_alias:
		if not comp in foundcomp.keys():
		  foundcomp[comp]=regenerate_idl([SVM_MODULE_RE, '\A%s$'%mdln, '\A%s$'%infn])
		links[pself]=[mdln, infn, foundcomp[comp], pcomp]
	  else:
	    if not comp in foundcomp.keys():
	      foundcomp[comp]=regenerate_idl([SVM_MODULE_RE, '\A%s$'%mdln, '\A%s$'%infn])
	    links[pself]=[mdln, infn, foundcomp[comp], pcomp]
  return links

def regenerate_idl(path):
  """ Only support modules, interfaces and operations."""

  if len(path)!=3:
    return None
  orb=SVMCORBA_RECORD.orb
  ctx=orb.resolve_initial_references('InterfaceRepository')

  # resolve SVMMODULE module
  SVM_MODULE=path[0]
  modules=limit_names(ctx.contents(CORBA.dk_Module, 0), SVM_MODULE)
  if not modules:
    return None

  # resolve model specific module
  MODEL_MODULE=path[1]
  models=[]
  for m in modules:
    models=models+limit_names(m.contents(CORBA.dk_Module, 0), MODEL_MODULE)
  if not models:
    return None

  # resolve interface
  SVM_INTERFACE=path[2]
  interfaces=[]
  for m in models:
    interfaces=interfaces+limit_names(m.contents(CORBA.dk_Interface, 0), SVM_INTERFACE)
  if not interfaces:
    return None

  idl_content ='\
//---------------------------------------------\n\
// IDL interface description regenerated by SVM\n\
// Thomas Huining Feng                         \n\
//---------------------------------------------\n\n'
  idl_content=idl_content+'#pragma prefix "msdl.cs.mcgill.ca"\n'
  for m in modules:
    idl_content=idl_content+'\n// Module namespace shared by all SVM models\n\n'
    idl_content=idl_content+'module %s\n' % m._get_name()
    idl_content=idl_content+'{\n'

    for mm in limit_names(m.contents(CORBA.dk_Module, 0), MODEL_MODULE):
      idl_content=idl_content+'    module %s\n' % mm._get_name()
      idl_content=idl_content+'    {\n'
      idl_content=idl_content+'        typedef sequence<any> param_list;\n'
      idl_content=idl_content+'        typedef sequence<string> port_list;\n'
      idl_content=idl_content+'        typedef sequence<string> comp_list;\n'

      for i in limit_names(mm.contents(CORBA.dk_Interface, 0), SVM_INTERFACE):
        upos=find(i._get_name(), '_')
        if upos<0:
	  continue
        idl_content=idl_content+'        interface %s\n' % i._get_name()
        idl_content=idl_content+'        {\n'
        des=i.describe_interface()
        for op in des.operations:
	  rtype=str(op.result.kind())[3:] # remove preceding tk_
	  oname=op.name
	  idl_content=idl_content+'            %s %s(' % (rtype, oname)
	  pai=0
	  while pai<len(op.parameters):
	    pa=op.parameters[pai]
	    if pa.mode==CORBA.PARAM_IN:
	      idl_content=idl_content+'in '
	    elif pa.mode==CORBA.PARAM_OUT:
	      idl_content=idl_content+'out '
	    elif pa.mode==CORBA.PARAM_INOUT:
	      idl_content=idl_content+'inout '
	    if pa.type.kind()==CORBA.tk_alias:
	      ptype=pa.type.name()
	    elif str(pa.type.kind())[0:3]=='tk_':
	      ptype=str(pa.type.kind())[3:]  # remove preceding tk_
	    else:
	      ptype=str(pa.type.kind())
	    pname=pa.name
	    idl_content=idl_content+'%s %s' % (ptype, pname)
	    if pai<len(op.parameters)-1:
	      idl_content=idl_content+', '
	    pai=pai+1
	  idl_content=idl_content+');\n'
        idl_content=idl_content+'        };\n'
      idl_content=idl_content+'    };\n'

    idl_content=idl_content+'};\n'

  return idl_content

def feed_idl(idl_file):
  try:
    from Fnorb.script import fnfeed
    fnfeed.main(['', idl_file])
  except:
    print 'WARNING: Unable to feed idl to interface repository.'
  #os.spawnvp(os.P_WAIT, 'fnfeed', ['fnfeed', idl_file])

def start_service():
  orb=SVMCORBA_RECORD.orb
  boa=BOA.BOA_init()
  ctx=orb.resolve_initial_references("NameService")

  path=[CosNaming.NameComponent('SVM', ''), CosNaming.NameComponent(SVM_MODULE, ''), CosNaming.NameComponent(SVMCORBA_RECORD.module_name, '')]
  for i in range(len(path)):
    try:
      ctx.bind_new_context(path[:i+1])
    except CosNaming.NamingContext.AlreadyBound:
      pass

  interface_name=SVMCORBA_RECORD.module_name+'_'+str(SVMCORBA_RECORD.module_num)
  stubpath=os.path.join(os.path.join(SVMCORBA_RECORD.work_path, 'serverif'), interface_name)
  sys.path=[stubpath]+sys.path
  
  impl=[]
  impl.append('from %s import %s' % (SVM_MODULE, SVMCORBA_RECORD.module_name))
  impl.append('from %s_skel import %s_skel' % (SVM_MODULE, SVMCORBA_RECORD.module_name))
  impl.append('from Fnorb.cos.naming import CosNaming')
  impl.append('import SVMCORBA')

  classdef='class inf_%dImpl(%s_skel.inf_%d_skel):\n' % (SVMCORBA_RECORD.module_num, SVMCORBA_RECORD.module_name, SVMCORBA_RECORD.module_num)
  for p in SVMCORBA_RECORD.ports:
    pp=SVMCORBA_RECORD.ports[p]
    if pp[PORT_IN]:
      classdef=classdef+'\
  def %s(self, event, params):\n\
    SVMCORBA.receive_external_event(%s, event, params)\n' % (p, p)
  classdef=classdef+'\
  def svm_module_add_connection(self, pserver, pclient, components):\n\
    SVMCORBA.svm_module_add_connection(pserver, pclient, components)\n'
  
  impl.append(classdef)
  impl.append('ifimpl=inf_%dImpl()'%SVMCORBA_RECORD.module_num)
  impl.append('ref=boa.create("inf_%d", inf_%dImpl._FNORB_ID)' % (SVMCORBA_RECORD.module_num, SVMCORBA_RECORD.module_num))
  impl.append('ctx.rebind([CosNaming.NameComponent("SVM", ""), CosNaming.NameComponent("%s", ""), CosNaming.NameComponent("%s", ""), CosNaming.NameComponent("inf_%d", "")], ref)'\
	      % (SVM_MODULE, SVMCORBA_RECORD.module_name, SVMCORBA_RECORD.module_num))
  impl.append('boa.obj_is_ready(ref, ifimpl)')
  impl.append('SVMCORBA.SVMCORBA_RECORD.impl=ifimpl')
  
  ii=code.InteractiveInterpreter(locals())
  for i in impl:
    ii.runsource(i)

  del sys.path[0]
  
  ThreadUtil.StartThread(boa._fnorb_mainloop, ())

def init_dns(eventhandler):
  if not SVMCORBA_RECORD.fnorb_installed:
    return RESULT_FNORB_NOT_INSTALLED
  orb=CORBA.ORB_init(FNORB_PARAMETERS)
  # orb._fnorb_override_options({'Threading Model': 'Threaded'})
  if not orb:
    return RESULT_FNORB_NOT_STARTED
  SVMCORBA_RECORD.orb=orb
  
  services=orb.list_initial_services()
  for rs in REQUIRED_SERVICES:
    if not rs in services:
      return RESULT_SERVICE_NOT_FOUND

  ifctx=orb.resolve_initial_references(INTERFACE_REPOSITORY)
  nctx=orb.resolve_initial_references(NAME_SERVICE)

  SVMCORBA_RECORD.nctx=nctx
  SVMCORBA_RECORD.ifctx=ifctx
  SVMCORBA_RECORD.work_path=eventhandler.work_path
  SVMCORBA_RECORD.module_name=eventhandler.options[MODEL_NAME]
  SVMCORBA_RECORD.module_num=eventhandler.internal_prefix
  SVMCORBA_RECORD.ports=eventhandler.ports
  SVMCORBA_RECORD.eh=eventhandler
  
  try:
    os.mkdir(eventhandler.work_path)
  except:
    1

  idl_file=generate_stub()

  interfaces=lookup_interfaces(eventhandler.required_components)
  if interfaces:
    links=link_ports(SVMCORBA_RECORD.eh.required_connections, interfaces)
    generate_link_stub(links)
    SVMCORBA_RECORD.eh.outgoing_table=create_link_table(links)
    links=link_ports(SVMCORBA_RECORD.eh.required_connections, interfaces, 1)
    generate_link_stub(links)
    locate_components(links)

  feed_idl(idl_file)
  start_service()

  if interfaces:
    notify_components(links)

  return RESULT_OK

def remove_path(path):
  os.spawnvp(os.P_WAIT, 'sh', ['sh', '-c', 'rm -rf '+path])

def end_dns():
  if REMOVE_ON_EXIT and SVMCORBA_RECORD.work_path:
    remove_path(SVMCORBA_RECORD.work_path)

def receive_external_event(name, event, params):
  SVMCORBA_RECORD.eh.event(name+'.'+event, params, 0)

def send_external_event(eventhandler, event):
  E=str(event)
  pos=find(E, '.')
  if pos>=0:
    pname=E[:pos]
    ename=E[pos+1:]
    if 'params' in dir(event):
      params=event.params
    else:
      params=[]
    if eventhandler.outgoing_table.has_key(pname):
      for p in eventhandler.outgoing_table[pname]:
	try:
	  p(ename, params)
	except:
	  print 'WARNING: The external event may not be successfully sent.'

def svm_module_add_connection(pserver, pclient, components):
  if len(pserver)!=len(pclient):
    return
  mdln=components[0]
  infn=components[1]
  orb=SVMCORBA_RECORD.orb
  ctx=orb.resolve_initial_references('InterfaceRepository')
  cnts=limit_names(ctx.contents(CORBA.dk_Module, 0), SVM_MODULE_RE)
  if not cnts:
    return
  mdl=limit_names(cnts[0].contents(CORBA.dk_Module, 0), '\A%s$'%mdln)
  if not mdl:
    return
  inf=limit_names(mdl[0].contents(CORBA.dk_Interface, 0), '\A%s$'%infn)
  if not inf:
    return
  interfaces={'':[mdl[0], [inf[0]]]}
  i=0
  ports=[]
  while i<len(pclient):
    ports.append(['.'+pclient[i], pserver[i]])
    i=i+1
  links=link_ports(ports, interfaces)
  generate_link_stub(links)
  newtable=create_link_table(links)
  for k in newtable.keys():
    if not SVMCORBA_RECORD.eh.outgoing_table.has_key(k):
      SVMCORBA_RECORD.eh.outgoing_table[k]=newtable[k]
    else:
      SVMCORBA_RECORD.eh.outgoing_table[k]=SVMCORBA_RECORD.eh.outgoing_table[k]+newtable[k]