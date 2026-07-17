import math

#Print information required for user to make a choice
print("Investment - to calculate the amount of interest you'll earn on your investment.")
print("Bond       - to calculate the amount you'll have to pay on a home loan.")

#Ask user to choose between the two options, Investment or Bond
#Make saved input lowercase
#If neither Investment or Bond are entered print an error message and explain why the error message has occured
choice = input("""Enter either "Investment" or "Bond" from the menu above to proceed: """).lower()


if choice == "investment":
    investment_deposit = int(input("How much money are you depositing: "))
    investment_rate = int(input("""The interest rate (just the number): """))
    investment_years = int(input("How many years do you plan on investing for: "))
    interest = input("""Do you want "simple" or "compound" interest: """).lower()

    if interest == "simple":
        simple_answer = investment_deposit * (1 + (investment_rate/100)*investment_years)
        print(simple_answer)

    elif interest == "compound":
        compound_answer = investment_deposit * math.pow((1+(investment_rate/100)),investment_years)
        print(compound_answer)
elif choice == "bond":
    house_value = int(input("The present value of the house: "))
    bond_rate = int(input("""The interest rate (just the number): """))
    bond_months = int(input("The number of months that you plan to take to repay the bond: "))
    bond_repayment = ((bond_rate/100/12) * house_value)/(1-(1+(bond_rate/100/12))**(-bond_months))
    print(bond_repayment)
else:
    print("""ERROR - neither "Investment" or "Bond" were input or were input correctly""")