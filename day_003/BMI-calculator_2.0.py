print("Welcome to the BMI Calculator!")
weight = int(input("Enter your weight in kg\n"))
height = input("Enter your height in m\n")
BMI = int(weight / (float(height) ** 2))
if BMI < 18.5:
    value = "Underweight"
elif BMI >= 18.5 and BMI <25:
    value = "Normal"
elif BMI >= 25 and BMI < 30:
    value = "Overweight"
elif BMI < 35:
    value = "Obese"
else:
    value = "Clinically Obese"
print(f"Your Body Mass Index is {BMI}")
print(f"According to World Health Organization, your BMI is {value}")
