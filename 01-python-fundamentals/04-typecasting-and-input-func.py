# TYPE-CASTING 

# there are two types of casting

# 1. IMPLICIT Casting ---> python automatically converts from one data type to another

math = 51
science = 50.55
total_marks = math + science
print(total_marks) # 101.55 auto converts

#-----------------------------------------------------------

# 2. EXPLICIT CASTING ---> we have to do casting manually 

history = 55.3
print(int(history)) # shows 55 integer type 

geography = "57" # type <str>
x = float(geography)
print(type(geography)) # here orignal is still <str> bcuz it creates a converted value & stores it in another variable
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

#-------------------------------------------------------------

# INPUT FUNCTION ---> input()

# used for taking input from user while program is running

age = input("enter your age : ")
print(age)
type(age) # type <str>

myAge = int(age) # convert <str> to <int> & stores it in myAge
print(myAge)
type(myAge) # now type <int>
