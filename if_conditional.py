

#Question 17:Bank loan approval

creditscore=int(input("What is your credit score?")) #input
income=int(input("Amount of money")) #input
if creditscore>=700: #if credit score is 700 or higher
    if income>3000: #if income is 3000 or more
        print("Approved for medium Loan limit") #prints the following
else: # else statement says the opposite 
    print("Not approved for medium loan limit") #prints the following 
if income >= 20000 and income <= 30000: # if income is between 2000-3000
    print("Approved for medium loan limit ") #prints the following
else: #else says the opposite
    print("Not approved for medium loan limit") # prints the following
if creditscore:600-699 #if credit score is between 600-699
if income>3000: #if income is above 3000
        
        print("Approved for medium loan limit with a higher rate") #prints the following
else: #says the opposite
    print("Not approved") # prints the following
if income<3000: #if below 3000
    print("Approved for low loan limit") # prints the following
else: #says the opposite
    print("not approved") #prints the following
    if creditscore<600: #if credit score is below 600
        print("Loan not approved") # prints the following




# Question 15: Tax Bracket Calculation

income = int(input("Annual Income: ")) #asks user their annual income
dependents = input("Have any Dependents?") # asks user if they have dependents

if income < 30000:   # if statement with outcome 
    if dependents: # also if dependents
        print("Tax Rate of 5%")
    else: print("Tax Rate of 7%") # prints else if no dependent

if income >= 30000 and income <= 70000:   # if statement with outcome
    if dependents: # also if dependents 
        print("Tax Rate of 10%")
    else: print("Tax Rate of 15%") # prints else if no dependent
if income > 70000:   # if statement with outcome
    print("Tax Rate of 20%")





