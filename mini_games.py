

#
#
# first_number = int(raw_input('Enter the first number: '))
# second_number = int(raw_input('Enter the second number: '))
# operator = raw_input('Enter the operator: ')
#
# if operator == '+':
#     print(first_number + second_number)
#
# elif operator == '-':
#     print(first_number - second_number)
#
# elif operator == '*':
#     print(first_number * second_number)
#
# else:
#     print('Try another operator!')

#
# for i in range(1000):
#     if i % 10 == 0:
#         print(i)

for i in range(10000000):
    if i % 3 == 0 and i % 5 == 0:
        print('fizzbuzz')
    elif i % 3 == 0:
        print('fizz')
    elif i % 5 == 0:
        print('buzz')
    else:
        print(i)

Selection = input('What is your selection')
while (Selection != "1" && Selection != "2"):
    Selection = input("Invalid input. Try again!")
