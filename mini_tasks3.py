
import re

# TASK 1. Calculates the sum of generated numbers. -------------------------------------------------------------------
def finds_sum(n, f_n):
    result = 0
    for number in range(n+1):
        if number > 0:
            result += int((str(f_n) * number))
    print(result)


finds_sum(3, 1)
# --------------------------------------------------------------------------------------------------------------------


# TASK 2. Finds difference between two lists. ------------------------------------------------------------------------
list1 = [1,3,4]
list2 = [2,4,5]


def difference_in_two_lists(list1: list, list2: list):
    all_elements = list(set(list1 + list2))
    intersection = set(list1).intersection(list2)
    for element in intersection:
        if element in all_elements:
            all_elements.remove(element)
    print(all_elements)


difference_in_two_lists(list1, list2)
# --------------------------------------------------------------------------------------------------------------------


# TASK 3. Finds sum of all numbers in the string.
string = "!1a2;b3c?vdvkdvdvddkd2"


def sum_of_string_numbers(string: str):
    number_list = re.sub('[^0-9]',',', string).split(',')
    sum_of_numbers = 0
    for object in number_list:
        if len(object) > 0:
            sum_of_numbers += int(object)
    print(f'Sum of all numbers in the string is {sum_of_numbers}.')


sum_of_string_numbers(string)
# --------------------------------------------------------------------------------------------------------------------


# TASK 4. Finds keys of three biggest values in dict.
_dict = {'1key':123, '2key':9785, '3key': 560, '4key':234, '5key': 3451}


def three_biggest_key(data: dict):
    dict_values = [value for value in _dict.values()]
    dict_values.sort()
    print(dict_values[-3:])
    for value in dict_values[-3:]:
        for key2, value2 in data.items():
            if value == value2:
                print(key2)


three_biggest_key(_dict)
# --------------------------------------------------------------------------------------------------------------------

# TASK 5. Finds factorial of number and check if the factorial was calculated before. --------------------------------
DICT_DATA = {}


def factorial(num):
    result = 1
    if num in DICT_DATA.keys():
        print(f'The factorial of {num} was calculated before. The value of the factorial is {DICT_DATA[num]}'
              f' and saved in our DICT.')

    for i in range(1, num+1):
        result = result * i
        DICT_DATA[i] = result
        last_key = sorted(DICT_DATA.keys())[-1]

    print(f'The factorial of {num} is {result}.')
    print(f'The biggest calculated factorial is: {last_key}.')
    print(f'The value of the factorial is: {DICT_DATA[last_key]}\n')

factorial(3)
# --------------------------------------------------------------------------------------------------------------------