.phony: all full copy scc svm python cpp java csharp

TESTS = test1.des test2.des test3.des test4.des test5.des

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
	cp ../final_harel_nonext/*.des ../final_harel_nonext/*.input ../final_harel_nonext/*.output .

clean:
	$(RM) `ls -I Makefile -I CVS`

java:

csharp:
