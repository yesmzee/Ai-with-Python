
# Following are practice codes from files 91-intro.py to 05-operators.py


# SIMPLE CALCULATOR PROJECT from 01-05 practice files

num1 = float(input("Enter first number : "))
num2 = float(input("Enter second number : "))

print("Addition of the numbers is :", num1 + num2)
print("Subtraction of the numbers is :", num1 - num2)
print("Multiplication of the numbers is :", num1 * num2)
print("Division of the numbers is :", num1 / num2)


# BASIC INFORMATION SYSTEM

person = {
    "Name": input("Name"),
    "Age": int(input("Age")),
    "Courses": input("Python,AI,Git"),
}
print(person)


# BILL CALCULATOR

price = float(input("Enter the price : "))
quantity = float(input("Enter the quatity"))

print("Total Price is RS:",price * quantity)


# UNIT CONVETER km --> m

km = float(input("Enter the distance in km :"))
meters = km * 1000
print("Distance in meters (m) is :",meters)

