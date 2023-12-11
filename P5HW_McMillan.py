  # This program is a math quiz program that allows the user to practice their addition and subtraction skills with random numbers. It tells you how many guesses you need and when you are right or wrong.

   # 12-07-23

   # CTI-110 P5HW - Math Quiz

   # Alexis McMillan

   #
# Import the random module to generate random numbers
import random

# Define a function that displays the menu and returns the user's choice
def display_menu():
    print("Welcome to Math quiz")
    print("")
    print("")
    print("") 
    print("MAIN MENU")
    print("-------------------------")
    print("1. Adding random numbers")
    print("2. Subtracting random numbers")
    print("3. Exit")
    choice = int(input("Enter your choice: "))
    return choice

# Define a function that generates two random numbers and returns them as a tuple
def generate_numbers():
    num1 = random.randint(100, 999)
    num2 = random.randint(100, 999)
    return (num1, num2)

# Define a function that performs the addition quiz and returns the number of guesses
def addition_quiz():
    # Generate two random numbers
    num1, num2 = generate_numbers()
    # Display the numbers
    print(f"  {num1}")
    print(f"+ {num2}")
    print("-----")
    # Initialize the answer and the number of guesses
    answer = 0
    guesses = 0
    # Loop until the answer is correct
    while answer != num1 + num2:
        # Increment the number of guesses
        guesses += 1
        # Ask the user to enter the answer
        answer = int(input("Enter the answer: "))
        # Check if the answer is correct
        if answer == num1 + num2:
            # Congratulate the user and return the number of guesses
            print("Congratulations! You got it right.")
            return guesses
        else:
            # Notify the user if the answer is too low or too high and ask them to guess again
            if answer < num1 + num2:
                print("Sorry, your answer is too low. Try again.")
            else:
                print("Sorry, your answer is too high. Try again.")

# Define a function that performs the subtraction quiz and returns the number of guesses
def subtraction_quiz():
    # Generate two random numbers
    num1, num2 = generate_numbers()
    # Display the numbers
    print(f"  {num1}")
    print(f"- {num2}")
    print("-----")
    # Initialize the answer and the number of guesses
    answer = 0
    guesses = 0
    # Loop until the answer is correct
    while answer != num1 - num2:
        # Increment the number of guesses
        guesses += 1
        # Ask the user to enter the answer
        answer = int(input("Enter the answer: "))
        # Check if the answer is correct
        if answer == num1 - num2:
            # Congratulate the user and return the number of guesses
            print("Congratulations! You got it right.")
            return guesses
        else:
            # Notify the user if the answer is too low or too high and ask them to guess again
            if answer < num1 - num2:
                print("Sorry, your answer is too low. Try again.")
            else:
                print("Sorry, your answer is too high. Try again.")

# Define the main function that runs the program
def main():
    # Display the menu and get the user's choice
    choice = display_menu()
    # Loop until the user chooses to exit
    while choice != 3:
        # Check if the choice is valid
        if choice in [1, 2]:
            # Perform the quiz based on the choice and get the number of guesses
            if choice == 1:
                guesses = addition_quiz()
            else:
                guesses = subtraction_quiz()
            # Display the number of guesses
            print(f"It took you {guesses} guesses to get the right answer.")
        else:
            # Display an error message for invalid choice
            print("Invalid choice. Please enter 1, 2, or 3.")
        # Display the menu and get the user's choice again
        choice = display_menu()
    # Display a farewell message
    print("Thank you for using the math quiz program. Goodbye.")

# Call the main function to start the program
main()
