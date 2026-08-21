# FUNCTIONS --> reuseable block of code


def greet():
    print("Hello, Zeeshan")

greet()  # calling a function


# WITH PARAMETER

def call(name):
    print("Calling", name)

call("Zeeshan") # Calling Zeeshan
call("Hassan") # Calling Hassan
# this above is an example of reuseability 

# FUNCTIONS WITH RETURN VALUE

def sum(a,b):
    result=a+b
    return result

answer = sum( 6 , 4 )
print(answer)

