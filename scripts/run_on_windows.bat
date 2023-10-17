@echo off
python -m ensurepip --default-pip
python -m pip install -r requirements.txt
python src/main.py
