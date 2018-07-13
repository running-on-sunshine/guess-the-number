# ============================== STEP 1 ================================
# secret_number = 5

# print "I am thinking of a number between 1 and 10."

# guess = int(raw_input("What's the number? "))

# while guess != secret_number:
#     print "Nope, try again!"
#     guess = int(raw_input("What's the number? "))
#     if guess == secret_number:
#         print "Yes! You win!"

# ====================== STEP 1 (ALTERNATE SOLUTION) ====================
# secret_number = 5

# print "I am thinking of a number between 1 and 10."

# while True:
#     guess = int(raw_input("What's the number? "))
#     if guess == secret_number:
#         print "Yes! You win!"
#         break
#     else:
#         print "Nope, try again."
        
# ============================== STEP 2 ================================
# secret_number = 5

# print "I am thinking of a number between 1 and 10."

# while True:
#     guess = int(raw_input("What's the number? "))
#     if guess == secret_number:
#         print "Yes! You win!"
#         break
#     elif guess > secret_number:
#         print "%s is too high." % str(guess)
#     elif guess < secret_number:
#         print "%s is too low." % str(guess)

# ============================== STEP 3 ================================
# import random
# my_random_number = random.randint(1, 10)
# secret_number = my_random_number

# print "I am thinking of a number between 1 and 10 (inclusive)."

# while True:
#     guess = int(raw_input("What's the number? "))
#     if guess == secret_number:
#         print "Yes! You win!"
#         break
#     elif guess > secret_number:
#         print "%s is too high." % str(guess)
#     elif guess < secret_number:
#         print "%s is too low." % str(guess)

# ============================== STEP 4 ================================
# import random
# my_random_number = random.randint(1, 10)
# secret_number = my_random_number
# guesses_left = 5
# print "I am thinking of a number between 1 and 10 (inclusive)."
# print "You have 5 guesses left."

# while guesses_left > 0:
#     guesses_left -= 1
#     guess = int(raw_input("What's the number? "))
#     if guess == secret_number:
#         print "Yes! You win!"
#         break
#     elif guess > secret_number:
#         print "%d is too high." % guess
#         if guesses_left == 0:
#             print "You ran out of guesses."
#         else:
#             print "You have %d guesses left." % guesses_left
#     elif guess < secret_number:
#         print "%d is too low." % guess
#         if guesses_left == 0:
#             print "You ran out of guesses."
#         else:
#             print "You have %d guesses left." % guesses_left
    
# ============================== BONUS: PLAY AGAIN ================================
# import random
# my_random_number = random.randint(1, 10)
# secret_number = my_random_number
# guesses_left = 5
# print "I am thinking of a number between 1 and 10 (inclusive)."
# print "You have 5 guesses left."

# while guesses_left > 0:
#     guesses_left -= 1
#     guess = int(raw_input("What's the number? "))
#     if guess == secret_number:
#         print "Yes! You win!"
#         play_again = raw_input("Do you want to play again (Y or N)? " )
#         if play_again == "Y":
#             guesses_left = 5
#         else:
#             print "Bye!"
#             break
#     elif guess > secret_number:
#         print "%d is too high." % guess
#         if guesses_left == 0:
#             print "You ran out of guesses."
#             play_again = raw_input("Do you want to play again (Y or N)? " )
#             if play_again == "Y":
#                 guesses_left = 5
#             else:
#                 print "Bye!"
#         else:
#             print "You have %d guesses left." % guesses_left
#     elif guess < secret_number:
#         print "%d is too low." % guess
#         if guesses_left == 0:
#             print "You ran out of guesses."
#             play_again = raw_input("Do you want to play again (Y or N)? " )
#             if play_again == "Y":
#                 guesses_left = 5
#             else:
#                 print "Bye!"
#         else:
#             print "You have %d guesses left." % guesses_left

# ====================== BONUS: PLAY AGAIN (FUNCTIONS) ================================
import random
my_random_number = random.randint(1, 10)

print "I am thinking of a number between 1 and 10 (inclusive)."
print "You have 5 guesses left."

secret_number = my_random_number
guesses_left = 5

def play_again():
    play_again = raw_input("Do you want to play again (Y or N)? " )
    if play_again == "Y":
        guesses_left = 5
    else:
        print "Bye!"

def no_more_guesses():
    if guesses_left == 0:
        print "You ran out of guesses."
        play_again()
    else:
        print "You have %d guesses left." % guesses_left
    
while guesses_left > 0:
    guesses_left -= 1
    guess = int(raw_input("What's the number? "))
    if guess == secret_number:
        print "Yes! You win!"
        play_again()
    elif guess > secret_number:
        print "%d is too high." % guess
        no_more_guesses()
    elif guess < secret_number:
        print "%d is too low." % guess
        no_more_guesses()