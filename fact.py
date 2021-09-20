
dict_data = {}


def factorial(num):
    result = 1
    if num in dict_data.keys():
        print(f'The factorial of {num} was calculated before. The value of the factorial is {dict_data[num]}'
              f' and saved in our DICT.')

    for i in range(1, num+1):
        result = result * i
        dict_data[i] = result
        last_key = sorted(dict_data.keys())[-1]

    print(f'The factorial of {num} is {result}.')
    print(f'The biggest calculated factorial is: {last_key}.')
    print(f'The value of the factorial is: {dict_data[last_key]}\n')


last_result = factorial(5)
last_result = factorial(4)
last_result = factorial(9)
last_result = factorial(3)


