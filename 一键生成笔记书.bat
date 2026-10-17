@echo off
chcp 65001 >nul
setlocal
rem ============================================================
rem  Rebuild the two note books (HTML + DOCX) and open the HTML.
rem  Just double-click this file.
rem ============================================================
set "PY=%USERPROFILE%\.dsh\dsh-runtimes\dsh-primary-runtime\dependencies\python\python.exe"
if not exist "%PY%" set "PY=python"
"%PY%" "%~dp0notes\tools\build_book.py" --open
echo.
if errorlevel 1 (
    echo [FAILED] Build failed. Send the error above to your AI assistant.
) else (
    echo [OK] Books generated in the notes\book\ folder.
    echo      - HTML book: double-click to read in browser
    echo      - Word book: open with WPS/Word ^(View - Navigation Pane^)
)
echo.
pause
endlocal
