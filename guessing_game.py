# print ("Welcome to Ayush's game 🎮")
# Learned: while loops, input validation, game logic
import random 
print ("Welcome to Ayush's Game 🎮")
print("I picked a number from 1 to 100")
print("Type q to quit, r to restart.\n")

secret = random.randint(1,100)
attempts = 0
MAX_ATTEMPTS = 7

while True:
    user_input = input("Your guess: ").strip().lower()
    if user_input ==  "q":
        print("Goodbye 👋")
        break
    if user_input == "r":
        secret = random.randint(1, 100)
        attempts = 0
        print("\nNew number picked. let's go.\n")
        continue
    if not user_input.isdigit():
        print("Enter a whole number (1-100), or q/r.")
        continue 
    
    guess = int(user_input)

    if guess < 1 or guess > 100:
        print("Out of range. Guess 1-100.")
        continue

    attempts += 1
    if attempts >= MAX_ATTEMPTS:
        print(f"You ran out of attempts 💀 The number was {secret}.")
        secret = random.randint(1,100)
        attempts = 0
        print("\\nNew number picked. Try again.\\ ")
        print(f"Attempts left: {MAX_ATTEMPTS - attempts}")
        continue
    
    if guess < secret:
        print("Too Low.")
    elif guess > secret:
        print("Too High.")
    else:
        print(f"You got it in {attempts} tries 🔥")
        # auto restart
        secret = random.randint(1, 100)
        attempts = 0
        print("\nNew number picked. Try again.\n")
