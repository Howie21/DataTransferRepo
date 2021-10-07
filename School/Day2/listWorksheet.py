
my_list = ["index0", "index1", "index2"]

colors = ["blue", "red", 'white', 'green', 'yellow']

def value1(list):
    print(list[0])

value1(my_list)

def check_for_color(list):
    for x in list:
        user_color_input = input("Please guess a color: ")
        if x == user_color_input:
            print("You have guessed a color")
            break
        else:
            print("That color is not in my list!")

check_for_color(colors)


numbers = [5, 20, 25, 50]

def is_it_evenLoop(list):
    sum = 0
    for x in list:
        sum += x
    return is_it_even(sum)


def is_it_even(list):
    if list % 2 == 0:
        return(f"{list} Is an even number")
    else:
        return(f"{list} is not even, ODD!! See what I did there?")

g = is_it_evenLoop(numbers)
print(g)

num_collection = [40, 400, 230, 5, 234, 543, 35, 212,]

def is_it_greater_then(list, number):
    for num in list:
        if number > num:
            print(f"{number} is greater than {num}")
        else:
            print(f"{number} is not greater than {num}")

try_me = is_it_greater_then(num_collection, 1)
print(try_me)