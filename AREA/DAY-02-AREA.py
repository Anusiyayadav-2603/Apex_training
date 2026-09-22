while True:
    print("\n1. Area of Circle")
    print("2. Area of Rectangle")
    print("3. Area of Square")
    print("4. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        r = float(input("Enter radius: "))
        area = 3.14 * r * r
        print("Area of Circle =", int(area))

    elif choice == 2:
        l = float(input("Enter length: "))
        b = float(input("Enter breadth: "))
        area = l * b
        print("Area of Rectangle =", int(area))

    elif choice == 3:
        s = float(input("Enter side: "))
        area = s * s
        print("Area of Square =", int(area))

    elif choice == 4:
        print("Program exited.")
        break

    else:
        print("Invalid choice")
