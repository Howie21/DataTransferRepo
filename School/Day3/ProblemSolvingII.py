
import math

#Prime Number


def primeCheck(x):
    sta = 1
    for i in range(2,int(math.sqrt(x))+1):
        if(x % i == 0):
            sta = 0
            print("Not Prime")
            break
        elif(sta==1):
            print("Prime")
        return sta


#Fibonacci

def print_single_integer(list):
    for number in list:
        print(number)

def fibonacci(x, y):
    start = 0
    number = 0
    num_list = [start, x]
    while num_list[-1] < y:
            number = num_list[-1] + num_list[-2]
            num_list.append(number)
    print_single_integer(num_list)

fibonacci(1, 200)

def fibonacci_with_input():
    x = int(input("Where do you want the Fibonacci to start?: "))
    y = int(input("Where do you want the Fibonacci to end?: "))
    start = 0
    number = 0
    num_list = [start, x]
    while number < y:
            number = num_list[-1] + num_list[-2]
            if number > y:
                break
            else:
                num_list.append(number)
    print_single_integer(num_list)

fibonacci_with_input()
