# OPERATORS IN PYTHON
# There are two types of operators in Python:

# Unary  Operators ---> These operators operate on a single operand
# Binary Operators ---> These operators operate on two operands

# 1. ARITHMETIC or MATHEMATICAL OPERATORS

print(5 + 3)  # addition
print(9 - 4)  # subtraction
print(3 * 9)  # multiply
print(3 / 9)  # divide
print(17.6 // 3)  # floor divide --> removes the decimal part

# floor divides but answer is <int> type if both operands are <int>
# if one of them is <float> result is <float> and only .0 in result not more than .0

print(10 % 3)  # remainder (modulus)
print(2**4)  # exponent (power)


# 2. COMPARISON or RELATIONAL OPERATORS --> always produces a <boolean> result true or false

print(5 == 4)  # equal to
print(7 != 3)  # not equal to
print(10 > 2)  # greater than
print(4 < 1)  # less than
print(10 >= 8)  # greater than or equal to
print(13 <= 12)  # less than or equal to


# 3. LOGICAL or BOOLEAN OPERATORS --> used to combine or reverse conditions

# AND --> for True result both conditions must be true

print(True and True)  # True
print(True and False)  # False
print(False and True)  # False
print(False and False)  # False
age = 20
print(age >= 18 and age <= 30)  # true result


# OR --> for True result only one condition must be true

print(True or True)  # True
print(True or False)  # True
print(False or True)  # True
print(False or False)  # False
age = 16
print(age < 18 or age > 60)  # true result


# NOT --> reverse the boolean value

print(not True)  # false result
print(not False)  # true result
is_raining = False
print(not is_raining)  # true result


# 4. ASSIGNMENT OPERATORS or COMPOUND ASSIGNMENT OPERATORS --> used to assign or modify values to variables

x = 10
x += 5  # x = x + 5
x -= 3  # x = x - 3
x *= 2  # x = x * 2
x /= 4  # x = x / 4
x //= 2  # x = x // 2
x %= 3  # x = x % 3
x **= 2  # x = x ** 2
print(x)  # final value of x


# 5. BITWISE OPERATORS --> works on the individual bits (0s and 1s) of integer numbers.

#AND (&) --> 1 if both bits are 1 else 0
# 5 --> 101
# 3 --> 011
print(5 & 3)  # bitwise AND

# OR (|) --> 1 if any of the bits is 1 else 0
# 5 --> 101
# 3 --> 011
print(5 | 3)  # bitwise OR

# XOR (^) --> 1 if both bits are different else 0
# 5 --> 101
# 3 --> 011
print(5 ^ 3)  # bitwise XOR

# NOT (~) --> 1's complement of the number (flips the bits)
# 5 --> 101
print(~5)  # bitwise NOT
