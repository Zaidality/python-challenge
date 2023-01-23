import os
import csv

csvpath = os.path.join('Resources','budget_data.csv')
report_path = os.path.join('analysis','analysis_report.txt')

# Variables
Total_Months = 0
Total = 0
net_change_list = []
Profits_max = 0
Profits_min = 0

# opening csv file
with open(csvpath) as csvfile:

    csvreader = csv.reader(csvfile)

    # reading the header + skipping the header
    header = next(csvreader)

    # extracting info from first row
    row1 = next(csvreader)
    Total_Months = Total_Months + 1
    previous_net = int(row1[1])

    # extracting the total $
    Total += int(row1[1])

    # reading through csv info
    for row in csvreader:

        # tracking total months
        Total_Months += 1

        # summing total P/L of months
        Total += int(row[1])

        # getting net change
        net_change = int(row[1]) - previous_net 
        net_change_list += [net_change]

        # Finding the greatest profit increase
        if int(row[1]) < int(row[1]) - 1:
            Profits_max = row

        # Finding the greatest profit decrease
        if int(row[1]) < int(row[1]) - 1:
            Profits_min = row

# net monthly avg
net_avg = sum(net_change_list) / (int(Total_Months) - 1)

analysis_report = (
    f"Financial Analysis\n"
    f"---------------------------\n"
    f"Total months: {Total_Months} \n"
    f"Total: {Total} \n"
    f"Average Change: {net_avg} \n"
    f"Greatest increase in profits: {Profits_max} \n"
    f"Greatest decrease in profits: {Profits_min} \n"


)
# print report
print(analysis_report)

# export report

with open(report_path, 'w') as report_file:
    report_file.write(analysis_report)
print(net_change_list)