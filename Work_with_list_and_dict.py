# import random
# twin_numbers = []
# odd_numbers = []

# def class_work(): 
#     trace = 0
#     while trace < 100:
#         trace += 1
#         num =  random.randint(1, 100)
#         if num % 2 == 0: 
#             twin_numbers.append(num)
#         else:
#             odd_numbers.append(num)
#     print(twin_numbers) 
#     print(odd_numbers)
#     print("Sum of elements in twin_numbers is :", sum(twin_numbers))
#     print("Sum of elements in odd_numbers is :", sum(odd_numbers))

     
# class_work()


# import random
# all_numbers = {'twin_numbers':[], 'odd_numbers':[]}


# def class_work(): 

#     trace = 0
#     while trace < 100:
#         trace += 1
#         num =  random.randint(1, 100)
#         if num % 2 == 0: 
#             all_numbers['twin_numbers'].append(num)
#         else:
#             all_numbers['odd_numbers'].append(num)
#     print(all_numbers) 
#     print("Length of elements in twin_numbers is :", len(all_numbers['twin_numbers']))
#     print("Length of elements in odd_numbers is :", len(all_numbers['odd_numbers']))
#     print("Sum of elements in twin_numbers is :", sum(all_numbers['twin_numbers']))
#     print("Sum of elements in odd_numbers is :", sum(all_numbers['odd_numbers']))


# class_work()


def probability():

    import random 

    random_number = format(random.uniform(1,3), ".3f")
    steps = 0
    while random_number != format(random.uniform(1,3), ".3f"): 
        steps += 1

    print(f"Final random probabily: {format(1/steps*100, '.3f')}%")

    # Statisticaly this calculation is not reliable, because each probability is random and every time is new.

probability()

