import random

"""Temperature Conversion Functions"""

# ... (previous functions remain unchanged)

def generate_random_score():
    """Generate a random score between 0 and 100."""
    return random.randint(0, 100)

def main():
    """Main function to demonstrate temperature conversions."""
    # ... (previous code remains unchanged)

    # Generate a random score
    random_score = generate_random_score()

    print("\nRandomly Generated Score:", random_score)

    if random_score < 0 or random_score > 100:
        print("Invalid score")
    else:
        if random_score > 90:
            print("Excellent")
        elif random_score > 50:
            print("Passable")
        else:
            print("Bad")

if __name__ == "__main__":
    main()
