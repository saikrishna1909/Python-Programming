num = int(input("Enter the length of the list:"))
lis = []
print("Enter the elements of list:")
for i in range(num):
    e = eval(input())
    lis.append(e)
filters = lambda x:x*2
result = map(filters,lis)
print(list(result))
