def add(x, y):
    return x+y


def subtract(x, y):
    return x-y


def multiply(x, y):
    return x*y


def divide(x, y):
    if y == 0:
        return "Improper action."
    return x/y


def modulo_division(x, y):
    if y == 0:
        return "Improper action."
    return x % y


print("\t\t\t***Welcome to Calculator App***\n\n\n")
act = 0
while act != "2" or act != "exit app":
    print("1. Continue with app\n2. Exit app\n")
    a = input("Enter your first number: ")
    b = input("Enter your second number: ")
    choice = 0
    while choice != "6" or choice != "Exit the app":
        print("1. Addition\n2. Subtraction\n3. Multiplication\n4. Division\n5. Modulo Division(Gives the reminder when given numbers are divided)\n6. Exit the app")
        choice = input("Enter the operation you would like to perform on the given input: ")
        choice.lower()
        if choice == "1" or choice == "addition":
            result = add(int(a), int(b))
            print(a, " + ", b, " = ", result)
        elif choice == "2" or choice == "subtraction":
            result = subtract(int(a), int(b))
            print(a, " - ", b, " = ", result)
        elif choice == "3" or choice == "multiplication":
            result = multiply(int(a), int(b))
            print(a, " * ", b, " = ", result)
        elif choice == "4" or choice == "division":
            result = divide(int(a), int(b))
            print(a, " / ", b, " = ", result)
        elif choice == "5" or choice == "modulo division":
            result = modulo_division(int(a), int(b))
            print(a, " % ", b, " = ", result)
        elif choice == "6" or choice == "exit the app":
            break
        else:
            print("Please enter a valid choice.")
    act = input("Enter your action: ")
    act.lower()
    if act == "2" or act == "exit app":
        break
print("\t\t\t***THANK YOU***")