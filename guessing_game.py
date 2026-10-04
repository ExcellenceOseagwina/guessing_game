# Guess Game variables
secret_number = 10
guess_limit = 5
guess_count = 0

while guess_count < guess_limit:
                 # Enter Secret Number
                 guess = int(input("Guess the Secret Number: "))
                 guess_count += 1
                 if guess == secret_number:
                                  print(f"Congratulations!, You won.\n You Guessed the number  correctly after {guess_count} trials")
                                  break
else:
                 print(f"Sorry, You failed after {guess_count} trials.\n Try again.")