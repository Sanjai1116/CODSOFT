import random

while True:
    print("\n--- ROCK PAPER SCISSORS ---")
    print("1. Rock")
    print("2. Paper")
    print("3. Scissors")
    print("4. Exit")
    
    user_choice = input("Enter your choice (1-4): ")
    
    if user_choice == "4":
        print("Thanks for playing! Goodbye!")
        break
    
    if user_choice not in ["1", "2", "3"]:
        print("Invalid choice! Try again.")
        continue
    
    choices = {"1": "Rock", "2": "Paper", "3": "Scissors"}
    user = choices[user_choice]
    
    computer_choice = random.choice(["1", "2", "3"])
    computer = choices[computer_choice]
    
    print(f"\nYou chose: {user}")
    print(f"Computer chose: {computer}")
    
    if user_choice == computer_choice:
        print("It's a TIE!")
    elif (user_choice == "1" and computer_choice == "3") or \
         (user_choice == "3" and computer_choice == "2") or \
         (user_choice == "2" and computer_choice == "1"):
        print("You WIN!")
    else:
        print("Computer WINS!")