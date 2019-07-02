def is_even(number):
    if number % 2 == 0:
        print(number, "is even.")
        return number
    else:
        print("Not even!")

while True:
    user = int(input("Put in a number."))
    is_even(user)
    exit()
