.phony: all full copy scc svm python cpp java csharp

TESTS = test1.des test2.des test3.des test4.des test5.des test6.des test7.des \
        test8.des test9.des test10.des

LOCAL_FILES = Makefile \
              test9.des test9.input test9.output \
              test10.des test10.input test10.output

SVM_SUCC = $(TESTS:.des=.svmsucc)

PYTHON_SUCC = $(TESTS:.des=.pysucc)
PYTHON_SOURCE = $(TESTS:.des=.py)

CPP_SUCC = $(TESTS:.des=.cppsucc)
CPP_SOURCE = $(TESTS:.des=.cpp)
CPP_BINARY = $(TESTS:.des=) $(TESTS:.des=.exe)

OUTFILE = outfile

all: copy
	$(MAKE) svm python clean

full: copy
	$(MAKE) svm scc clean

svm: $(SVM_SUCC)
	$(RM) $(SVM_SUCC)
	$(RM) $(OUTFILE)

%.svmsucc: %.des %.input %.output
	svm -t $< < `basename $< .des`.input > $(OUTFILE)
	outname=`basename $< .des`.output; \
	if diff -y $$outname outfile; then \
	  echo "" > $@; \
	  echo SUCCESS: $<; \
	  echo; \
	  echo; \
	else \
	  echo FAILURE: $<; \
	  echo; \
	  echo; \
	  exit 1; \
	fi

scc: python cpp

python: $(PYTHON_SUCC)
	$(RM) $(PYTHON_SUCC)
	$(RM) $(PYTHON_SOURCE)
	$(RM) $(OUTFILE)

%.pysucc: %.des %.input %.output
	scc -lpython --ext $<
	python `basename $< .des`.py < `basename $< .des`.input > $(OUTFILE)
	outname=`basename $< .des`.output; \
	if diff -y $$outname outfile; then \
	  echo "" > $@; \
	  echo SUCCESS: $<; \
	  echo; \
	  echo; \
	else \
	  echo FAILURE: $<; \
	  echo; \
	  echo; \
	  exit 1; \
	fi

cpp: $(CPP_SUCC)
	$(RM) $(CPP_SUCC)
	$(RM) $(CPP_SOURCE)
	$(RM) $(CPP_BINARY)
	$(RM) $(OUTFILE)

%.cppsucc: %.des %.input %.output
	scc -lcpp --ext $<
	`scc -c -lcpp --ext $<`
	./`basename $< .des` < `basename $< .des`.input > $(OUTFILE)
	outname=`basename $< .des`.output; \
	if diff -y $$outname outfile; then \
	  echo "" > $@; \
	  echo SUCCESS: $<; \
	  echo; \
	  echo; \
	else \
	  echo FAILURE: $<; \
	  echo; \
	  echo; \
	  exit 1; \
	fi

copy:
	cp ../priority_harel_nonext/*.des ../priority_harel_nonext/*.input ../priority_harel_nonext/*.output .

clean:
	delete_files=`ls -I unsupported -I CVS`; \
	for excluded in $(LOCAL_FILES); do \
	  delete_files=`echo $$delete_files | sed "s/$$excluded//"`; \
	done; \
	$(RM) $$delete_files

java:

csharp:
