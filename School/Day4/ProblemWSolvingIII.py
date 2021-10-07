
import re

# 1.	Given an array of integers, return indices of the two numbers such that they 
# add up to a specific target. You may assume that each input would have exactly 
# one solution, and you may not use the same element twice.
# a.	Use Case:
# i.	Given numbers in an array: [5, 17, 77, 50] 
# ii.	Target: 55

list_for_number_one = [5, 17, 77, 50]

def does_list_provide_target_sum(target, list):
    new_list = []
    for number in list:
        for number2 in list:
            if number + number2 == target:
                return print(f"{number} + {number2} gave us {target}")
            elif number - number2 == target:
                return print(f"{number} - {number2} gave us {target}")
    else:
        return print("Nothing in the list gave us the target output")

# does_list_provide_target_sum(22, list_for_number_one)

# 2.Panlindrome
def reverse_string(x):
    result = x[::-1]
    return result

def check_palindrome(input):
    proper_input = input.lower()
    input_reversed = reverse_string(proper_input)
    if proper_input == input_reversed:
        return print("This is considered a Palindrome!")
    elif proper_input != input_reversed:
        return print("This is not a Palindrome, try again!")

# 3
list_of_numbers = [1, 5, 4, 3, 2, 6, 7, 8]
list_of_random_numbers = [1, 2, 3, 4, 5, 7]
    

def is_it_consecutive(list_name):
    list_name.sort()
    list_length = len(list_name)
    min_index = list_name[0]
    max_index = list_name[list_length - 1]
    range_list = list(range(min_index, (max_index + 1)))
    if list_name == range_list:
        print(f"{list_name} has a sequence!")
    else:
        print(f"{list_name} does not have a sequence!")

# is_it_consecutive(list_of_random_numbers)


#4

random_numbers = [-44, 77, 345, 23, 5, 6, 4, -6, -45, -74]
def seperate_numbers(list_name):
    postive_values = []
    negative_values = []
    for number in list_name:
        if number >= 0:
            postive_values.append(number)
        elif number < 0:
            negative_values.append(number)
    postive_values.sort()
    negative_values.sort()
    print(f"{postive_values} is your Positive Numbers")
    print(f"{negative_values} are your Negative Numbers")

#seperate_numbers(random_numbers)

#5

def highest_lowest(list_name):
    list_name.sort()
    lowest_value = list_name[0]
    highest_value = list_name[len(list_name) -1]
    print(f"Your list was {list_name}.")
    print(f"Your lowest value was: {lowest_value}. Your highest value was: {highest_value} ")
    
#highest_lowest(random_numbers)

#6 

def check_email():
    email = input("Type your email")   
    regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'
    if(re.search(regex,email)):   
        print("Valid Email")   
    else:   
        print("Invalid Email")

# check_email()


#7 
alphabet = 'abcdefghijklmnopqrstuvwxyz'

def code_translator(string):
    dictt = {'a':'1','b':'2','c':'3','d':'4','e':'5','f':'6','g':'7','h':'8',
    'i':'9','j':'10','k':'11','l':'12','m':'13','n':'14','o':'15','p':'16','q':'17',
    'r':'18','s':'19','t':'20','u':'21','v':'22','w':'23','x':'24','y':'25','z':'26'
    }
    translation = []
    new_text = string.lower()
    for dict_letter in new_text:
        for letter in dictt.keys():
            if letter == dict_letter:
                add = dictt[dict_letter]
                translation.append(add)
    return str(translation)

# g = code_translator("try me again")
# print(g)

#8

def crack_the_case():
    current_lock = "3893"
    target_lock = "5296"
    turns_dail= 0
    for number, number2 in zip(current_lock, target_lock):
            if number == number2:
                continue
            elif number > number2:
                turns = int(number) - int(number2)
                turns_dail = turns_dail + turns
            elif number < number2:
                turns = int(number2) - int(number)
                turns_dail = turns_dail + turns
                continue
    print(f"It took {turns_dail} turns to get {current_lock} to {target_lock}")

#crack_the_case()

#9
#Happy Numbers

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

# happy_check(19)

#10
#Recipricals

def reverse_string(x):
    result = str(x[::-1])
    return result

def recipricals(number):
    number_string = str(number)
    number_reversed = reverse_string(number_string)
    reversed_number = int(number_reversed)
    recip = float(1 / reversed_number)
    print(('{:6.5f}'.format(recip))+" " + "is your value")


# recipricals(17) 