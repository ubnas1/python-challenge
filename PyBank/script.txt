# importing modules

import os
import csv

# providing file path to file_path variable

file_path = os.path.join("pybank","Resources", "budget_data.csv")

# opening file using open function

with open(file_path) as csv_file:

#   putting all the values in csv_reader variable seperated by a comma

    csv_reader = csv.reader(csv_file, delimiter=",")

#   skipping header using next function

    next(csv_reader)

#   initialsing greatest increase and greatest decrease variables

    gr_inc = 0
    gr_dec = 0

#   making empty lists for dates profit/loss and changes in profit/loss

    date = []
    pro_loss = []
    change = []

#   initialising variables for total sum and total months

    total_sum = 0
    total_months = 0

#   now going through all values using for loop

    for row in csv_reader:

#       add all the values in profit/loss column 

        total_sum += int(row[1])

#       counter to find total number of months

        total_months += 1

#       append all the dates to the date list

        date.append(row[0])

#       append all the profit/loss values to the list

        pro_loss.append(int(row[1]))

#   going through the profit/lost list

    for i in range(1, len(pro_loss)):

#       calculate values of change by subtracting previous value from current
#       and appending to the change list

        change.append(pro_loss[i] - pro_loss[i-1])






#   calculating average of change list

    avg_change = sum(change)/len(change)

#   finding maximun profit increase and decrease and assign the values to the variable

    max_profit_increase = max(change)
    min_profit_increase = min(change)

#   finding month of maximum profit

    max_profit_increase_date = str(date[change.index(max_profit_increase)+1])

#   finding month of minimum profit increase (maximum loss)

    min_profit_increase_date = str(date[change.index(min_profit_increase)+1])

#   print analysis

print(" ")
print("  Financial Analysis")
print("  ------------------")
print(" ")
print(f'Total Months: {total_months}')
print(" ")
print(f'Total Revenue: {total_sum}')
print(" ")
print(f'Average Change: {round(avg_change, 2)}')  
print(" ")
print(f'Greatest increase in profits: | {max_profit_increase_date} | <--> {max_profit_increase}')
print(" ")
print(f'Greatest Decrease in profits: | {min_profit_increase_date} | <--> {min_profit_increase}')
print(" ")

#  providing text file path to variable

text_file_path = os.path.join("PyBank","Analysis", "analysis.txt")

# print analysis to text file

with open(text_file_path,"w") as handle:
    handle.write(f"  Financial Analysis \n ------------------ \n Total Months: {total_months} \n Total Revenue: {total_sum} \n Average Change: {round(avg_change, 2)} \n")
    handle.write(f' Greatest increase in profits: | {max_profit_increase_date} | <--> {max_profit_increase} \n Greatest Decrease in profits: | {min_profit_increase_date} | <--> {min_profit_increase} \n')



# ------------------------------------------
#      Test Function
# ------------------------------------------


    # for j in range(len(change)):
    #     print(f'{date[j]} :  {change[j]}')