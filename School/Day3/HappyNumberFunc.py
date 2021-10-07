


#Happy Number


def happy_check(x):
    number = 0
    if len(str(x)) == 1:
        number = x ** 2
    else:
        number = x
    total = 0
    while number != 1:
        for index in str(number):
            total += int(index) ** 2
        number = total
        total = 0
        if number != 1 and len(str(number)) == 1:
            print("Not a Happy Number")
        elif number == 1:
            print("Your number is the happy type!")
        elif number == x:
            return

happy_check(19)

# 1. Identify the input
# 2. Split input
# 3. square numbers
# 
# 4. get sum.
