# type-casting 
# there are two types of casting

# 1. Implicit Casting ---> python auto converts from one data type to another

math = 51
science = 50.55
total_marks = math + science
print(total_marks) # 101.55 auto converts

#-----------------------------------------------------------

# 2. Explicit Casting ---> we have to do casting manually 

history = 55.3
print(int(history)) # shows 55 integer no. 

geography = "57" # <str>
x = float(geography)
print(type(geography)) # here orignal x is still <str> bcuz it creates a converted value 
print(type(x))         # here the converted value is in x and now is <float>

#-----------------------------------------------------------

# CONVERSIONS THAT ARE NOT POSSIBLE

# String --> Integer (if string is not a valid number)
# "hello" --> int

# String --> Float (if string is not a valid number)
# "hello" --> float

# Complex --> Integer
# 5 + 2j --> int

# Complex --> Float
# 5 + 2j --> float

# List --> Integer
# [1, 2, 3] --> int

# List --> Float
# [1, 2, 3] --> float

# Dictionary --> Integer
# {"a": 1} --> int

# Dictionary --> Float
# {"a": 1} --> float

#-------------------------------------------------

# INPUT FUNCTION ---> input()
# used for taking input from user while program is running

age = input("enter your age : ")
print(age)
type(age) # its <str>

myAge = int(age) # convert <str> to <int> & stores it in myAge
print(myAge)
type(myAge) # now its <int>
