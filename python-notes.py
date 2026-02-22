# Objective 1:
# this is a comment in python, using hashtag

print("Python is Working!")
variable_name_example = 2 # instead of camel case, use snake case!

# Rules to Remember:
    # Variable names can only start with a letter or an underscore (_), not a number.
    # Variable names can only contain alphanumeric characters (a-z, A-Z, 0-9) and underscores (_).
    # Variable names are case-sensitive — age, Age, and AGE are all considered unique.
    # Variable names cannot be one of Python's reserved keywords such as if, class, or def.

print('My favorite colors are', 'blue', 'green', 'red')
#Output: My favorite colors are blue greeen red
# python automatically adds spaces between each item when you separate w commas

# unlike other porgramming languages python doesn't need data types like int or char
name = 'Jhon Doe' # Python knows this is a string
age = 25 # Python knows this is an integer

# What does compiling mean? Compiling means the computer checks your code in advance and prepares to run it. 
    # languages that copile can catch type errors before the program even starts. 
# Python does not compile. In python, type errors can real themselves during execution, then the program is actually running.

# Common Data types in Python 

# Integer: A whole number without decimals, can be positive or negative
my_integer_var = 10
print('Integer:', my_integer_var) # Integer: 10

# Float: A umber with decimal points, can be positive or negative
my_float_var = 4.50
print('Float:', my_float_var) #Float: 4.5

# String: A sequence of character enclosed in a single or double quotation marks like 'Hello World!'
my_string_var = 'hello'
print('String:', my_string_var) # String: hello

# Boolean: A true or false type, written as True or False
my_boolean_var = True
print('Boolean:', my_boolean_var) # Boolean: True

# Set: An unordered Collection of Unique elements, like {4, 2, 0}
my_set_var = {7, 5, 8}
print('Set:', my_set_var) # Set: {7, 5, 8}

# Dictionary: A collection of key-value pairs enlosed in curly braces, like {'name': 'Jhon Doe', 'age': 28}
my_dictionary_var = {'name': 'Alice', 'age': 25}
print('Dictionary:', my_dictionary_var) # Dictionary: {'name': 'Alice', 'age': 25}

# Tuple: An immutable ordered collection, ecosed in brackets, like (7, 8, 4)
my_tuple_var = (7, 5, 8)
print('Tuple:', my_tuple_var) # Tulple: (7, 5, 8)

# Range: A sequence of numbers, often used in loops, for example, range(5)
my_range_var = range(5)
print('Range:', my_range_var) # Range: range(0, 5)

# List: An ordered collectuon of elements that supports different data types.
my_list = [22, 'Hello word', 3.14, True]
print(my_list) # [22, 'Hello World', 3.14, True]

# None: A special value that represents the absence of a value.
my_none_var = None
print('None:', my_none_var) #None: None

# To get the data type of a variable, you can use the type() function:
my_var_1 = 'Hello world'
print(type(my_var_1)) # <class 'str'>
my_var_2 = 21
print(type(my_var_2)) # <class 'int'>
# Examples using the previous data types
print(type(my_integer_var))  # <class 'int'>
print(type(my_float_var))  # <class 'float'>
print(type(my_string_var))  # <class 'str'>
print(type(my_boolean_var))  # <class 'bool'>
print(type(my_set_var))  # <class 'set'>
print(type(my_dictionary_var))  # <class 'dict'>
print(type(my_tuple_var))  # <class 'tuple'>
print(type(my_range_var))  # <class 'range'>
print(type(my_list)) # <class 'list'>
print(type(my_none_var))  # <class 'NoneType'>

# The built-in isinstance() function lets you check if a variable matches a specific data type. 
# it takes in and object and the type you want to ckeck it against, then returns a boolean. 
isinstance('Hello world', str) # True
isinstance(True, bool) # True
isinstance(42, int) # True
isinstance('Jhon Doe', int) # False

# Objective 2:
# What are strings and what is string Immutability?
# A string is a sequence of characters surrounded by either single or double quotation marks. You can use either or:
my_str_1 = 'Hello'
my_str_2 = "World"

# If you need a multi-line string, you can use tripple double quotes or single quotes:
my_str_3 = """Multiline
String"""
my_str_4 = '''Another
multiline-String'''
print(my_str_3)
print(my_str_4)

# If your coding a string and it contains either single or double quotation marks, use the opposite of the ones inside the string to wrapt the string in: 
msg = "It's a sunny day" # Notice how the word (It's) has a single quotation so I put double quotation to wrap the string. 
quote = 'She said, "Hello World"' # Notice how ("Hello World") has double quotation so I put single quotation to wrap the string. 

# Another way to express a string using both single and double quotations is to implement \. With this method you can use either single or double quotations to wrap the string:
msg = 'It\'s a sunny day' # Notice how I use single quotation marks in the same string but for different purposes
quote = "She said, \"Hello!\"" # Notice how I use double quotation maks in the same string but for different purposes

# What if you need to check if a string has one or more characters? the in operator, whihc returns a boolean that specifies whether the character(s) exist in the string or not:
my_str = 'Hello World'
print('Hello' in my_str) # True
print('hey' in my_str) # False
print('hi' in my_str) # False
print('e' in my_str) # True
print('f' in my_str) # False

# How can you get the length of a string and work with the individual characters in a string? This is called indexing, and you can use the built-in len() function: 
my_str = 'Hello World'
print(len(my_str)) # 11, notice how the space is also acounted for in length

#index: the position of a character in a string. The index starts at 0, cunting the very first character in the string at index 0. 
# To access a character by its index, you use square brackets [] with the index of the character you wna tto accesss inside: 
my_str = "Hello World"
print(my_str[0]) # H
print(my_str[6]) # w
#Negatie indexing is also allowed, so you can get the last character of any string with -1, the second-to-last character with -2, and so on: 
my_str = 'Hello World'
print(my_str[-1]) # d
print(my_str[-2]) # l

# Grouping Data types: In python ALL data gets treated as objects, and some objects are mutable while others are immutable. Strings are immutable data types in python, meaning you can reassign a different string to a varibale 
    # Immutable Data Types: Can't be modified or altered once they are declared. You can poin ttheir variables at something new, called reassignment, but you can't change the original object by adding, removing, or replacing any of it's elements
# Example with other languages include (primitive data type: simple and immutable. They cannot be changed or declared), (Refrence Types: Can hold multiple values and are either mutable or immutable)
greetings = 'hi'
greetings = 'hello'
print(greetings) # hello
# Direct modification of a string isn't allowed
greetings = 'hi'
# greetings[0] = 'H' ERROR!!

# What are String Concatenations and String Interpolation?
# String Concatenation: In python you can compine multiple strings together with the + operator. 
my_str_1 = 'Hello'
my_str_2 = "World"
str_plus_str = my_str_1 + ' ' + my_str_2
print(str_plus_str) # Hello World
    # You canno't concatonate strings with numbers, we can only concatonate sttring with string
name = 'Jhon Doe'
age = 26
# name_and_age = name + age
# print(name_and_age) ERROR!
    # To allow the concatonation of a string and another data type, first turn the other data type into a string using the built-in str()
name_and_age = name + str(age)
print(name_and_age) # Jhon Doe26
    # Another way is tp use the argunemnted assignment operator for concatonation represented by +=, this performs both concatonation and assignment in one step:
name_and_age = name # start with the name
name_and_age += str(age) # append the age as string
print(name_and_age) # Jhon Doe26

# String Interpolation: The process of inserting variables and exporessions into a string.
# F-strings: Category of string in python (formatted string literals), which allows you to handgle interpolation with a compct and readable syntax
    # Starts with f before the quotes, and allows you to embed variables or expressions iside replacement fields indicated by {}
name_and_age = f'My name is {name} and I am {age} years old'
print(name_and_age) # My name is Jhon Doe and I am 26 years old

num1 = 5
num2 = 10
print(f'The sum of {num1} and {num2} is {num1 + num2}') # The sum of 5 and 10 is 15

# Objective 3