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

my_function() # --> Calling the function to see the local variable in action


# GLOBAL VARIABLES :
# global variables are defined outside of any function and can be accessed from anywhere in the code including functions

myName = "Zeeshan"
def greet():
    print(myName)

greet()
print(myName)

x = 16

def show():
    print(x+1) # updates x by adding 1

show() # 17