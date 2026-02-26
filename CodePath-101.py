# Problem Set version 1
# Problem 1: hello World!
def hello_world(): 
    print("Hello world!")

hello_world() # Prints 'Hello world!'

print("--------------------------------------------------------------------")
# Problem 2: Today's Mood
def todays_mood():
    mood = "😎"
    print("Today's mood: " +  mood)

todays_mood()

print("--------------------------------------------------------------------")
# Problem 3: Lunch Menus
def print_menu(menu):
    print("Lunch menu to day is: " + menu)

menu = "🍕"
print_menu(menu) # Prints the menu item to console
# The variable listed between the () of a function definition is known as a parameter. 

print("--------------------------------------------------------------------")
# Problem 4: Sum of Two Integers
def sum(a, b): # here we are sort of declaring sum() to know what it will do for all cases
    return a + b
num_sum = sum(13, 27) # use sum() to calculate the sum of 13 and 27
result_sum = sum(num_sum, num_sum) # use sum() to double the calculated sum

print(result_sum)# Print the result to the console

print("--------------------------------------------------------------------")
# Problem 5: Product of two integers
def product(a, b): # Writing the function Product() that returns the product of two integers a and b
    return a * b
result_product = product(22, 7) # Example product of 22 times 7
print(result_product) # Printing the product of two numbers a and b to console

print("--------------------------------------------------------------------")
# Problem 6: Classify Age
def classify_age(age): 
    if age < 18:
       return "child"
    elif age >= 18:
        return "adult"

output = classify_age(18)
print(output)
output = classify_age(7)
print(output)
output = classify_age(50)
print(output)
print("-----------------")
    # Another way to do this with print statements inside the if elif statement: 
def classify_age(age): 
    if age < 18:
       print("child")
    elif age >= 18:
        print("adult")

classify_age(18)
classify_age(7)
classify_age(50)

print("--------------------------------------------------------------------")
# Problem 7: What time is it? 
def what_time_is_it(hour): # hour is the parameter of the function what_time_is_it
    if hour == 2:

        return "taco time 🌮"
    elif hour == 12:
        return "peanut butter jelly time 🥪"
    else: 
        return "nap time 😴" 

time = what_time_is_it(2)
print(time)
time = what_time_is_it(7)
print(time)
time = what_time_is_it(12)
print(time)

print("--------------------------------------------------------------------")
# Problem 8: Blackjack
def blackjack(score): 
    if score == 21:
        print("Blackjack!")
    elif score > 21: 
        print("Bust!")
    elif score >= 17 and score <= 21: # in python use the built-in and for connecting inside the if statement!
        print("Nice hand!")
    elif score < 17:
        print("Hit me!")

blackjack(21)
blackjack(24)
blackjack(19)
blackjack(10)

print("--------------------------------------------------------------------")
# Problem 9: First Item
def get_first(lst): 
    if lst == []:  # add the empty condition first before you check for the first item in the list 
        return None
    return lst[0]

print(get_first([3,1,6,7,5]))

# Problem 10: Last Item 
def get_last(lst): 
    if lst == []:
        return None
    return lst[-1]

print(get_last([3,1,6,7,5])) # printing the fuction properties we just coded for the specified list!

print("--------------------------------------------------------------------")
# Problem 11: Counter
# write a function counter() that uses the built-in range function to: 
def counter(stop):
    # print numbers between 1 and a given stop value (inclusive)
    for i in range(1, stop + 1): # The plus includes the last indez instead of excluding it!
        print(i) #???
counter(7) # Example code 

print("--------------------------------------------------------------------")
# Problem 12: Sum of 1 to 10
# Accumulator variable is a variable that keeps running total while you program loops, so it grows step-by-step
def sum_ten():
    accumulator_sum = 0 # start the accumulator at 0
    for i in range(1, 11): # sum from 1 to 11
        accumulator_sum += i # add the current number to the accumulator
    return accumulator_sum 
print(sum_ten()) # Print your code!

# 




