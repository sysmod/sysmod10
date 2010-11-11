.PHONY: all clean

python = $(shell which python)
gcc = $(shell which gcc)
SHELL = bash

PY_INC = `$(python) -c "import sys, os; print os.path.join(os.path.join(sys.prefix, 'include'), 'python'+sys.version[:3])"`
PY_LIB = `$(python) -c "import sys, os; print os.path.join(os.path.join(os.path.join(sys.prefix, 'lib'), 'python'+sys.version[:3]), 'config')"`
LD_PY_LIB = `$(python) -c "import sys; print 'python'+sys.version[:3]"`

all:: pypvm_coremodule.o
	UNAME=`uname`; \
	if [ "$${UNAME#CYGWIN}" != "$$UNAME" ]; then \
	  LD_RPC_LIB=-lrpclib; \
	  TARGET=pypvm_coremodule.dll; \
	else \
	  TARGET=pypvm_coremodule.so; \
	fi; \
	$(gcc) -shared -L/usr/local/lib -L$(PVM_ROOT)/lib/$(PVM_ARCH) -L$(PY_LIB) ./pypvm_coremodule.o -lpvm3 -lgpvm3 -l$(LD_PY_LIB) $$LD_RPC_LIB -o ../../../$$TARGET

pypvm_coremodule.o: pypvm_coremodule_formatted.c
	$(gcc) -fPIC -DNDEBUG -g -O3 -Wall -Wstrict-prototypes -I/usr/local/include -I$(PY_INC) -I$(PVM_ROOT)/include -DHAVE_CONFIG_H -c ././pypvm_coremodule_formatted.c -o ./pypvm_coremodule.o

pypvm_coremodule_formatted.c: pypvm_coremodule.c
	$(python) format.py pypvm_coremodule.c > pypvm_coremodule_formatted.c

clean:
	$(RM) *.o
	$(RM) *.so
	$(RM) *.dll
	$(RM) pypvm_coremodule_formatted.c
