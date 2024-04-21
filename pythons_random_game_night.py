# Pythons Random Game Night
# Random Choice Game 4 Task 1

# Objective

# The Aim of this assignment is to explore the random package in Python and understand
# how it can be used with loops to introuce randomness into your programs.

import random
car_makers = ['Jeep', 'Hummer', 'Tesla', 'Chevy', 'Ford']

selected_car_maker = random.choice(car_makers)
user_guess = input('Guess which car was selected: ')

if user_guess.lower() == selected_car_maker.lower():
  print(f'You guessed correctly. The selected car maker was {selected_car_maker}!')
else:
  print(f'Sorry, your guess was wrong. The selected car maker was {selected_car_maker}.')