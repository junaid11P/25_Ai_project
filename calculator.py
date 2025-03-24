def add(x,y):
    return x+y
def sub(x,y):
    return x-y
def mult(x,y):
    return x*y
def div(x,y):
    if y==0:
        return "error! division by zero not allowed"
    else:
        return x/y
def calculator():
    print("select option:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiple")
    print("4. Division")
    while True:
        choice = input("Enter choices(1/2/3/4):")
        if choice in ['1','2','3','4']:
            num1=float(input("Enter first number:"))
            num2=float(input("Enter second number:"))
            
            if choice =='1':
                print(f"{num1}+{num2}={add(num1,num2)}")
            if choice =='2':
                print(f"{num1}-{num2}={sub(num1,num2)}")
            if choice =='3':
                print(f"{num1}*{num2}={mult(num1,num2)}")
            if choice =='4':
                print(f"{num1}/{num2}={div(num1,num2)}")
                
        next_calculation=input("do you want to perform another calculation? (yes/no):")
        if next_calculation.lower() !='yes':
            break 
        print("Exiting calculator... Goodbye")
calculator()
