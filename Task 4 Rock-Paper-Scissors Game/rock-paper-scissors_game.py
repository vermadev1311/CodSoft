import random

def get_computer_choice():
    return random.choice(["rock", "paper", "scissors"])

def get_user_choice():
    choice = input("Enter your choice (rock, paper, scissors): ").lower()
    if choice in ["rock", "paper", "scissors"]:
        return choice
    else:
        print("❌ Invalid choice. Please try again.")
        return get_user_choice()

def determine_winner(user, computer):
    if user == computer:
        return "It's a tie!"
    elif (user == "rock" and computer == "scissors") or \
         (user == "scissors" and computer == "paper") or \
         (user == "paper" and computer == "rock"):
        return "🎉 You win!"
    else:
        return "😔 You lose."

def play_game():
    user_score = 0
    computer_score = 0

    while True:
        print("\n=== Rock-Paper-Scissors Game ===")
        user = get_user_choice()
        computer = get_computer_choice()
        print(f"🧑 You chose: {user}")
        print(f"💻 Computer chose: {computer}")

        result = determine_winner(user, computer)
        print(f"🏁 Result: {result}")

        if "win" in result:
            user_score += 1
        elif "lose" in result:
            computer_score += 1

        print(f"\n📊 Scores → You: {user_score} | Computer: {computer_score}")

        again = input("\nPlay again? (yes/no): ").lower()
        if again != "yes":
            print("👋 Thanks for playing!")
            break

if __name__ == "__main__":
    play_game()
