#  the logical operator are 
# 01 and
# 02 or 
# 03 not
#  01 and
a = 56
if(a<54 and a<45):
    print("yes a is greater than 54 and 45")
else:
    print("no it is not gteater than 54 and 45")#in this the both condition are checked and then it goes to the next

# 02 or
if (a<56 or a>45):
    print("yes the given condition is true ")
else:
    print("the given condition is not true")# in this if only one condition is also true then the program will execute 

# 03 not this will reverse the condition 

# use of is , it works  like =
a = 54
if(a is 54):
    print("yes it is true")

# use of in,it works like =
a = {7,8,9,7,6}
print(7 in a)
    
