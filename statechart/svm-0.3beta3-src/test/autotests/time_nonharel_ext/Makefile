.phony: all full copy scc svm python cpp java csharp

TESTS = test1.des test2.des test3.des test4.des test5.des test6.des test7.des

SVM_SUCC = $(TESTS:.des=.svmsucc)

PYTHON_SUCC = $(TESTS:.des=.pysucc)
PYTHON_SOURCE = $(TESTS:.des=.py)

CPP_SUCC = $(TESTS:.des=.cppsucc)
CPP_SOURCE = $(TESTS:.des=.cpp)
CPP_BINARY = $(TESTS:.des=) $(TESTS:.des=.exe)

OUTFILE = outfile

LOCAL_OUTPUTS = Makefile test6.output test7.output

all: copy
	$(MAKE) svm python clean

full: copy
	$(MAKE) svm scc clean

svm: $(SVM_SUCC)
	$(RM) $(SVM_SUCC)
	$(RM) $(OUTFILE)

%.svmsucc: %.des %.output
	svm -t $< > $(OUTFILE)
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
	python `basename $< .des`.py > $(OUTFILE)
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
	./`basename $< .des` > $(OUTFILE)
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
	cp ../time_harel_ext/*.des .
	output_files=`cd ../time_harel_ext && ls *.output`; \
	for excluded in $(LOCAL_OUTPUTS); do \
	  output_files=`echo $$output_files | sed "s/$$excluded//"`; \
	done; \
	for output in $$output_files; do \
	  cp ../time_harel_ext/$$output .; \
	done
	for fn in *.des; do \
	  echo "OPTIONS:" > tmp; \
	  echo "  Harel = 0" >> tmp; \
	  echo >> tmp; \
	  cat $$fn >> tmp; \
	  mv tmp $$fn; \
	done

clean:
	delete_files=`ls -I CVS`; \
	for excluded in $(LOCAL_OUTPUTS); do \
	  delete_files=`echo $$delete_files | sed "s/$$excluded//"`; \
	done; \
	$(RM) $$delete_files

java:

csharp:
