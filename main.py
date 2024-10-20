employeeName = input("Enter employee's name: ")
numShifts = input("Enter number of shifts: ")
numTransactions = input("Enter number of transactions: ")
transactionValue = input("Enter transaction dollar value: ")

maxBonus = 200.00
minBonus = 50.00
secondBonus = 75.00
thirdBonus = 100.00

#Productivity Score Calculation
productivityScore = (int(transactionValue) / int(numTransactions)) / int(numShifts)
#Output
print(employeeName)
#If Statements
if productivityScore <= 30:
  print("Employee Bonus: $" + str(minBonus))
elif productivityScore > 31 and productivityScore <= 69:
  print("Employee Bonus: $" + str(secondBonus))
elif productivityScore > 69 and productivityScore <= 199:
  print("Employee Bonus: $" + str(thirdBonus))
elif productivityScore >= 200:
  print("Employee Bonus: $" + str(maxBonus))
