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

