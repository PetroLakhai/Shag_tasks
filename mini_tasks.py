
import collections
from datetime import timedelta

# TASK 1. Finds the bigger numbers than some number. -----------------------------------------------------------------
data = [1, 3, 5, 7, 9, 12]
number = 6


def find_bigger_numbers(data_list: list, number: int):
    list_of_bigger_numbers = [i for i in data_list if i > number]
    print(f'The bigger numbers than {number} is all in {list_of_bigger_numbers}.')


find_bigger_numbers(data, number)
# --------------------------------------------------------------------------------------------------------------------


# TASK 2. Finds intersection between two lists. ----------------------------------------------------------------------
list_1 = [1, 2, 4]
list_2 = [1, 2, 5]


def intersection_of_two_lists(list_1: list, list_2: list):
    intersection = set(list_1).intersection(list_2)
    print(f'Intersection of two abjects is {intersection}.')


intersection_of_two_lists(list_1, list_2)
# --------------------------------------------------------------------------------------------------------------------


# TASK 3. Convert seconds into usual time. ---------------------------------------------------------------------------
def convert_seconds_in_usual_time(seconds: int):
    usual_time = str(timedelta(seconds=seconds))
    print(f'{seconds} seconds in format hh.mm.ss. is: {usual_time}.')


convert_seconds_in_usual_time(12345)
# --------------------------------------------------------------------------------------------------------------------


# TASK 4. Finds the longest word and most frequent. ------------------------------------------------------------------
def find_longest_word_and_most_frequent(data_str: str):
    _dict = {}
    data_list = data_str.split()
    for word in data_list:
        _dict[len(word)] = word
    list_keys = _dict.keys()
    print(f'The longest word is: {max(list_keys)}')

    occurance = collections.Counter(data_list)
    _list = occurance.values()
    print(f'The most common word is: {max(_list)}')


data_str = 'sss rrrr ss sss'
find_longest_word_and_most_frequent(data_str)
# --------------------------------------------------------------------------------------------------------------------
