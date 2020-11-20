#main.py
#script for python hw - PyBank

#import our modules needed
import os
import csv

#load the file
pybank_csv_path = os.path.join("resources","budget_data.csv")

#create lists to store csv file column data
date = []
profit_loss = []

#create and initialize a new list variable (i.e. column) that will track monthly changes 
monthly_change = []

#create and initialize variables
total_months = 0
total_profit_loss = 0
total_change_profit = 0
average_change_profit = 0
monthly_change_profit_loss = 0
greatest_incr_profit = 0
greatest_decr_profit = 0
final_profit_loss = 0
initial_profit_loss = 0
date_hi_profit = ""
date_low_profit_or_loss = ""

#create a row counter variable to advance for loop
row_count = 0

#open the csv
with open(pybank_csv_path, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ",")
    csv_header =  next(csvreader)
    #print(csvreader)

    #initiate for loop and counter to go through rows
    for r in csvreader:
        row_count = row_count + 1

        #append profit info
        profit_loss.append(r[1])

        #calculate profit by summing up all rows in the column
        total_profit_loss = total_profit_loss + int(r[1])

        #calculate average mo-mo change in profits
        final_profit_loss += int(r[1])
        monthly_change_profit_loss = final_profit_loss - initial_profit_loss
        monthly_change.append(monthly_change_profit_loss)

        total_change_profit = total_change_profit + monthly_change_profit_loss

        #calculate the average change in profits
        average_change_profit = (total_change_profit/row_count)

        #reset final_profit_loss for successive iterations
        final_profit_loss = initial_profit_loss

        #append date info
        date.append(r[0])
       
        #Use min and max functions to find where the highest and lowest profits or losses occured
        greatest_incr_profit = max(monthly_change) 
        greatest_decr_profit = min(monthly_change)

        #use the date index we've created to capture dates of the min/max
        date_hi_profit = date[monthly_change.index(greatest_incr_profit)]
        date_low_profit_or_loss = date[monthly_change.index(greatest_decr_profit)]

    #print the results to match the format desired to terminal
    print("------------------------------")
    print("Financial Analysis")
    print("------------------------------")
    print("Total Months: " + str(row_count))
    print("Total Profit: " + "$" + str(total_profit_loss))
    print("Average Change: " + "$" + str(average_change_profit))
    print("Greatest Increase in Profits: " + str(date_hi_profit) + " $(" + str(greatest_incr_profit) + ")")
    print("Greatest Decrease in Profits: " + str(date_low_profit_or_loss) + " $(" + str(greatest_decr_profit) + ")")
    print("--------------------------")

    #export as text file
with open('pybank_result_summary.txt',  'w') as text:
    text.write("------------------------------\r\n")
    text.write("Financial Analysis" + "\r\n")
    text.write("------------------------------\r\n")
    text.write("Total Months: " + str(row_count) + "\r\n")
    text.write("Total Profit: " + "$" + str(total_profit_loss) + "\r\n")
    text.write("Average Change: " + "$" + str(average_change_profit) + "\r\n")
    text.write("Greatest Increase in Profits: " + str(date_hi_profit) + " $(" + str(greatest_incr_profit) + ")\r\n")
    text.write("Greatest Decrease in Profits: " + str(date_low_profit_or_loss) + " $(" + str(greatest_decr_profit) + ")\r\n")
    text.write("--------------------------\r\n")