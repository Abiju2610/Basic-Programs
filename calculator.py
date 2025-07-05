print("Operations: add, subtract, multiply, divide, quit")
calc = input("Choose from operations above: ")

answer = 0

while calc != "quit":
    if calc == "add" or calc == "subtract" or calc == "multiply" or calc == "divide":
        while True:
            try:
                num1 = int(input("Enter first number: "))
            except ValueError:
                print("Invalid value. Please enter an integer")
            else:
                break
        
        while True:
            try:
                num2 = int(input("Enter second number: "))
            except ValueError:
                print("Invalid value. Please enter an integer")
            else:
                break
        
        if calc == "add":
            answer = num1 + num2
        elif calc == "subtract":
            answer = num1 - num2
        elif calc == "multiply":
            answer = num1 * num2
        elif calc == "divide":
            answer = num1 / num2
    
        print("Answer is: ", answer)
    
        print("Operations: add, subtract, multiply, divide, quit")
        calc = input("Choose from operations above: ")

        
    else:
        print("\nInvalid Operation")
        print("Operations: add, subtract, multiply, divide, quit")
        calc = input("Choose from operations above: ")

    
