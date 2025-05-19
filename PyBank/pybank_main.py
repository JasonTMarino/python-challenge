# -*- coding: UTF-8 -*-
import csv
import os

# File paths (make sure these folders exist)
file_to_load = os.path.join("Resources", "budget_data.csv")
file_to_output = os.path.join("analysis", "budget_analysis.txt")

# Initialize variables
total_months = 0
total_net = 0
net_change_list = []
months = []

greatest_increase = ["", 0]
greatest_decrease = ["", 0]

with open(file_to_load) as financial_data:
    reader = csv.reader(financial_data)
    header = next(reader)
    first_row = next(reader)
    
    total_months += 1
    total_net += int(first_row[1])
    prev_net = int(first_row[1])

    for row in reader:
        date = row[0]
        net = int(row[1])
        total_months += 1
        total_net += net

        net_change = net - prev_net
        net_change_list.append(net_change)
        months.append(date)

        if net_change > greatest_increase[1]:
            greatest_increase = [date, net_change]
        if net_change < greatest_decrease[1]:
            greatest_decrease = [date, net_change]

        prev_net = net

average_change = round(sum(net_change_list) / len(net_change_list), 2)

output = (
    f"Financial Analysis\n"
    f"----------------------------\n"
    f"Total Months: {total_months}\n"
    f"Total: ${total_net}\n"
    f"Average Change: ${average_change}\n"
    f"Greatest Increase in Profits: {greatest_increase[0]} (${greatest_increase[1]})\n"
    f"Greatest Decrease in Profits: {greatest_decrease[0]} (${greatest_decrease[1]})\n"
)

print(output)

with open(file_to_output, "w") as txt_file:
    txt_file.write(output)
