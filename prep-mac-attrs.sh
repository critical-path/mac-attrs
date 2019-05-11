#!/bin/bash

echo "Fetching 'oui.csv' from the IEEE's website..."
echo
curl http://standards-oui.ieee.org/oui/oui.csv > oui.csv

echo "Fetching 'cid.csv' from the IEEE's website..."
echo
curl http://standards-oui.ieee.org/cid/cid.csv > cid.csv

echo "Creating, training, testing, and saving a classifier using 'oui.csv' and 'cid.csv'..."
echo 
python3 create_train_test_save.py
