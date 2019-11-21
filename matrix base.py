#write a functions to print a matrix base on user , like if user types 3 row and 3 colum you should print 3*3 matrix with all  1's
# def matrix(a,b):
#     A=[]
#     B=[]
#     for i in range (a):
#         for j in range(b):
#             B.append(3)
#         A.append(B)
#         B=[]
#
#     return A
# x = int(input ("enter the first number"))
# y=int(input ("enter the second number"))
# print(matrix(x,y))




a=[]
for i in range (3):
    a.append([])
    for j in range(3):
        a[i].append(1)
print(a)






