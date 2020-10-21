@ECHO off
SETLOCAL
CALL :find_dp0

IF EXIST "%dp0%\sh.exe" (
  SET "_prog=%dp0%\sh.exe"
) ELSE (
  SET "_prog=sh"
  SET PATHEXT=%PATHEXT:;.JS;=;%
)

"%_prog%"  "%dp0%\..\jetifier\bin\jetifier-standalone" %*
ENDLOCAL
EXIT /b %errorlevel%
:find_dp0
SET dp0=%~dp0
EXIT /b
