# This is a short program made by Ossi Lahti (version: 6.9.2020)
# The idea is to check if a number belongs to the Fibonacci sequence.
# My goal was to learn some basic stuff about Python.


def input_checker():  # Validates the input to be in the correct format.
    if user_input.isdigit() and int(user_input) < 250:  # Checks if the input is a natural number {0, 1, 2..}
        # and below 250
        print('The input is in the correct format.')
        print('.\n.\n.')
    else:
        print('Format is invalid! (it needs to be an INTEGER below 250).')


def sequence_creation():  # Creates the Fibonacci sequence in a list and prints the outcome
    sequence_creation.a, b = 0, 1
    sequence_creation.list = [0]  # A list for the numbers
    while b <= 250:
        sequence_creation.a, b = b, sequence_creation.a + b  # It means that a = b and b = a+b
        sequence_creation.list.append(sequence_creation.a)
    print('Fibonacci sequence below 250 looks like this: \n' + str(sequence_creation.list))


def last_checker():  # Checks if user's input is in the list
    if int(user_input) in sequence_creation.list:
        print('\nIt is a match! Your input ' + str(user_input) + ' is there.')
    else:
        print('\nIt does not match. The number ' + str(user_input) + ' is not in the Fibonacci sequence.')

# Main program


print('This is a program where the user inputs a number below 250 and \n'
      'the program resolves if it belongs to the Fibonacci sequence.\n')
print('Please input a number below 250 in the next line.')
user_input = input('Your number: ')  # Global attribute for user input
print('Program checks if the number is in the asked format and in the Fibonacci sequence. \n.\n.\n.')

input_checker()
sequence_creation()
last_checker()
