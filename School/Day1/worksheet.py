
import random

#Worksheet - Variables

age = str(input("What is your age?: "))
print(f"I am {age} years old!")

first_name = input("Please enter your first name: ")

last_name = input("Pleas enter your last name: ")

full_name = first_name + " " + last_name

print(f"My first name is {first_name} and my last name is {last_name}, which means my full name is {full_name}!")

#temperature converter ------------------

fahrenheit = float(input("Whats your temperature in Fahrenheit: "))

celsius_calculation = (fahrenheit - 32) * 5.0/9.0

print(f"{fahrenheit} degrees Farhrenheit is {celsius_calculation} degrees Celsius")

#conditionals ---------------------------

#Driving Age --------------
legal_driving_age = 16

drivers_age = int(input("What is your age?: "))

years_to_wait = 16 - drivers_age

if drivers_age >= legal_driving_age:
    print("You are legally able to drive!")
else:
    print(f"You are not old enough to drive yet. You have {years_to_wait} years left! Come back then!")

#Random Colors and Numbers -

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

random_number()

#NFL Teams ------------------

team_name = input("Please type a Team name: ")

if team_name == "Bears":
    print("Quarterback much?")
elif team_name == "Vikings":
    print("Loud Noises!!!!")
elif team_name == "Lions":
    print("Lol! They bad!")
elif team_name == "Packers":
    print("Best team in the world! Actually, the universe")
else:
    print(f"Sorry, we dont recognize {team_name} as a real team. Pick a different team!")

