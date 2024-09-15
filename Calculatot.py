print("Welcome to me mini calculator")
num1=int(input('Enter 1st number'))
num2=int(input('Enter 2nd number'))
print("press 1 for Addition\n press 2 for substraction\n press 3 for Multiplication\n press 4 for division")
choice=int(input("Enter your choice from 1-4:"))
if choice==1:
    print("Your result is",num1+num2)
elif choice==2:
    print("Your result is",num1-num2)
elif choice==3:
    print("Your result is",num1*num2)
elif choice==4:
    print("Your result is",num1//num2)
else:
    print("Invalid input")
