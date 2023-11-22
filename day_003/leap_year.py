print("Welcome to the leap year checker!")
year = int(input("Enter the year you want to check: "))
if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print(f"Year {year} is a leap year")
        else:
            print(f"Year {year} is not a leap year")
    else:
        print(f"Year {year} is a leap year")
else:
    print(f"Year {year} is not a leap year")