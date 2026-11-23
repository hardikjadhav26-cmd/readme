while True:
    password = input("Enter a password (or 'stop' to exit): ")

    if password.lower() == "stop":
        print("Program stopped.")
        break

    if (len(password) >= 8 and
        any(ch.isupper() for ch in password) and
        any(ch.islower() for ch in password) and
        any(ch.isdigit() for ch in password)):

        print("Strong Password")
    else:
        print("Weak Password")
