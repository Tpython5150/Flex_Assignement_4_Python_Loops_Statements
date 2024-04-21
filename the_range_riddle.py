# The Range Riddle 1 Task 1
 
# Objective
# The aim of this assignment is to deepen your understanding of Python's range()
# function and its applliiation in loops.  You will correct a code snippet, 
# simulate moods for different days, and create a countdown timer.abs


# Write a program that prints off different moods for each day of the week.
# Create a list of mood such as "Happy", "Sad", "Energetlic", and "Calm". 
# Using the range() fpunciton, loop through the days of the week and for each day,
# randomly select a mood from the list and print it.  Ensure that your program includes
# the use of the random module to sleect the mood.

days_of_week = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
moods = ['Happy', 'Sad', 'Energetic', 'Calm']

import random
for day in days_of_week:
  mood = random.choice(moods)
  print(f'{day}: {mood}')
  