# LOOPING DATA STRUCTURES

# STRINGS

my_name = "ZeeshaN"
for l in my_name:
    print(l)

# CHARACTER REPEATING :

x = 0
text = input("Enter a text: ")
charac = input("enter character to know how many times a character is repeated :")
for m in text:
    if m == charac:
        x += 1
print(charac, "reapeated", x, "times")

# REVERSING STRING :

textt = input("enter text to reverse ")  # e.g : "Zeeshan"
reverse = ""
for c in textt:
    reverse = (
        c + reverse
    )  # first reverse = "" + "Z" = "Z" , second reverse = "e" + "Z" = "eZ"..........
print(reverse)  # nahseeZ

# DICTIONARY

# FOR KEYS

student = {"name": "Zeeshan", "age": 21, "course": "AI"}
for key in student:
    print(key)
# or

student = {"name": "Ali", "age": 11, "course": "urdu"}
for key in student.keys():
    print(key)


# FOR VALUES

students = {"name": "husnain", "class": "6th"}
for key in students:  # for this method to work variable name must be "key"
    print(students[key])
# or

students = {"name": "husnain", "class": "6th"}
for k in students.values():
    print(k)


# BOTH KEYS & VALUES

stu = {"name": "hasan", "class": "8th"}
for l, m in stu.items():
    print(l, m)  # name here doesn't matter like key 0r value
# or

stud = {"name": "qasim", "class": "9th"}
for key in stud:  # must be variable "key" here also
    print(key, stud[key])

student_list = [
    {"name": "husnain", "class": "6th"},
    {"name": "hasan", "class": "7th"},
]
for student in student_list:
    print(f"Name: {student.get("name",'')} | Class: {student.get("class",'')}")
# .get() gives us value of the 
# f"" <-- this is f string ( we can use variables to print inside string "")

