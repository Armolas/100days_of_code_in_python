print("Welcome to paint calculator!")
height = int(input("What is the height of the wall in metres? "))
width = int(input("What is the width of the wall in metres? "))
def paint_calc(width, height):
    cans = round(width * height / 5)
    print(f"You'll need {cans} cans of paint")
paint_calc(width, height)
