print("Welcome to the tip calculator!")
total_bill = float(input("How much is the total bill? $"))
tip_percent = int(input("What percentage of tip would you like to give? 10, 12, 15? "))
tip = tip_percent / 100 * total_bill
total_bill += tip
no_of_payers = int(input("How many people are spliting the bill? "))
each_pay = round(total_bill / no_of_payers, 2)
print("Each person should pay ${:.2f}.".format(each_pay))