
num1=float(input("enter the first number"))
num2=float(input("enter the second number"))
operation=input("choose the process you want to perform(+,-,/,*) ")
def calculate(num1,num2,operation):
    if operation == "*" :
        return num1*num2
    elif operation == "/" :
        if num2 == 0:
            return "division by zero is not allowed"
        else :
            return num1/num2
        return num1/num2
    elif operation == "+" :
        return num1+num2
    elif operation == "-" :
        return num1-num2
    else :
        return "please enter a valid operation"
result=calculate(num1,num2,operation)
print (result)
       



