


#REVERSE A STRING ------

def reverse_string(x):
    result = x[::-1]
    return result

#Capitalize a string ----

def capitalize_string_proper(string):
    result = string.capitalize()
    return result

def capitalize_each_word(string):
    result = string.title()
    return result

# print(capitalize_each_word("hello world!"))

#Compress String

def compress_string(input):
    result = ""
    l = len(input)
    if l == 0:
        return ""
    if l == 1:
        return input + "1"
    last = input[0]
    cnt = 1
    initial = 1
    while initial < l:
        if input[initial] == input[initial - 1]:
            cnt += 1
        else:
            result = result + input[initial - 1] + str(cnt)
            cnt = 1
        initial += 1
    result = result + input[initial - 1] + str(cnt)
    return result

#print(compress_string("ffffrrrreeeedddd"))

def check_palindrome(input):
    proper_input = input.lower()
    input_reversed = reverse_string(proper_input)
    if proper_input == input_reversed:
        return print("This is considered a Palindrome!")
    elif proper_input != input_reversed:
        return print("This is not a Palindrome, try again!")

test = check_palindrome("Yankee")
print(test)