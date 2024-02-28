import string

def check_password_strength():
    while True:
        password = input('Enter the password: ')
        strength = 0
        remarks = ''
        lower_count = upper_count = num_count = wspace_count = special_count = 0

        for char in password:
            if char in string.ascii_lowercase:
                lower_count += 1
            elif char in string.ascii_uppercase:
                upper_count += 1
            elif char in string.digits:
                num_count += 1
            elif char == ' ':
                wspace_count += 1
            else:
                special_count += 1

        if lower_count >= 1:
            strength += 1
        if upper_count >= 1:
            strength += 1
        if num_count >= 1:
            strength += 1
        if wspace_count >= 1:
            strength += 1
        if special_count >= 1:
            strength += 1

        if strength == 1:
            remarks = ('That\'s a very bad password.'
                       ' Change it as soon as possible.')
        elif strength == 2:
            remarks = ('That\'s a weak password.'
                       ' You should consider using a tougher password.')
        elif strength == 3:
            remarks = 'Your password is okay, but it can be improved.'
        elif strength == 4:
            remarks = ('Your password is hard to guess.'
                       ' But you could make it even more secure.')
        elif strength == 5:
            remarks = ('Now that\'s one hell of a strong password!!!'
                       ' Hackers don\'t have a chance guessing that password!')

        print('Your password has:-')
        print(f'{lower_count} lowercase letters')
        print(f'{upper_count} uppercase letters')
        print(f'{num_count} digits')
        print(f'{wspace_count} whitespaces')
        print(f'{special_count} special characters')
        print(f'Password Score: {strength / 5}')
        print(f'Remarks: {remarks}')

        choice = input('What would you like to do?\n'
                       '1. Check another password\n'
                       '2. Improve your password\n'
                       '3. Exit the code\n'
                       'Enter your choice (1/2/3): ')

        if choice == '1':
            continue
        elif choice == '2':
            improve_password(password)
        elif choice == '3':
            print("Exiting the code...")
            break
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")

def improve_password(password):
    print("You've chosen to improve your password.")
    print("Here are some recommendations to improve your password:")

    # Check if more special characters are needed
    if not any(char in string.punctuation for char in password):
        print("- Add more special characters (!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~)")

    # Check if more numbers are needed
    if not any(char.isdigit() for char in password):
        print("- Add more numbers (0-9)")

    # Check if more uppercase letters are needed
    if not any(char.isupper() for char in password):
        print("- Add more uppercase letters (A-Z)")

    # Check if more lowercase letters are needed
    if not any(char.islower() for char in password):
        print("- Add more lowercase letters (a-z)")

if __name__ == '__main__':
    print('===== Welcome to Password Strength Checker =====')
    check_password_strength()
