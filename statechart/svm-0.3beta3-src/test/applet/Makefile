.PHONY: all clean release

find = $(shell which find)
grep = $(shell which grep)
java = $(shell which java)
javac = $(shell which javac)
python = $(shell which python)
j2h = ../../lib/java2html/j2h.jar
SHELL = bash

javafiles = `$(find) .|$(grep) "\.java$$"|$(grep) -v "svmapplet\.java$$"`
classfiles = `$(find) .|$(grep) "\.class$$"`
htmlfiles = `$(find) .|$(grep) "\.java\.html$$"`
cleanfiles = $(javafiles) $(classfiles) $(htmlfiles)

all: sample.class svmapplet.class sample.java.html svmapplet.java.html

sample.java.html svmapplet.java.html: sample.java svmapplet.java
	UNAME=`uname`; \
	if [ "$${UNAME#CYGWIN}" != "$$UNAME" ]; then \
	  $(java) -jar "`cygpath -w $(j2h)`" -js . -d tmp; \
	else \
	  $(java) -jar "$(j2h)" -js . -d tmp; \
	fi
	cp tmp/*.java.html .
	$(RM) -r tmp

svmapplet.class: svmapplet.java
	$(javac) svmapplet.java

sample.class: sample.java
	$(javac) sample.java

sample.java:
	$(python) ../../scc.py sample.des	

clean:
	$(RM) $(cleanfiles)

release: all
	cp -r . $(HOME)/svmapplet
	cd $(HOME)/svmapplet && rm -rf `find|grep CVS` && cd .. && tar -zcvf svmapplet.tar.gz svmapplet
	$(RM) -r $(HOME)/svmapplet
