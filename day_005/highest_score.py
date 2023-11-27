scores = input("Input the scores of the students:\n").split()
high = 0
for score in scores:
    if int(score) > high:
        high = int(score)
print(f"The highest score in the class is: {high}")