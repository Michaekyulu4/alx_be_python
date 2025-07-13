monthly_income = int(input("Enter your total monthly income")) #Prompting the user to feed their monthly income.
monthly_expenses = int(input ("Enter your total monthly expenses"))#Prompting the user to feed the monthly expenses

monthly_savings = monthly_income - monthly_expenses #calculating the monthly savings through subtraction


projected_savings = monthly_savings * 12 + (monthly_savings * 12 * 0.05) #Calculating the projected savings for the whole year

print(monthly_savings)
print(projected_savings)


                     
