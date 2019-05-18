#!/bin/bash

echo "Fetching 'oui.csv' from the IEEE's website..."
curl -s http://standards-oui.ieee.org/oui/oui.csv > oui.csv

echo "Fetching 'cid.csv' from the IEEE's website..."
curl -s http://standards-oui.ieee.org/cid/cid.csv > cid.csv

echo "Making, training, testing, and saving a classifier..."
python3 make_train_test_save.py
