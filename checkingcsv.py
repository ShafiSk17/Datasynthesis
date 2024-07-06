import os
import csv

def read_csv(file_path):
    with open(file_path, "r", newline="") as csvfile:
        reader = csv.reader(csvfile)
        # Process CSV data here
        ...

# Assuming agents.py and sample.csv are in the same directory
file_path = os.path.join(os.path.dirname(__file__), 'data', 'sample.csv')
sample_data = read_csv(file_path)