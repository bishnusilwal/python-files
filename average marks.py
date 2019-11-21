# uses of 2D lists to imitate tables!!!!!
result=[['name','maths','english'],
        ['ram',68,65],
        ['hari',89,56]
        ]
#
# print(result[1])
# sum =0
# avg=0
# for i in range (1,len(result[1])):
#     sum =result[1][i]+sum
#     avg=sum/len(result[1])-1
# print(sum)
# print(avg)



sum=0
avg=0
for p in range (1,len(result[2])):
    sum=result[1][p]+result[2][p]
    print("sum in ",result[0][p]," is ",sum )
    print(sum/2)

