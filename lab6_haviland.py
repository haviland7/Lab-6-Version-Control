def encoder(message):
    result = ''
    for digit in message:
        new_digit = str((int(digit) + 3) % 10)
        result += new_digit
    return result


def main():
    while True:
        print("Menu")
        print("-------------")
        print("1. Encode")
        print("2. Decode")
        print("3. Quit")
        choice = input("Please enter an option: ")
        if choice == "1":
            value = input("Please enter your password to encode: ")
            print("Your password has been encoded and stored!")
            encoded = encoder(value)
        elif choice == "2":
            print(f"The encoded password is {encoder(value)} and the original password is {decoder(encoded)}")
        elif choice == "3":
            break
        else:
            print("Invalid choice")
        print()


main()