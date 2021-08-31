list1 = []
list2 = []
num1 = eval(input("Enter the size of list1"))
num2 = eval(input("Enter the size of list2"))
print("Enter the elements of list1:")
for i in range(num1):
    e = eval(input())
    list1.append(e)
for i in range(num2):
    e = eval(input())
    list2.append(e)
def sample(l1,l2):
    if len(l1) != len(l2):
        print("Lists are not equal")
    elif sorted(l1) == sorted(l2):
        print("Lists are equal")
    else:
        print("Lists are not equal")
sample(list1,list2)
