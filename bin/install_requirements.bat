@echo off

rem Move one directory up
cd..

rem Set root as current working directory
set "cwd=%cd%"
set "venvScripts=venv/Scripts"
set "wheelsDir=libs/.whl"

rem Activate venv
cd %venvScripts%
call activate

rem Change directory to root
cd %cwd%

rem Install framework requirements
call pip install -r requirements.txt

rem Install wheels
cd %wheelsDir%
for %%x in (*.whl) do call pip install %%x

rem Deactivate venv
cd %cwd%/%venvScripts%
call deactivate

rem Change directory to root
cd %cwd%

rem Exit but keep console open
cmd /k
