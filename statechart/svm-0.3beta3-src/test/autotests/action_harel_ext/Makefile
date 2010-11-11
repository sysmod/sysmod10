.phony: all full scc svm python cpp java csharp

TESTS = test1.des test2.des test3.des test4.des test5.des test6.des test7.des \
        test8.des test9.des test10.des

SVM_SUCC = $(TESTS:.des=.svmsucc)

PYTHON_SUCC = $(TESTS:.des=.pysucc)
PYTHON_SOURCE = $(TESTS:.des=.py)

CPP_SUCC = $(TESTS:.des=.cppsucc)
CPP_SOURCE = $(TESTS:.des=.cpp)
CPP_BINARY = $(TESTS:.des=) $(TESTS:.des=.exe)

OUTFILE = outfile

all: svm python

full: svm scc

svm: $(SVM_SUCC)
	$(RM) $(SVM_SUCC)
	$(RM) $(OUTFILE)

%.svmsucc: %.des %.output
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

%.pysucc: %.des %.output
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

%.cppsucc: %.des %.output
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

java:

csharp:
