
# Single line comment
letter = 'P'                # A string could be a single character or a bunch of texts
print(letter)               # P
print(len(letter))          # 1
greeting = 'Hello, World!'  # String could be  a single or double quote,"Hello, World!"
print(greeting)             # Hello, World!
print(len(greeting))        # 13
sentence = "I hope you are enjoying python bootcamp challenge"
print(sentence)

# Multiline String
multiline_string = '''I am a teacher and enjoy teaching.
I didn't find anything as rewarding as empowering people.
That is why I created python bootcamp.'''
print(multiline_string)
# Another way of doing the same thing
multiline_string = """I am a teacher and enjoy teaching.
I didn't find anything as rewarding as empowering people.
That is why I created python bootcamp."""
print(multiline_string)

# String Concatenation
first_name = 'Ayoub'
last_name = 'Hamadouche'
space = ' '
full_name = first_name  +  space + last_name
print(full_name) # Ayoub Hamadouche
# Checking length of a string using len() builtin function
print(len(first_name))  # 8
print(len(last_name))   # 7
print(len(first_name) > len(last_name)) # True
print(len(full_name)) # 15

#### Unpacking characters 
language = 'Python'
a,b,c,d,e,f = language # unpacking sequence characters into variables
print(a) # P
print(b) # y
print(c) # t 
print(d) # h
print(e) # o
print(f) # n

# Accessing characters in strings by index
language = 'Python'
first_letter = language[0]
print(first_letter) # P
second_letter = language[1]
print(second_letter) # y
last_index = len(language) - 1
last_letter = language[last_index]
print(last_letter) # n

# If we want to start from right end we can use negative indexing. -1 is the last index
language = 'Python'
last_letter = language[-1]
print(last_letter) # n
second_last = language[-2]
print(second_last) # o

# Slicing

language = 'Python'
first_three = language[0:3] # starts at zero index and up to 3 but not include 3
last_three = language[3:6]
print(last_three) # hon
# Another way
last_three = language[-3:]
print(last_three)   # hon
last_three = language[3:]
print(last_three)   # hon

# Skipping character while splitting Python strings
language = 'Python'
pto = language[0:6:2] # 
print(pto) # pto

# Escape sequence
print('I hope every one enjoying the python challenge.\nDo you ?') # line break
print('Days\tTopics\tExercises')
print('Day 1\t3\t5')
print('Day 2\t3\t5')
print('Day 3\t3\t5')
print('Day 4\t3\t5')
print('This is a back slash  symbol (\\)') # To write a back slash
print('In every programming language it starts with \"Hello, World!\"')

## String Methods
# capitalize(): Converts the first character the string to Capital Letter

challenge = 'python bootcamp'
print(challenge.capitalize()) # 'Python bootcamp'

# count(): returns occurrences of substring in string, count(substring, start=.., end=..)

challenge = 'python bootcamp'
print(challenge.count('y')) # 3
print(challenge.count('y', 7, 14)) # 1
print(challenge.count('th')) # 2`

# endswith(): Checks if a string ends with a specified ending

challenge = 'python bootcamp'
print(challenge.endswith('on'))   # True
print(challenge.endswith('tion')) # False

# expandtabs(): Replaces tab character with spaces, default tab size is 8. It takes tab size argument

challenge = 'thirty\tdays\tof\tpython'
print(challenge.expandtabs())   # 'thirty  days    of      python'
print(challenge.expandtabs(10)) # 'thirty    days      of        python'

# find(): Returns the index of first occurrence of substring

challenge = 'python bootcamp'
print(challenge.find('y'))  # 5
print(challenge.find('th')) # 0

# format()	formats string into nicer output    
first_name = 'Ayoub'
last_name = 'Hamadouche'
job = 'teacher'
country = 'Algeria'
sentence = 'I am {} {}. I am a {}. I live in {}.'.format(first_name, last_name, job, country)
print(sentence) # I am Ayoub Hamadouche. I am a teacher. I live in Algeria.

radius = 10
pi = 3.14
area = pi # radius ## 2
result = 'The area of circle with {} is {}'.format(str(radius), str(area))
print(result) # The area of circle with 10 is 314.0

# index(): Returns the index of substring
challenge = 'python bootcamp'
print(challenge.find('y'))  # 5
print(challenge.find('th')) # 0

# isalnum(): Checks alphanumeric character

challenge = 'ThirtyDaysPython'
print(challenge.isalnum()) # True

challenge = '30DaysPython'
print(challenge.isalnum()) # True

challenge = 'python bootcamp'
print(challenge.isalnum()) # False

challenge = 'python bootcamp 2019'
print(challenge.isalnum()) # False

# isalpha(): Checks if all characters are alphabets

challenge = 'python bootcamp'
print(challenge.isalpha()) # True
num = '123'
print(num.isalpha())      # False

# isdecimal(): Checks Decimal Characters

challenge = 'python bootcamp'
print(challenge.find('y'))  # 5
print(challenge.find('th')) # 0

# isdigit(): Checks Digit Characters

challenge = 'Thirty'
print(challenge.isdigit()) # False
challenge = '30'
print(challenge.digit())   # True

# isdecimal():Checks decimal characters

num = '10'
print(num.isdecimal()) # True
num = '10.5'
print(num.isdecimal()) # False


# isidentifier():Checks for valid identifier means it check if a string is a valid variable name

challenge = '30DaysOfPython'
print(challenge.isidentifier()) # False, because it starts with a number
challenge = 'thirty_days_of_python'
print(challenge.isidentifier()) # True


# islower():Checks if all alphabets in a string are lowercase

challenge = 'python bootcamp'
print(challenge.islower()) # True
challenge = 'Python bootcamp'
print(challenge.islower()) # False

# isupper(): returns if all characters are uppercase characters

challenge = 'python bootcamp'
print(challenge.isupper()) #  False
challenge = 'PYTHON BOOTCAMP'
print(challenge.isupper()) # True


# isnumeric():Checks numeric characters

num = '10'
print(num.isnumeric())      # True
print('ten'.isnumeric())    # False

# join(): Returns a concatenated string

web_tech = ['HTML', 'CSS', 'JavaScript', 'React']
result = '#, '.join(web_tech)
print(result) # 'HTML# CSS# JavaScript# React'

# strip(): Removes both leading and trailing characters

challenge = ' python bootcamp '
print(challenge.strip('y')) # 5

# replace(): Replaces substring inside

challenge = 'python bootcamp'
print(challenge.replace('python', 'coding')) # 'coding bootcamp'

# split():Splits String from Left

challenge = 'python bootcamp'
print(challenge.split()) # ['python', 'bootcamp']

# title(): Returns a Title Cased String

challenge = 'python bootcamp'
print(challenge.title()) # Python Bootcamp

# swapcase(): Checks if String Starts with the Specified String

challenge = 'python bootcamp'
print(challenge.swapcase())   # PYTHON BOOTCAMP
challenge = 'Python Bootcamp'
print(challenge.swapcase())  # pYTHON bOOTCAMP

# startswith(): Checks if String Starts with the Specified String

challenge = 'python bootcamp'
print(challenge.startswith('python')) # True
challenge = 'Python Bootcamp'
print(challenge.startswith('python')) # False