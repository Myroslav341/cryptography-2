#!/bin/bash

python -m venv venv
source venv/Scripts/activate
python -m pip install --upgrade pip
pip install --upgrade -r requirements.txt