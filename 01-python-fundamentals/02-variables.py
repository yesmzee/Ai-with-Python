# VARIABLES :
# variables are memory locations for our data

# RULES FOR DEFINING A VARIABLE :
# start with letter or underscore, not with numbers
# variables names can't have spaces in between them 
# keywords or reserved words can not be used as variable name
# use snakecase-->lower case but with underscore (total_amount ) or 
# use camelcase-->without spaces or underscore (totalAmount) but second word's first alphabet should be capital

# there are different types of variables in python


# this is an integer variable ( all +ive & -ive ) values

age = 23

# this is a float variable ( all +ive & -ive ) values

score = 95.5
print("Age:", age, "and Score:", score)

# type() function is used to check the data-type of a variable

print("data type of age:", type(age))
print("data type of score:", type(score))

# print function can also perform operations with variables

print( score + 5)


# print function can also perform string concatenation using the + operator

name = "Zeeshan"
last_name = "Ali"
print("Hello, " + name + last_name + " ! ")

# print function can also perform operations on variables

print("Next year, my age will be", age + 1, "years old.")


# this is a boolean variable
# boolean has only two values true or false

is_passed = True
print(is_passed)
print(type(is_passed))