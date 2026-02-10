'''#Task 1 (Mutable Default Argument – Function Bug)Task: Analyze given code where a mutable default argument causes unexpected behavior. Use AI to fix it.# Bug: Mutable default argumentdef add_item(item, items=None):  if items is None:    items = []  items.append(item)  return itemsprint(add_item(1))print(add_item(2))Expected Output: Corrected function avoids shared list bug.		
def add_item(item, items=None):
    if items is None:
        items = []
    items.append(item)
    return items
print(add_item(1))
print(add_item(2))'''

'''#  Task2: Analyze given code where floating-point comparison fails.     Use AI to correct with tolerance.
import math
def check_sum():
    return math.isclose(0.1 + 0.2, 0.3, rel_tol=1e-6)
print(check_sum())

#Task3: Analyze given code where recursion runs infinitely due to missing base case. Use AI to fix.
def countdown(n):
    if n <= 0:
        return
    print(n)
    countdown(n-1)
countdown(5)'''

'''#TASK4:Analyze given code where a missing dictionary key causes error. Use AI to fix it
def get_value():
    data = {"a": 1, "b": 2,}
    return data.get("c")
print(get_value())'''

'''#Task5: Analyze given code where loop never ends. Use AI to detect and fix it.
def loop_example():
    i = 0
    while i < 5:
        print(i)
        i += 1   # Increment i so the loop can end
loop_example()'''

'''#Task6: Analyze given code where tuple unpacking fails. Use AI to fix it.
a, b, c = (1, 2, 3)
print(a, b, c)'''

'''#Task7: Analyze given code where mixed indentation breaks execution. Use AI to fix it.
def func():
    x = 5
    y = 10
    return x+y
print (func())'''

'''#Task8: Analyze given code with incorrect import. Use AI to fix.
import math
print(math.sqrt(16))'''

'''#Task9: Analyze given code where a return inside a loop prevents full iteration. Use AI to fix it.
def total(numbers):
    for n in numbers:
        return n
print(total([1,2,3]))'''


'''#Task10: Analyze given code where a variable is used before being defined. Let AI detect and fix the error.
def calculate_area(length, width):
    return length * width
print(calculate_area(5, 10))'''

'''# Task11: Analyze given code where integers and strings are added incorrectly. Let AI detect and fix the error.
def add_values():
    return 5 + int("10")
print(add_values())'''

'''# Task12: Analyze code where a string is incorrectly added to a list.
def combine():
    return "Numbers: " + str([1, 2, 3])
print(combine())'''

'''#Task13: Detect and fix code where a string is multiplied by a float
def repeat_text():
    return "Hello" * 2
print(repeat_text())'''

'''#Task14: Analyze code where None is added to an integer.
def compute():
    value = 0
    return value + 10
print(compute())'''

#Task15: Fix code where user input is not converted properly.
'''def sum_two_numbers():
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))
    return a + b
print (sum_two_numbers())'''












