print("Welcome to Treasure Map!\nHere is your map:")
row1 = ['🟩', '🟩', '🟩']
row2 = ['🟩', '🟩', '🟩']
row3 = ['🟩', '🟩', '🟩']
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
mark = input("Which point will you like to mark?\nEnter 2 digits e.g: '12' for column 1, row 2: ")
col = int(mark[0]) - 1
row = int(mark[1]) - 1
map[row][col] = "X"
print("Your point has been marked!")
print(f"{row1}\n{row2}\n{row3}")