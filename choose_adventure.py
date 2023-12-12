import time

def introduction():
    print("Welcome!")
    time.sleep(1)
    print("You have just spawned in an unfamiliar place.")
    time.sleep(1)
    print("Your goal is to bypass the challenges and reach the treasure.\n")

def make_choice(choices):
    print("Choose your action:")
    for i, choice in enumerate(choices, start=1):
        print(f"{i}. {choice}")

    while True:
        try:
            choice_num = int(input("Enter the number of your choice: "))
            if 1 <= choice_num <= len(choices):
                return choice_num
            else:
                print("Invalid choice. Please enter a valid number.")
        except ValueError:
            print("Invalid input. Please enter a number.")

def forest_scenario():
    print("You are now entering a dark forest.")
    time.sleep(1)
    print("Up ahead there are two paths.")
    time.sleep(1)

    choices = ["Take the left path", "Take the right path"]
    choice = make_choice(choices)

    if choice == 1:
        print("You come across a friendly giant. It guides you through the forest safely.")
        return True
    else:
        print("You get lost in the forest. After some time, you will hopefully find your way out.")
        return False

def cave_scenario():
    print("You have now arrived at a cliff.")
    time.sleep(1)
    print("You are now worried about the drop.")
    time.sleep(1)

    choices = ["Jump", "Turn back"]
    choice = make_choice(choices)

    if choice == 1:
        print("You jumped, landed on a trampoline, and was greeted with a treasure chest!")
        return True
    else:
        print("You decide not to jump and continue on elsewhere.")
        return False

def conclusion():
    print("Congratulations! You've completed game!")

def play_game():
    introduction()

    # Scenario 1: Forest
    if forest_scenario():
        # Scenario 2: Cave
        if cave_scenario():
            conclusion()

if __name__ == "__main__":
    play_game()
