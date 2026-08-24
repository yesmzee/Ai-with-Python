# VARIABLES SCOPE IN PYTHON :
# means that where we can use a variable in our code.

# # LOCAL  VARIABLES :
# local variables are defined inside a function and can only be accessed within that function.
# gets deleted when function stops running.

def greet():
    myName= "Zeeshan"
    print(myName)

greet() # calling function for local variable

def my_function():
    local_variable = "I am a local variable"
    print(local_variable)

# Calling the function to see the local variable in action
my_function()

# GLOBAL VARIABLES :
# global variables are defined outside of any function and can be accessed from anywhere in the code.

global_variable = "I am a global variable"
print(global_variable)

# so , if we try to access the local variable outside of its function, it will result in an error.
# print(local_variable)  # This will raise a NameError
