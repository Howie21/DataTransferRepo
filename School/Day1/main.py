
import random

# total_instructors = 8

# qualified_instructors = 5

# print(f"{qualified_instructors}/{total_instructors} instructors are qualified to teach C++")

# x = 300

# y = 200

# # Below, returns else statement even if one of the
# # if's return true

# def assignment_operators():
#     result = 0
#     if x == y:
#         print(f"{x} does equal {y}")
#     if x != y:
#         print(f"{x} does not equal {y}")
#     if x > y:
#         print(f"{x} is greater then {y}")
#     if x < y:
#         print(f"{y} is greater than {x}")
#     else:
#         print("I do not understand")

# # ----




# assignment_operators()

# -------------------------------------------------------


def random_number():
    number = random.randint(1, 11)
    print("Generating number between 1 and 10")
    if number <= 2:
        print("Your Number is 0 or 1 or 2!")
    elif number > 2 and number <= 5: 
        print("Your number is 3 or 4 or 5")
    elif number > 5 and number <= 8:
        print("Your number is 6 or 7 or 8")
    elif number == 9 or number == 10:
        print("Your number is 9 or 10")
    else:
        print("With your luck, you would get 11!")

#random_number()
