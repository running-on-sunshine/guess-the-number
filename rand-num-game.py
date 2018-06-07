from random import randint

def play_game():
    random_number = randint(1, 10)
    guesses_left = 3
    print("Guess the Random Number")
    print("-----------------------")
    print("Try to correctly guess the random number (1 to 10) in 3 tries.")
    while guesses_left > 0:
      guess = int(input("Your guess: "))
      if guess == random_number:
        print("You win!")
        break
      guesses_left -= 1
    else: 
      print("You lose.")
      def replay():
        try_again = raw_input("Try again? (y/n) ")
        if try_again == "y":
          play_game()
        elif try_again == "n":
          print("Thanks for playing!")
        else: 
          print("Sorry, I did not understand your response.")
          replay()
      replay()
    
play_game()
