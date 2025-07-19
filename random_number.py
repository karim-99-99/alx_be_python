# import random
# from unittest import case
# secret_number = random.randint(1, 10)
# guess = int(input("Guess a number between 1 and 10: "))
# match guess:
#     case secret_number == guess:
#         print("Congratulations! You guessed the correct number.")
#     case secret_number < guess:
#             print("Too high! Try again.")
#     case secret_number > guess:
#             print("Too low! Try again.")

rows = 5
col = 5
for i in range(1, rows):
  # Outer loop controls the number of rows
  for j in range(1, i*3 , step=1):
    # Inner loop prints asterisks for each row
    print("*", end="")
  print()