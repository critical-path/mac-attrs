#!/bin/bash

# Fetch `oui.csv` from the IEEE's website.
curl http://standards-oui.ieee.org/oui/oui.csv > oui.csv

# Fetch `cid.csv` from the IEEE's website. 
curl http://standards-oui.ieee.org/cid/cid.csv > cid.csv

# Create, train, test, and save a classifier using `oui.csv` and `cid.csv`.
python3 create_train_test_save.py
