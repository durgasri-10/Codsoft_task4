import random
def get_computer_choice():
    choices = ['rock', 'paper', 'scissor']
    return random.choice(choices)
def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return 'tie'
    elif (user_choice == 'rock' and computer_choice == 'scissor') or \
         (user_choice == 'scissor' and computer_choice == 'paper') or \
         (user_choice == 'paper' and computer_choice == 'rock'):
        return 'user'
    else:
        return 'computer'
def display_result(user_choice, computer_choice, winner):
    print("\nYou chose: user_choice")
    print("Computer chose: computer_choice")
    if winner == 'tie':
        print("It's a tie!")
    elif winner == 'user':
        print("You win")
    else:
        print("You lose")
def play_again():
    while True:
        again = input("\nDo you want to play another round? (yes/no): ").lower()
        if again in ['yes', 'no']:
            return again == 'yes'
        else:
            print("enter 'yes' or 'no'.")
def main():
    user_score = 0
    computer_score = 0
    print("Welcome to Rock, Paper, Scissor!")
    while True:
        user_choice = input("\nChoose rock, paper, or scissor: ").lower()
        if user_choice not in ['rock', 'paper', 'scissor']:
            print("Invalid choice, please try again.")
            continue
        computer_choice = get_computer_choice()
        winner = determine_winner(user_choice, computer_choice)
        if winner == 'user':
            user_score += 1
        elif winner == 'computer':
            computer_score += 1
        display_result(user_choice, computer_choice, winner)
        print("\nCurrent Score: You user_score - Computer computer_score")
        if not play_again():
            print("\nThanks for playing!")
            break
if __name__ == "__main__":
    main()
