# type-casting 
# there are two types of casting

# 1. Implicit Casting ---> python auto converts from one data type to another

math = 51
science = 50.55
total_marks = math + science
print(total_marks) # 101.55 auto converts

# 2. Explicit Casting ---> we have to do casting manually 

history = 55.3
print(int(history)) # shows 55 integer no. 

geography = "57" # <str>
x = float(geography)
print(type(geography)) # here orignal x is still <str> bcuz it creates a converted value 
print(type(x))         # here the converted value is in x and now is <float>

# %%
