@echo off
color 6
pip install -r requirements.txt
echo DONE!
git pull -f
echo UPDATE DONE!
pause
python leaked.py