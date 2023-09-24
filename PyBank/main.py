# Print the title
print("Financial Analysis")
print("------------------------")

# Import modules
import os
import csv
import statistics

# Path to the CSV data
pybank_data = os.path.join("Resources/budget_data.csv")

# Read the CSV data without the header
with open(pybank_data, encoding='UTF-8') as csvfile:
    pybank_data_csv = csv.reader(csvfile, delimiter=",")
    header = next(pybank_data_csv)

    # Initialize variables
    month_count = 0
    total_amount = 0
    g_increase = 0
    gi_month = ''
    g_decrease = 0
    gd_month = ''

    monthly_amount = []
    monthly_date = []

    # The total number of months included in the dataset
    # The net total amount of "Profit/Losses" over the entire period
    for x in pybank_data_csv:
        month_count += 1
        total_amount += int(x[1])
        monthly_amount.append(int(x[1]))
        monthly_date.append(x[0])
        
    print("Total Months: ", month_count)
    print(f"Total: ${total_amount}")
    
    # The changes in "Profit/Losses" over the entire period, and then the average of those changes 
    monthly_change = []
    monthly_date_change = []
    
    for y in range(len(monthly_amount)-1):
        change = monthly_amount[y+1] - monthly_amount[y]
        monthly_change.append(change)
        monthly_date_change.append(monthly_date[y+1])

    # The greatest increase in profits (date and amount) over the entire period
    # The greatest decrease in profits (date and amount) over the entire period
    g_increase = monthly_change[0]
    g_decrease = monthly_change[0]        
    for z in range(len(monthly_change)-1):
        if monthly_change[z+1] > g_increase:
            g_increase = monthly_change[z+1]
            gi_month = monthly_date_change[z+1]
        if monthly_change[z+1] < g_decrease:
            g_decrease = monthly_change[z+1]
            gd_month = monthly_date_change[z+1]

    average_monthly_change = statistics.mean(monthly_change)
    print("Average Change: $", round(average_monthly_change,2))
    print("Greatest Increase in Profits: ", gi_month, "($"+ str(round(g_increase,2))+")")
    print("Greatest Decrease in Profits: ", gd_month, "($"+ str(round(g_decrease,2))+")")
   

# Print the resutls to txt file
print("Financial Analysis", file=open("analysis/Pybank.txt", "a"))
print("------------------------", file=open("analysis/Pybank.txt", "a"))
print(f"Total Months: {month_count}", file=open("analysis/Pybank.txt", "a"))
print(f"Total: ${total_amount}", file=open("analysis/Pybank.txt", "a"))
print(f"Average Change: ${round(average_monthly_change,2)}", file=open("analysis/Pybank.txt", "a"))
print(f"Greatest Increase in Profits: {gi_month} (${str(round(g_increase,2))})", file=open("analysis/Pybank.txt", "a"))
print(f"Greatest Decrease in Profits: {gd_month} (${str(round(g_decrease,2))})", file=open("analysis/Pybank.txt", "a"))