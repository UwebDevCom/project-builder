@echo off
REM Git post-commit hook for Windows (no Git Bash required).
REM
REM INSTALL:
REM   copy .claude\plugins\project-builder\scripts\post-commit.bat .git\hooks\post-commit
REM   (Git on Windows runs .bat hooks automatically)

for /f %%i in ('git rev-parse HEAD') do set COMMIT_HASH=%%i
for /f "tokens=*" %%i in ('git log -1 --pretty^=%%B') do set COMMIT_MSG=%%i
for /f "tokens=*" %%i in ('git log -1 --pretty^=%%an') do set COMMIT_AUTHOR=%%i
for /f %%i in ('powershell -command "Get-Date -Format yyyy-MM-dd"') do set COMMIT_DATE=%%i

for /f "tokens=*" %%i in ('git rev-parse --show-toplevel') do set REPO_ROOT=%%i
set SCRIPT=%REPO_ROOT%\.claude\plugins\project-builder\scripts\mine-commit.py

start /b python "%SCRIPT%" ^
  --hash "%COMMIT_HASH%" ^
  --author "%COMMIT_AUTHOR%" ^
  --message "%COMMIT_MSG%" ^
  --date "%COMMIT_DATE%"
