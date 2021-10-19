
# TASK 1. Finds word and 150 symbols before and after the word. ------------------------------------------------
TEXT = 'fsfslskfdfsdfdfl d;dldksdkfkljdfkbjxjvvksjzdvdksdvkdvdkjvs vjfkfjvjdvkjdjjvkjvjdvld jdvjdvlsjdvjdvljdvljdsv ' \
       'jfvjjvfvdvjlddvkdlv vldvlvdvdksdvdlkvdkvdkl dlkdvldvkdvdlkFg glory! The dgjjlgjgjjgjrj gjrjgjjjldfjlhjldfjhf' \
       'hjfjlh word glory today vknvdvdvdkvdnvkdvdvdnsdvkndvknd vknsdvndvdkvdnvdvkvsndvndvdknvdnkvsnkdvndkvsknvnkdvn' \
       'kdvnsdnvdnvnsdvsndvndkvknsnvdnvsdnkvnkdvnkdsvnkdnvndvsnkdvnksnkdvnksdnvndvsndvnkdvndvnsnkvnk!' \
       ' eegge? Free glory continent.'
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


# TASK 2. Sorts numbers by the biggest first numbers. ---------------------------------------------------------
NUMBERS = [114, 2, 6, 23, 22, 6, 45, 659]
NUMBER_STR = []

for number in NUMBERS:
    NUMBER_STR.append(str(number))

NUMBER_STR = sorted(NUMBER_STR)
final_number = ''.join(reversed(NUMBER_STR))
print(final_number)
# -------------------------------------------------------------------------------------------------------------