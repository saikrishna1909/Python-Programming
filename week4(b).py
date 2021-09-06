num = eval(input("Enter the length of the list:"))
lis = []
print("Enter the elements of list:")
for i in range(num):
    e = eval(input())
    lis.append(e)
filters = lambda x: x%2 == 0
results = filter(filters,lis)
print(list(results))
