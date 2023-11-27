heights = input("Input a list oof student heights:\n").split()
sum = 0
i = 0
for height in heights:
    sum += int(height)
    i += 1
average = round(sum / i)
print(f"The average student height is {average}")