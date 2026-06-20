import random
import string

def generate_password(length):
    # Step 1: Character pool create pannuthu (letters + digits + symbols)
    characters = string.ascii_letters + string.digits + string.punctuation

    # Step 2: Random ah characters select panni password generate pannuthu
    password = ''.join(random.choice(characters) for i in range(length))

    return password


def main():
    print("=== PASSWORD GENERATOR ===")

    while True:
        try:
            # Step: User input - password length kekkurathu
            length = int(input("Enter desired password length: "))

            if length <= 0:
                print("Please enter a positive number.\n")
                continue

            # Step: Password generate pannurathu
            password = generate_password(length)

            # Step: Generated password display pannurathu
            print(f"Generated Password: {password}\n")

        except ValueError:
            print("Invalid input! Please enter a number.\n")
            continue

        # Optional: another password generate panna venuma nu kekkurathu
        again = input("Generate another password? (y/n): ").lower()
        if again != 'y':
            print("Thank you for using Password Generator!")
            break


if __name__ == "__main__":
    main()