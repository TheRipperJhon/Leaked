#!/bin/bash
sudo -H pip3 install -r requirements.txt
sudo -H pip install -r requirements.txt
echo "DONE!"
sudo git pull -f
echo "UPDATED DONE!"
python3 leaked.py