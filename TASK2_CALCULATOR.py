#TASK 2: Calculator

#Addition
def add_numbers(x, y):
    return x+y

#Subtraction
def sub_numbers(x, y):
    return x - y

#Multiplication
def mul_numbers(x, y):
    return x * y

#Division
def divide_numbers(x, y):
    return x / y

#modulus
def mod(x, y):
    return x % y


while(True):

    try:
        a = float(input("\nEnter first number: "))
        b = float(input("Enter second number: "))
    except:
        print("Enter a valid numbers")
    
    print("\n1: Addition ")
    print("2: Subtraction")
    print("3: Multiplication")
    print("4: Division")
    print("5: Modulus/ Remainder")
    operation = input("Choose an operation by chosing '1','2','3','4','5': ")

    if operation == '1':
        print(a,"+",b,":", add_numbers(a, b))
    elif operation == '2':
        print( a,"-",b,":", sub_numbers(a, b))
    elif operation == '3':
        print(a,"*",b,":",mul_numbers(a, b))
    elif operation == '4':
        print(a,"/",b,":",divide_numbers(a, b))
    elif operation == '5':
        print(a,"%",b,":",mod(a, b))
    else:
        print("Enter a valid operation! ")

