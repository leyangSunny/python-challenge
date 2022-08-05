from audioop import avg
import os
import csv
import statistics

budget_data = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'resources', 'budget_data.csv')

average_change = 0
Total_month = 0 
Total_profitloss = 0
Totalchange = 0
greatest_increase = 0
greatest_decrease = 0
monthly_Changes = 0
increase_date = []
decrease_date = []
profitloss = []
date = []
monthly_Changes_list = [] 
a = []
count = []
first_change = 0
Snd_change = 0
date=[]


with open(budget_data, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)
   

    # Read each row of data after the header
    for count in csvreader:
      Total_month = Total_month + 1
    #The net total amount of "Profit/Losses" over the entire period
      profitloss.append(count[1])
      Total_profitloss = Total_profitloss +int(count[1])
      # Changes 
      date.append(count[0])
      Snd_change=int(count[1])
      monthly_Changes = Snd_change - first_change
      monthly_Changes_list.append(monthly_Changes)
      Totalchange= Totalchange + monthly_Changes
      first_change = Snd_change

      # The greatest increase/ in profits (date and amount) over the entire period/ average
      greatest_increase = max(monthly_Changes_list)
      greatest_decrease = min(monthly_Changes_list) 
      increase_date = date[monthly_Changes_list.index(greatest_increase)]
      decrease_date = date[monthly_Changes_list.index(greatest_decrease)]
      average_change = (int(Totalchange) / int(Total_month))
      
  # Office hour 
   # if int(count[1]) < greatest_decrease:
   #        greatest_decrease = int(count[1])
   #        decrease_date = (count[0])
   #increase
   #if int(count[1]) > greatest_increase:
   #        greatest_increase = int(count[1])
   #        increase_date = (count[0])
   


print("--------------------")
print("Financial Analysis")
print("--------------------")
print("Total Months: " + str(Total_month))
print("Total Profits: " + "$" + str(Total_profitloss))
print("Average Change: " + "$" + str(int(average_change)))
print("Greatest Increase in Profits: " + str(increase_date) + " ($" + str(greatest_increase) + ")")
print("Greatest Decrease in Profits: " + str(decrease_date) + " ($" + str(greatest_decrease)+ ")")
print("---------------------")

with open('financial_analysis.txt', 'w') as text:
    text.write("-----------------\n")
    text.write("Financial Analysis"+ "\n")
    text.write("-----------------\n\n")
    text.write("Total Months: " + str(Total_month) + "\n")
    text.write("Total Profits: " + "$" + str(Total_profitloss) +"\n")
    text.write("Average Change: " + '$' + str(int(average_change)) + "\n")
    text.write("Greatest Increase in Profits: " + str(increase_date) + " ($" + str(greatest_increase) + ")\n")
    text.write("Greatest Decrease in Profits: " + str(decrease_date) + " ($" + str(greatest_decrease) + ")\n")
    text.write("---------------------\n")
