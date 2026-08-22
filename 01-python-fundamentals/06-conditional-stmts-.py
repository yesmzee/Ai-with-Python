# CONDITIONAL STATEMENTS :
# conditional statements are used to perform different decisions based on different conditions.

temp = int(input("enter the temperature :"))
# IF-ELSE

# if-else is used when you want to perform :
# one action if the condition is true and
# another action if it is false.

# IF --> alone used when you want to execute code only if a condition is true
if temp > 30:
    print("it is hot today !")

# ELSE --> runs if previous condition is false.
else:
    print("it is not hot today !")


# IF-ELIF-ELSE --> used when there are multiple conditions or decisions

# SIMPLE RESULT CALCULATION :

math = float(input("enter math marks : "))
print("math :", math)
eng = float(input("enter english marks : "))
print("english :", eng)
sci = float(input("enter science marks : "))
print("science :", sci)
hist = float(input("enter history marks : "))
print("history :", hist)

total_obt = math + eng + sci + hist
print("total marks : 400 ")
print("total obtained marks : ", total_obt)

percent = float((total_obt / 400) * 100)
print("percentage :", percent, "%")

if percent >= 90:
    print("congrats ! you got A grade")

elif percent >= 80:
    print("congrats ! you got B grade")

elif percent >= 70:
    print("you got C grade")

elif percent >= 60:
    print("try hard ! you got D grade")

else:
    print("fail ! sorry below 60% are fail according to Zeeshan")


# NESTED IF --> means an if statement inside another if statement

# FOR CHECKING SUBJ NAME :

subj = input("enter you subject name (bio, comp, chem) :")
fsc_total_m = int(input("enter you total marks in fsc :"))

if subj == "comp" or subj == "bio" or subj == "chem":
    if subj == "comp":
        if fsc_total_m >= 900:
            print("you can enroll in computer science dept.")
        else:
            print("sorry ! marks criteria not met for computer science dept.")
    elif subj == "bio":
        if fsc_total_m >= 950:
            print("you can enroll in medical dept.")
        else:
            print("sorry ! marks criteria not met for medical dept.")
    elif subj == "chem":
        if fsc_total_m >= 930:
            print("you can enroll in chemistry dept.")
        else:
            print("sorry ! marks criteria not met for chemistry dept.")
else:
    print("enter valid subject name")


# COMBINED CONDITIONAL STATEMENTS --> used when you want to combine multiple conditions in a single if statement

# AGE CHECK FOR VOTE :

age = int(input("enter your age :"))
region = input("enter your region : [baloch, sindh, punjab, kpk, gb, ajk ] :")

if age >= 18 and region == "gb":
    print("you can vote in gilgit-baltistan")
elif age >= 18 and region == "baloch":
    print("you can vote in balochistan")
elif age >= 18 and region == "sindh":
    print("you can vote in sindh")
elif age >= 18 and region == "kpk":
    print("you can vote in khyber-pakhtunkhuwa")
elif age >= 18 and region == "kpk":
    print("you can vote in azad jammu kashir")
elif age >= 18 and region == "punjab":
    print("you can vote in punjab")
else:
    print("you are not eligible to vote ")