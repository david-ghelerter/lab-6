def encoder(password):
    res = []
    decode_list = list(password.strip(" "))  # Converts string to a list
    for i in range(0, len(decode_list)):  # Adds 3 to each list element
        res.append(int(decode_list[i]) + 3)

    return ''.join(str(i) for i in
                   res)  # returns a string, source: https://www.simplilearn.com/tutorials/python-tutorial/list-to-string-in-python


def decoder(encoded_password):
    pass


def print_menu():
    print('Menu')
    print('-------------')
    print('1. Encode')
    print('2. Decode')
    print('3. Quit')


def is_valid(num):
    return num == 1 or num == 2 or num == 3


def main():
    while True:
        print_menu()

        option = int(input('Please enter an option: '))

        # Error checking for menu options
        while not is_valid(option):
            print('That is not a valid option, please choose again')
            option = int(input('Please enter an option: '))

        if option == 1:  # Encode password
            password = input("Please enter your password to encode: ")
            encoded_password = encoder(password)
            print('Your password has been encoded and stored!')
        elif option == 2:  # Decode password
            print(f'The encoded password is {encoded_password}, and the original password is {decoded_password}')
        elif option == 3:  # Quit
            break


if __name__ == '__main__':
    main()