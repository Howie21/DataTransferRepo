


list1 = [23, 50, 24, 67, 34, 2, 6]

def average_of_list(list_name):
    average = sum(list_name) / len(list_name)
    return average 


def create_less_then_average_list(list_name):
    less_than_average = []
    average = average_of_list(list_name)
    for number in list_name:
        if number < average:
            less_than_average.append(number)
    less_than_average.sort()
    return less_than_average

g = create_less_then_average_list(list1)
print(g)

def get_list_length(list_name):
    result = len(list_name)
    return result

def identify_number_at_index(list_name, index_number):
    list_length = get_list_length(list_name)
    if (index_number < list_length):
        num = list_name[index_number]
        return num
    else:
        return print(f"No Value at this index. The list named, is only {list_length} index's long. Try a number before that.")

print(identify_number_at_index(list1, 6))

list2 = [2, 3, 4, 4, 4, 5, 6, 7, 3, 1]

def most_frequent_value(list_name):
    counter = 0
    num = list_name[0]
     
    for number in list_name:
        curr_number = list_name.count(number)
        if(curr_number > counter):
            counter = curr_number
            num = number
    return num

print(most_frequent_value(list2))

name_list1 = ["Mike", "David", "Nevin"]
name_list2 = ["Brett", "Mike", "Charles"]

def find_matches_in_list(list1, list2):
    matching_names_list = []
    for string in list1:
        for string2 in list2:
            if string == string2:
                matching_names_list.append(string)
    return matching_names_list

matching = find_matches_in_list(name_list1, name_list2)
print(matching)

# example_list = []
# for name in name_list1:
#     for other_name in name_list2:
#         if name == other_name:
#             example_list.append(name)

# print(example_list)