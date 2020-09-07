import os
import csv

pybank_csv = os.path.join("Resources","02-Homework_03-Python_Instructions_PyBank_Resources_budget_data.csv")

dates = []
profitlosses = []
changes = []


with open(pybank_csv) as csvfile:
    csvreader = csv.reader(csvfile,delimiter=",")
    csv_header = next(csvreader)

    for row in csvreader:
        dates.append(row[0])
        profitlosses.append(int(row[1]))

for i in range(len(profitlosses)-1):
    changes.append(int(profitlosses[i+1])-int(profitlosses[i]))


total_month = int(len(dates))
total_profitlosses = sum(profitlosses)
average_change = round(sum(changes)/int(len(changes)),2)
max_increase = max(changes)
maxincrease_month = dates[changes.index(max_increase)+1]
max_decrease = min(changes)
maxdecrease_month = dates[changes.index(max_decrease)+1] 

summary = f'''
Financial Analysis
-------------------------------
Total Months: {total_month}
Total: ${total_profitlosses}
Average Change: ${average_change}
Greatest Increase in Profits: {maxincrease_month} (${max_increase})
Greatest Decrease in Profits: {maxdecrease_month} (${max_decrease})
'''

txtfile_path = os.path.join("analysis","Output.txt")

f = open(txtfile_path, "w")
f.write(summary)
f.close()

