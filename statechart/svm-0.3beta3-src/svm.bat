@echo off

set params=
:start_shift
if "%1"=="" goto end_shift
set params=%params% %1
shift
goto start_shift
:end_shift

set path_name=
set program_name=svm.py
if exist %program_name% set path_name=%program_name%
for %%d in (%path%) do if exist %%d\%program_name% set path_name=%%d\%program_name%
for %%d in (%path%) do if exist %%d%program_name% set path_name=%%d%program_name%
for %%d in (%pythonpath%) do if exist %%d\%program_name% set path_name=%%d\%program_name%
for %%d in (%pythonpath%) do if exist %%d%program_name% set path_name=%%d%program_name%

if not "%path_name%"=="" goto start_svm
echo Could not find %program_name% in the current directory, PATH or PYTHONPATH.
goto exit_script
:start_svm
python %path_name% %params%
:exit_script