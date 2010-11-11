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


.PHONY: all clean cleanpyc pypvm applet release releaseapplet binary

find = $(shell which find)
grep = $(shell which grep)
java = $(shell which java)
javac = $(shell which javac)
j2h = $(shell pwd)/lib/java2html/j2h.jar
python = $(shell which python)
tar = $(shell which tar)
mv = $(shell which mv)

pycfiles = `$(find) .|$(grep) "\.pyc$$"`
otherfiles = DNS pypvm.py pypvm_coremodule.dll pypvm_coremodule.so lib/installer/linux/config.dat
examples = CDPlayer DataTypes MP3Player Simple test

version = $(shell python -c "import __version__; print __version__.version")

all: pypvm applet
	$(RM) $(pycfiles)

pypvm:
	$(MAKE) -C lib/pypvm/linux all python=$(python)
	cp lib/pypvm/pypvm.py .

applet:
	$(MAKE) -C test/applet all python=$(python) find=$(find) grep=$(grep) java=$(java) javac=$(javac) j2h=$(j2h)

cleanpyc:
	$(RM) $(pycfiles)

clean:
	$(MAKE) -C test/applet clean
	$(MAKE) -C lib/pypvm/linux clean
	$(RM) $(otherfiles)
	$(RM) -r lib/installer/linux/bincache*
	$(RM) -r svm-$(version)-`uname -s`-`uname -r`-`uname -m` svm-$(version)-`uname -s`-`uname -r`-`uname -m`.tar.gz
	$(RM) warnscc.txt warnsvm.txt warnsvmdns.txt svm.spec scc.spec svmdns.spec
	$(MAKE) -C lib/installer/linux/source/linux clean
	$(RM) $(pycfiles)
	$(RM) *~ pypvm_core.dll
	$(RM) -r buildsvm

release: releaseapplet clean
	cp -r ../svm $(HOME)/svmnightly
	cd $(HOME)/svmnightly && rm -rf `$(find) .|$(grep) CVS`
	cd $(HOME) && tar -zcvf svmnightly.tar.gz svmnightly && rm -rf svmnightly

releaseapplet:
	$(MAKE) -C test/applet release python=$(python) find=$(find) grep=$(grep) javac=$(javac) j2h=$(j2h)

binary: pypvm applet
	$(python) lib/installer/linux/source/linux/Make.py
	$(MAKE) -C lib/installer/linux/source/linux
	PATH=$(PATH):`pwd`/lib/installer/linux/upx && $(python) lib/installer/linux/Configure.py
	$(python) lib/installer/linux/Makespec.py --tk --upx svm.py
	$(python) lib/installer/linux/Makespec.py --upx scc.py
	$(python) lib/installer/linux/Makespec.py --upx svmdns.py
	PATH=$(PATH):`pwd`/lib/installer/linux/upx && $(python) lib/installer/linux/Build.py svm.spec
	PATH=$(PATH):`pwd`/lib/installer/linux/upx && $(python) lib/installer/linux/Build.py scc.spec
	PATH=$(PATH):`pwd`/lib/installer/linux/upx && $(python) lib/installer/linux/Build.py svmdns.spec
	$(mv) distscc/scc distsvm/
	$(mv) distsvmdns/svmdns distsvm/
	$(RM) -r buildsvm buildscc distscc buildsvmdns distsvmdns
	chmod -x distsvm/*.so*
	cp -r $(examples) distsvm/
	cd distsvm && $(RM) -r `$(find) .|$(grep) CVS`
	cp INSTALL.bin.linux README distsvm
	$(mv) distsvm svm-$(version)-`uname -s`-`uname -r`-`uname -m`
	$(tar) -zcvf svm-$(version)-`uname -s`-`uname -r`-`uname -m`.tar.gz svm-$(version)-`uname -s`-`uname -r`-`uname -m`
