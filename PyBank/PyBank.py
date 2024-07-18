import pandas as pd
#File Path
file_path = 'python-challenge/PyBank/Resources/budget_data.csv'
#Read file
data = pd.read_csv(file_path)
#set up int and string
total_months = data['Date'].nunique()
total_profit = data['Profit/Losses'].sum()
data['Monthly Change'] = data['Profit/Losses'].diff()
average_change = data['Monthly Change'].mean()
#Print flame and value
print("Financial Analysis")
print("----------------------------")
print(f"Total Months: {total_months}")
print(f"Total: ${total_profit}")
print(f"Average Change: ${average_change:.2f}")
#find out greatest increase&decrease
greatest_increase = data.loc[data['Monthly Change'].idxmax()]
greatest_decrease = data.loc[data['Monthly Change'].idxmin()]
#print out
print(f"Greatest Increase in Profits: {greatest_increase['Date']} (${greatest_increase['Monthly Change']})")
print(f"Greatest Decrease in Profits: {greatest_decrease['Date']} (${greatest_decrease['Monthly Change']})")
