while True:
    
    print("This is created by Nitesh singh Baghel(whitedevil)")




    print("+" "Addition")
    print("-" "Subtraction")
    print("*" "Multiplication")
    print("/" "Division")
    
    
    print("Entre q or Q to Exit")


    choice = input("enter your symbol what you want to do :")

    if choice == 'q' or choice == 'Q':
        break

    num1 =float(input("Entre First Number :"))
    num2 =float(input("Entre Second  Number  :"))

    if choice == "+":
        print(num1,"+", num2, "=", (num1+num2))

    elif choice == "-":
        print(num1,"-", num2, "=", (num1+num2))

    elif choice == "*":
        print(num1,"*", num2, "=", (num1+num2))    

    elif choice == "/":
        if num2 == 0.0:
            print("Divide by 0 Error")
        else:
          print(num1,"/", num2, "=", (num1+num2))
          print.__sizeof__(50)


    else:
     print("Invalid option")
    
        