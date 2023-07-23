def get_password(min_length):
    while True:
        password = input("Enter your password: ")
        if len(password) < min_length:
            print(f"Password should be at least {min_length} characters long. Try again.")
        else:
            return password

def main():
    min_password_length = 8  # Set the minimum password length here
    password = get_password(min_password_length)
    print(f"Password accepted: {password}")

if __name__ == "__main__":
    main()
