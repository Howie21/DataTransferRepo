


#For Loops Task--------------------------------

# for x in range(5):
#     print("Hello")

# for y in range(11):
#     print(y)

# for numbx in range(11, 0, -1):
#     print(numbx)

# def print_specific():
#     user_input = int(input("enter a number: "))
#     for number in range(user_input):
#         print(f"{number}: devCodeCamp")

# #print_specific()

# football_team = "Packers"

# for character in football_team:
#     print(character)

# #FizzBuzz ChaLLenge-----------------------

# for number in range(100):
#     if number % 3 == 0 and number % 5 == 0:
#         print("Fizzbuzz")
#     elif number % 3 == 0:
#         print("Fizz")
#     elif number % 5 == 0:
#         print("Buzz")
#     else:
#         print(number)

#while loops ---------------------------------

X = 0

while X != 5:
    X += 1
    print("Hello world")



def check_password():
    user_input = ''
    counter = 0
    while user_input != "testpassword" and counter < 3:
        user_input = str(input("Please type your password"))
        if user_input != "testpassword":
            print(f"{user_input} is the wrong password, please try again: ")
            counter += 1
        elif user_input == "testpassword":
            print("User Validated")
            break

check_password()