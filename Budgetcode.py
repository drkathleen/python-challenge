
import os
import csv

#set csv path
budgetCSV = os.path.join('Resources', 'budget_data.csv')
foutput = os.path.join('budget_results.txt')

#parameters
totalMonths = 0
Changemonth = []
Change = []
greatestIncrease = ["", 0]
greatestDecrease = ["", 99999999999]
totalNet = 0

#read CSV file
with open(budgetCSV) as financial_data:
 reader = csv.reader(financial_data)
 header = next(reader)

 first_row = next(reader)
 totalMonths = totalMonths + 1
 totalNet = totalNet +int(first_row[1])
 prevNet= int(first_row[1])

 for row in reader:

   #total
   totalMonths = totalMonths + 1
   totalNet = totalNet + int(row[1])

   #net change
   netChange = int(row[1]) - prevNet
   prevNet = int(row[1])
   Change = Change + [netChange]
   Changemonth = Changemonth + [row[0]]

   #greatest decrease
   if netChange < greatestDecrease[1]:
     greatestDecrease[0] = row[0]
     greatestDecrease[1] = netChange

   #greatest increase
   if netChange > greatestIncrease[1]:
     greatestIncrease[0] = row[0]
     greatestIncrease[1] = netChange
     
monthAverage = sum(Change) / len(Change)

#Prints
output = (
   f"Financial Analysis"
   f"\n"
   f"Total Months: {totalMonths}\n"
   f"Total: ${totalNet}\n"
   f"Average Change: ${monthAverage}\n"
   f"Greatest Increase in Profits: {greatestIncrease[0]} (${greatestIncrease[1]})\n"
   f"Greatest Decrease in Profits: {greatestDecrease[0]} (${greatestDecrease[1]})")

print(output)

#export txt file
with open(foutput,'w') as txt_file:
 txt_file.write(output)
