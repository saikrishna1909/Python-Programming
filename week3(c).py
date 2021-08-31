fact = 1
num = eval(input("Enter the number: "))
def factorial(fact,num):
    for i in range(num):
        fact = fact*(i+1)
    print("Factorial of ",num,"is: ",fact)
factorial(fact,num)
