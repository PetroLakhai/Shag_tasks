
import collections
from datetime import timedelta

# TASK_1. Finds the bigger numbers than some number. -----------------------------------------------------------
data = [1, 3, 5, 7, 9, 12]
number = 6


def find_bigger_numbers(data_list: list, number: int):  # TASK_1. Finds the bigger numbers than some number.
    list_of_bigger_numbers = [i for i in data_list if i > number]
    print(f'The bigger numbers than {number} is all in {list_of_bigger_numbers}.')


find_bigger_numbers(data, number)
# --------------------------------------------------------------------------------------------------------------

# TASK_2. Finds intersection between two lists. ----------------------------------------------------------------
list_1 = [1, 2, 4]
list_2 = [1, 2, 5]


def intersection_of_two_lists(list_1: list, list_2: list):  # TASK_2. Finds intersection between two lists.
    intersection = set(list_1).intersection(list_2)
    print(f'Intersection of two abjects is {intersection}.')


intersection_of_two_lists(list_1, list_2)
# --------------------------------------------------------------------------------------------------------------


# TASK 3. Convert seconds into usual time. ---------------------------------------------------------------------
def convert_seconds_in_usual_time(seconds: int):  # TASK 3. Convert seconds into usual time.
    usual_time = str(timedelta(seconds=seconds))
    print(f'{seconds} seconds in format hh.mm.ss. is: {usual_time}.')


convert_seconds_in_usual_time(12345)
# --------------------------------------------------------------------------------------------------------------


# TASK 4. Finds the longest word and most frequent. ------------------------------------------------------------
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
# --------------------------------------------------------------------------------------------------------------


# TASK 5. Finds word and 150 symbols before and after the word. ------------------------------------------------
TEXT = 'Fg glory! The dgjjlgjgjjgjrj gjrjgjrjjldfjlhjldfjhfhjfjlh word glory today vknvdvdvdkvdnvkdvdvdnsdvkndvkndvknsdvndvdkvdnvdvkvsndvndvdknvdnkvsnkdvndkvsknvnkdvnkdvnsdnvdnvnsdvsndvndkvknsnvdnvsdnkvnkdvnkdsvnkdnvndvsnkdvnksnkdvnksdnvndvsndvnkdvndvnsnkvnk! eegge? Best glory continent.'
WORD = 'glory'


def find_word(TEXT: str, WORD: str):
    list_of_sentences = []
    sentences = TEXT.split('.')

    for one_sentence in sentences:
        words = one_sentence.split()

        if WORD in words:
            text_before = one_sentence.partition(WORD)[0]
            text_after = one_sentence.partition(WORD)[2]

            if len(text_before) >= 150:
                text_before = f'... {text_before[-149:]}'
            elif len(text_after) >= 150:
                text_after = f'{text_after[:149] } ...'
            sentence_with_word = f'{text_before}{WORD}{text_after}'
            list_of_sentences.append(sentence_with_word)
    print(list_of_sentences)


find_word(TEXT, WORD)
# -------------------------------------------------------------------------------------------------------------


# TASK 6. Sorts numbers by the biggest first numbers. ---------------------------------------------------------
NUMBERS = [114, 2, 6, 23, 22, 6, 45, 659]
NUMBER_STR = []


for number in NUMBERS:
    NUMBER_STR.append(str(number))

NUMBER_STR = sorted(NUMBER_STR)
final_number = ''.join(reversed(NUMBER_STR))
print(final_number)
# -------------------------------------------------------------------------------------------------------------