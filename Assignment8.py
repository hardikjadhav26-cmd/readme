def calculate_area(shape, a, b=0):
    if shape == "circle":
        return 3.14 * a * a

    elif shape == "rectangle":
        return a * b

    elif shape == "triangle":
        return 0.5 * a * b

    else:
        return "Invalid shape"


print("1. Circle")
print("2. Rectangle")
print("3. Triangle")

choice = input("Enter shape: ").lower()

if choice == "circle":
    r = float(input("Enter radius: "))
    print("Area of circle =", calculate_area("circle", r))

elif choice == "rectangle":
    l = float(input("Enter length: "))
    w = float(input("Enter width: "))
    print("Area of rectangle =", calculate_area("rectangle", l, w))

elif choice == "triangle":
    base = float(input("Enter base: "))
    height = float(input("Enter height: "))
    print("Area of triangle =", calculate_area("triangle", base, height))

else:
    print("Invalid choice")
