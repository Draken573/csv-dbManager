#!/bin/bash
python3 -m ensurepip --default-pip
python3 -m pip install -r requirements.txt
python3 src/main.py
