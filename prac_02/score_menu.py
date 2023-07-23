"""Program to handle scores."""

def main():
    """Main function to run the program."""

    while True:
        print_menu()
        choice = input("Enter your choice: ").strip().lower()

        if choice == "g":
            score = get_valid_score()
        elif choice == "p":
            print_result(score)
        elif choice == "s":
            show_stars(score)
        elif choice == "q":
            print("Farewell! Thanks for using the program.")
            break
        else:
            print("Invalid choice. Please try again.")

def get_valid_score():
    """
    Prompt the user for a valid score between 0 and 100 inclusive.

    Returns:
        int: The valid score entered by the user.
    """
    min_score = 0
    max_score = 100
    while True:
        try:
            score = int(input("Enter a score (0-100): "))
            if min_score <= score <= max_score:
                return score
            else:
                print("Invalid score. Please enter a score between 0 and 100.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")

def print_result(score):
    """
    Print the result based on the given score.

    Args:
        score (int): The score to determine the result from.
    """
    # Assume you have a function named 'determine_result()' in score.py that returns the result.
    # You can copy or import the function from score.py here.
    # For this example, we'll just print a dummy result.
    result = "Pass" if score >= 50 else "Fail"
    print(f"The result is: {result}")

def show_stars(score):
    """
    Display stars based on the given score.

    Args:
        score (int): The score to determine the number of stars.
    """
    print("Stars:")
    print("*" * score)

def print_menu():
    """Print the main menu."""
    print("\nMain Menu:")
    print("(G)et a valid score")
    print("(P)rint result")
    print("(S)how stars")
    print("(Q)uit")

if __name__ == "__main__":
    main()
