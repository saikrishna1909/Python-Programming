num1 = eval(input("Enter the first number :"))
num2 = eval(input("Enter the second number:"))
def sample(num1,num2):
    while 1:
        print("Enter")
        print("1. TO PERFORM ADDITITON ")
        print("2. TO PERFORM SUBTRACTION")
        print("3. TO PERFORM MULTIPICATION")
        print("4. TO PERFORM DIVISION")
        print("5. TO EXIT")
        ch = int(input(""))
        if ch == 1:
            c = num1+num2
            print("Addition of ",num1,"and",num2,"is:",c)
        elif ch == 2:
            c = num1-num2
            print("Subtraction of ",num1,"and",num2,"is:",c)
        elif ch == 3:
            c = num1*num2
            print("Multiplication of ",num1,"and",num2,"is:",c)
        elif ch == 4:
            c = num1/num2
            print("Division of ",num1,"and",num2,"is:",c)
        elif ch == 5:
            exit()
        else:    
            print("Please enter a valid number")
sample(num1,num2)
