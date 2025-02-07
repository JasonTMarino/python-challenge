# Dependencies
import csv
import os

# Files to load and output (updated with correct file paths)
file_to_load = os.path.join("Resources", "budget_data.csv")  # Input file path
file_to_output = os.path.join("analysis", "budget_analysis.txt")  # Output file path

# Variables to track the financial data
total_months = 0
total_net = 0

# Opens and reads the csv, skips the header row
with open(file_to_load) as financial_data:
    reader = csv.reader(financial_data)
    header = next(reader)