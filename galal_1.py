import random
import string

print("Welcome to the Password Generator")

# Getting input for the number of characters in the password
number_of_passwd = int(input("Enter the total number of characters in the password: "))
number_let = int(input("Enter the number of letters in the password: "))
number_num = int(input("Enter the number of digits in the password: "))
number_ch = int(input("Enter the number of symbols in the password: "))

# Check if the total number of characters matches the sum of letters, numbers, and symbols
total_check = number_let + number_ch + number_num

if total_check == number_of_passwd:
    # Generate random letters, numbers, and symbols
    random_let = random.choices(string.ascii_letters, k=number_let)
    random_sympol = random.choices(string.punctuation, k=number_ch)
    random_num = random.choices(string.digits, k=number_num)

    # Combine all parts into one list
    random_password_list = random_let + random_sympol + random_num

    # Shuffle the combined list to make the password random
    random_password=random.shuffle(random_password_list)

    # Join the shuffled list into a string
    random_password = ''.join(random_password_list)

    print(f"Your generated password is: {random_password}")
else:
    print("Error: The sum of letters, numbers, and symbols does not equal the total number of characters.")
