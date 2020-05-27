'''
Created on May 26, 2020

@author: ITAUser
'''
def main():
    print("\n")
    print("WELCOME TO MY CALCULATOR!!!")
    
    print("\n")
    print("For addition use + in the operator")
    
    print("For subtraction use - in the operator")
    
    print("For multiplication use * in the operator")
    
    print("For devision use / in the operator")
    
    print("For exponents use ** in the operator")
    
    print("For square root use //")
    
    print("\n")
    num1 = float(input("Enter First Number:"))
    op = input("Enter Operator:")
    num2 = float(input("Enter Second Number:"))

    if op == "+":
        print (num1 + num2)
    elif op == "-":
        print (num1 - num2)
    elif op == "*":
        print (num1 * num2)
    elif op == "/":
        print (num1 / num2)
    elif op == "**":
        print (num1 ** num2)
    elif op == "//":
        print (num1 ** 0.5)
    else:
        print ("Invalid Input")
    print("\n")
    restart = input ("Type yes if you want to solve a problem").lower()
    if restart == "yes":
        main()
    else:
        exit()
main()
