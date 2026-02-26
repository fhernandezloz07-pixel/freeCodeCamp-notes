# Problem Set version 1
# Problem 1: hello World!
def hello_world(): 
    print("Hello world!")

hello_world() # Prints 'Hello world!'

# Problem 2: Today's Mood
def todays_mood():
    mood = "😎"
    print("Today's mood: " +  mood)

todays_mood()

# Problem 3: Lunch Menus
def print_menu(menu):
    print("Lunch menu to day is: " + menu)

menu = "🍕"
print_menu(menu) # Prints the menu item to console
# The variable listed between the () of a function definition is known as a parameter. 

# Problem 4: Sum of Two Integers
def sum(a, b): # here we are sort of declaring sum() to know what it will do for all cases
    return a + b
first = sum(13, 27) # use sum() to calculate the sum of 13 and 27
result = sum(first, first) # use sum() to double the calculated sum

print(result)# Print the result to the console

# Problem 5

