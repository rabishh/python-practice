# # 01 write a program to create a dictonary of hindi eords with values as their english translation progide user with an ootion to look it up
# a = {
#     "kaam" : "work",
#     "araam" : "rest",
#     "masti" : "enjoy",
#     "mata" : "mother",
#     "pita" : "father"
#      }
# b  = input("enter the any of the following kaam,araam,masti,mata,pita\n")
# # print("your meaning is : ", a[b])#this line will throw an error if the word is not available 
# print("your meaning of the word is : ", a.get(b))# this line  will not throw an error
# # 02 write a program to input eight numbers from the user and display all the unique number
# a = int(input('enter your first number:\n'))
# b = int(input('enter your second number :\n'))
# c = int(input('enter your third number:\n'))
# e = int(input('enter your fourth number :\n'))
# f = int(input('enter your fifth number :\n'))
# g = int(input('enter your sixth number :\n'))
# h = int(input('enter your seventh number;\n'))
# list = {a,b,c,e,f,g,h}
# print(list)
# 03 what will the length of the following set s
# s = set()
# s.add(20)
# s.add(20.0)
# s.add("20") 
# s = set()
# s.add(20)
# s.add(20.0)
# s.add("20") 
# print(s)
# 04 creat an empty dictionary allow 4 friends to enter their favourite language as values and use keys as their names assume that the names are unique 
a = {
    "rabish" : input("rabish enter your favourite langauge:"),
    "abhishek" : input("abhishek enter your favourite langauge:"),
    "sonal" : input("sonal enter your favourite langauge:"),
    "mummy" : input("mummy enter your favourite langauge:")
}
print(a)