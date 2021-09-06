import functools
num = int(input("Enter the length of the list: "))
lis = []
print("Enter the elements of list:")
for i in range(num):
    e = eval(input())
    lis.append(e)
a = lambda x,y:x+y
result = functools.reduce( a,lis)
print(result)
