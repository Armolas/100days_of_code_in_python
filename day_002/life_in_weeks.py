days = 90 * 365
weeks = 90 * 52
months = 90 * 12
print("Welcome to Life in weeks\n---------------------")
print("Calculate your time left to live if you could live up to 90")
age = int(input("What is your current age?\n"))
days -= age * 365
weeks -= age * 52
months -= age * 12
print(f"You have {days}days, {weeks}weeks, and {months}months left if you could live up to 90")