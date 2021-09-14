# # 01 write a program to find greatest of four number enterd by the usaer
# a = int(input("enter your first number:"))
# b = int(input("enter your second number:"))
# c = int(input("enter your third number:"))
# d = int(input("enter your fourth number:"))
# if(a>b and a>c and a>d):
#     print(str(a) + "  is greater\n")
# elif(b>a and b>c and b>d):
#     print(str(b) + "  is grerter")
# elif(c>a and c>b and c>d):
#     print(str(c) + "  is greater")
# else:
#     print(str(d) + " is greater")

# #  02 write a program to find out whether a student is pass or fail if it  require total 40% and at least 33% in each subject to pass.
# #  assume 3 subject and take marks as an input from user.

# a = int(input("enter your subject 1 marks:"))
# b = int(input("enter your subject 2 marks:"))
# c = int(input("enter your subject 3 marks:"))
# if(a<33 or b<33 or c<33):
#     print("your are fail because you have less than 33% in one of the subject")
# elif(a+b+c)/3<40:
#     print("you are fail because your percentage is less than 40")
# else:
#     print(" you are pass the exam")

# # 03 a spam comment is defined as a text containing followings key word "make a lot of money ","buy now ", "subscribe now","click this",
# # "write a program to dectect these spam"
# a = input('enter your comment ')
# if(a in "make a money"  or a in "subscribe now" or a in "click this"  or a in "buy now"):
#     print("hey! its spam dectes")
# else:
#     print("wow! you are safe")

# # 04 write a program to find whether a given user name contain less than 10 character or not 
# a = input("enter your name\n")
# if(len(a) > 10):
#     print("hey! your name is greater than 10 digit")
# else:
#     print("no your name is not greater than 10 digit")

# # 05 write a program which find out whether a given name is present in a list or not
# b = input("please enter your name\n")
# a = {"rabish","abhishek","shambhu","sonal","kumkum"}
# if(b in a ):
#     print("hey! the name you entered is in the list")
# else:
#     print("the name you enterd is not in the list")

# 06 write a program to calculate the grade of a sstudent from his marks from the following scheme:
# 90-100->ex,80-90->a,70-80->b,60-70->c,50-60->d,<50->f
 
a = int(input("enter your marks:"))
if(a > 90):
    print("congratulation! your grade is EX")
elif(a > 80):
    print("congratulation! your grade is A")
elif(a > 70):
    print("congratulation! your grade is B")
elif(a > 60):
    print("congratulation! your grade is C")
elif(a > 50):
    print("congratulation! your grade is D")
else:
    print("oops! you are fail")


