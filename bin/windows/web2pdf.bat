@ECHO OFF
REM
REM wget.exe --continue --recursive --level=2 --accept .pdf --no-directories --input-file urls.txt
ECHO Start ...
ECHO +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

IF EXIST urls.txt (
    wget.exe --continue --recursive --level=2 --accept .pdf --input-file urls.txt
) ELSE (
    ECHO "Please put urls into 'urls.txt' file under directory '%CD%'"
)

ECHO +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
ECHO Finished .
PAUSE
