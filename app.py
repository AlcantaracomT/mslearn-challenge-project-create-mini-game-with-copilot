import random

def user():
    choices = ['rock', 'paper', 'scissors']
    while True:
        user_ch = input("Choose rock, paper or scissors: ").lower()
        if user_ch in choices:
            return user_ch
        else:
            print("Invalid choice")

def computer():
    choices = ['rock', 'paper', 'scissors']
    return random.choice(choices)

def winner(user_ch, computer):
    if user_ch == computer:
        return "A tie"
    elif(user_ch == 'rock' and computer == 'scissor') or  (user_ch == 'paper' and computer == 'rock') or (user_ch == 'scissor' and computer == 'paper'):
        return "Winner"
    else:
        return "Looser"
    
def play():
    user_ch = user()
    computer_ch = computer()
    print(f"You are {user_ch}")
    print(f"The computer is {computer_ch}")
    result = winner(user_ch, computer_ch)
    print(result)

if __name__ == "__main__":
    play()