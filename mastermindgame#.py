import random

# List of fruits to choose from
Fruits = ["apple", "banana", "grape", "orange", "mango"]

class MastermindGame:
    def __init__(self):
        self.secret_code = self.generate_code()
        self.attempts = 0
        self.attempts_max = 5
        self.guesses = []

 #Generate a random secret code consisting of 5 fruits.
    def generate_code(self):
        return random.sample(Fruits, 5)
    
 # Check how many fruits are correct in terms of color and position.
    def check_feedback(self, guess):
        correct_position = sum([1 for i in range(5) if guess[i] == self.secret_code[i]])
        correct_color = sum([min(guess.count(color), self.secret_code.count(color)) for color in Fruits]) - correct_position
        
        if correct_position == 5:
            return "Correct! You have guessed the code."
        else:
            return f"{correct_position} correct in position, {correct_color} correct color but wrong position"
        
 # Main game loop."""
    def play_game(self):
        print("WELCOME TO MASTERMIND! TRY TO GUESS THE SECRET CODE.")
        print("THE CODE CONSISTS OF 5 FRUITS FROM THE FOLLOWING LIST:")
        print(", ".join(Fruits))
        
        while self.attempts < self.attempts_max:
            print(f"\nAttempt {self.attempts + 1} of {self.attempts_max}")
            guess = input("ENTER YOUR GUESS (5 FRUITS SEPERATED BY SPACES): ").split()

# Check if the guess has exactly 5 fruits
            if len(guess) != 5:
                print("INVALID GUESS! PLEASE ENTER EXACTLY 5 FRUITS.")
                continue

            self.attempts += 1
            feedback = self.check_feedback(guess)
            print(f"Feedback: {feedback}")

            if feedback == "CORRECT! YOU HAVE GUESSED THE CODE.":
                print(f"CONGRATULATIONS! YOU GUESSED THE CODE IN {self.attempts} ATTEMPTS.")
                break
        else:
            print(f"\nGAME OVER! YOU'VE USED ALL {self.attempts_max} ATTEMPTS.")
            print(f"THE CORRECT CODE WAS: {', '.join(self.secret_code)}")

# To play the game
if __name__ == "__main__":
    game = MastermindGame()
    game.play_game()
