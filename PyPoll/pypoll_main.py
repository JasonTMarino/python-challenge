# -*- coding: UTF-8 -*-
"""PyPoll Homework Complete Script."""

# Import necessary modules
import csv
import os

# Files to load and output
file_to_load = os.path.join("Resources", "election_data.csv")
file_to_output = os.path.join("analysis", "election_analysis.txt")

# Initialize variables
total_votes = 0
candidate_votes = {}

# Open the CSV file and process it
with open(file_to_load) as election_data:
    reader = csv.reader(election_data)
    header = next(reader)

    for row in reader:
        total_votes += 1
        candidate_name = row[2]

        if candidate_name not in candidate_votes:
            candidate_votes[candidate_name] = 0

        candidate_votes[candidate_name] += 1

# Determine the winner
winning_candidate = ""
winning_count = 0

# Build output lines
output_lines = []
output_lines.append("Election Results")
output_lines.append("-------------------------")
output_lines.append(f"Total Votes: {total_votes}")
output_lines.append("-------------------------")

for candidate in candidate_votes:
    votes = candidate_votes[candidate]
    vote_percentage = (votes / total_votes) * 100
    output_lines.append(f"{candidate}: {vote_percentage:.3f}% ({votes})")

    if votes > winning_count:
        winning_candidate = candidate
        winning_count = votes

output_lines.append("-------------------------")
output_lines.append(f"Winner: {winning_candidate}")
output_lines.append("-------------------------")

# Print results to terminal
for line in output_lines:
    print(line)

# Save results to a text file
with open(file_to_output, "w") as txt_file:
    for line in output_lines:
        txt_file.write(line + "\n")
