.phony: all full scc svm python cpp java csharp

TESTS = test1.des test2.des test3.des test4.des test5.des test6.des test7.des \
        test8.des

SVM_SUCC = $(TESTS:.des=.svmsucc)

PYTHON_SUCC = $(TESTS:.des=.pysucc)
PYTHON_SOURCE = $(TESTS:.des=.py)

CPP_SUCC = $(TESTS:.des=.cppsucc)
CPP_SOURCE = $(TESTS:.des=.cpp)
CPP_BINARY = $(TESTS:.des=) $(TESTS:.des=.exe)

JAVA_SUCC = $(TESTS:.des=.javasucc)
JAVA_SOURCE = $(TESTS:.des=.java)
JAVA_BINARY = $(TESTS:.des=.class) EventList.class Hierarchy.class History.class State.class StateMachine.class StringList.class

CS_SUCC = $(TESTS:.des=.cssucc)
CS_SOURCE = $(TESTS:.des=.cs)
CS_BINARY = $(TESTS:.des=.exe)

OUTFILE = outfile

all: svm python

full: svm scc

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

scc: python cpp java csharp

python: $(PYTHON_SUCC)
	$(RM) $(PYTHON_SUCC)
	$(RM) $(PYTHON_SOURCE)
	$(RM) $(OUTFILE)

%.pysucc: %.des %.input %.output
	scc -lpython $<
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
	scc -lcpp $<
	`scc -c -lcpp $<`
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

java: $(JAVA_SUCC)
	$(RM) $(JAVA_SUCC)
	$(RM) $(JAVA_SOURCE)
	$(RM) $(JAVA_BINARY)
	$(RM) $(OUTFILE)

%.javasucc: %.des %.input %.output
	scc -ljava $<
	`scc -c -ljava $<`
	java `basename $< .des` < `basename $< .des`.input > $(OUTFILE)
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

csharp: $(CS_SUCC)
	$(RM) $(CS_SUCC)
	$(RM) $(CS_SOURCE)
	$(RM) $(CS_BINARY)
	$(RM) $(OUTFILE)

%.cssucc: %.des %.input %.output
	scc -lcsharp $<
	`scc -c -lcsharp $<`
	mono `basename $< .des`.exe < `basename $< .des`.input > $(OUTFILE)
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
