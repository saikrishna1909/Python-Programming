a = lambda x:x*2
b = lambda y,z:y+z
x = eval(input("Enter the number to be doubled:"))
y = eval(input("Enter the first number:"))
z = eval(input("Enter the second number:"))
print("The double of ",x,"is:",a(x))
print("The sum of ",y,"and",z,"is:",b(y,z))
