# Reading of a file
#
# f = open('mydata.txt','r')
#
# #print(f.read())
#
# print(f.readline())
# print(f.readline())
# print(f.readline(),end="#")
#
# Writing to a file
#
# f1 = open('abc','w')
#
# f1.write("Soemthing")
# f1.write("Laptop")
#
# Append to a file
#
# f = open('abc','a')
#
# f.write("Hi there")
#
#
# Now do we copy from one file to another file
#
# f = open('mydata.txt','r')
# f1 = open('abc','a')
# for i in f:
#     f1.write(i)
#
#
# How do we print something which is ending with a jpg file
#
# f =open('1_hRIZr550N8UK8iSNjaBCjw.png','r')
#
# f.read()
#
# this will fail. that is the reason you might have to read it as 'rb'
#
# f =open('Picture1.jpg','rb')
# #f =open('Picture1.jpg','wb')
# f.read()