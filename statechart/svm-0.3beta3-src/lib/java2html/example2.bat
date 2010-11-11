@echo off
set JAVA_HOME_J2H=C:\j2sdk1.4.0
j2h -js  %JAVA_HOME_J2H%\demo\jfc\SwingSet2 -d examples\SwingSet_demo -jd %JAVA_HOME_J2H%\docs\api http://java.sun.com/products/jdk/1.4/docs/api -n SwingSet_DEMO -m 4
