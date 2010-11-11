#!/bin/bash

export PYTHONPATH="`pwd`/svm-0.3beta3-src:`pwd`/startingpoint"
java -jar xmi2svm2.jar startingpoint/statechart.xmi > startingpoint/statechart.des
cd startingpoint
../svm-0.3beta3-src/svm -i Header.des statechart.des
