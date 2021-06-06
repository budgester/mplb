#!/bin/bash

python3 -m venv .load-venv

source .load-venv/bin/activate

pip3 install -r requirements.txt

locust -V

locust --config config.py
