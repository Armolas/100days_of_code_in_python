print("Welcome to prime number checker!")
n = int(input("Enter the number you'd like to check: "))
def check_prime(number):
    prime = True
    if number < 3:
        return prime
    for i in range(2, number):
        if number % i == 0:
            prime = False
            break
    return prime
if check_prime(number=n) == True:
    print(f"{n} is a prime number")
else:
    print(f"{n} is not a prime number")
