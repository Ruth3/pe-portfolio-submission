#!/bin/bash
set -e

export TESTING=true
python3 -m unittest discover -s tests -p "test_*.py" -v
