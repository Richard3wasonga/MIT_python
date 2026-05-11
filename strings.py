# input & output
# using f-string

# name = input("How are you ")
# age = input("Enter your age ")

# print(f"Hello your name is {name}, and you are {age} years old") # string formatting

# first_name = 'Bob'
# last_name = 'Oyier'

# sentence = 'my name is {} {}'.format(first_name, last_name)
# print(sentence)

# Benefit of f-string is we can run method directly within the f-string
# sentence = f'my name is {first_name} {last_name}'
# print(sentence)

# person = {'name': 'Jenn', 'age': 23}

# sentence = 'My name is {} and I am {} years old'.format(person['name'], person['age'])

# print(sentence)

# you want to use double quotes on the outer string so as not terminate it early while acessing the values from the dictionary
# sentence = f"My name is {person['name']} and I am {person['age']} years old"

# print(sentence)

#Calculation

# Calculation = f'4 times 11 is equal to {4 * 11}'

# print(Calculation)


# for n in range(1, 11):
#     sentence = f'The value is {n:02}'
#     print(sentence)


# precision
# pi = 3.14159265

# sentence = f'Pi is equal to {pi:.4f}'
# print(sentence)

from datetime import datetime

birthday = datetime(1990, 1, 1)

sentence = f'Jenn has a birthday on {birthday:%B %d, %Y}'
print(sentence)