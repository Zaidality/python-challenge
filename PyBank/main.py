import os
import csv

csvpath = os.path.join('Resources','budget_data.csv')
report_path = os.path.join('analysis','analysis_report.txt')

# Variables
Total_Months = 0
Total = 0

# opening csv file
with open(csvpath) as csvfile:

    csvreader = csv.reader(csvfile)

    # reading the header + skipping the header
    header = next(csvreader)

    # extracting info from first row
    row1 = next(csvreader)
    Total_Months = Total_Months + 1

    # extracting the total $
    Total += int(row1[1])

    # reading through csv info
    for row in csvreader:

        # tracking total months
        Total_Months += 1

        # summing total P/L of months
        Total += int(row[1])




analysis_report = (
    f"Financial Analysis\n"
    f"---------------------------\n"
    f"Total months: {Total_Months} \n"
    f"Total: {Total} \n"
    


)
# print report
print(analysis_report)

# export report

with open(report_path, 'w') as report_file:
    report_file.write(analysis_report)
