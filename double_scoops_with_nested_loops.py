# Double Scoop with Nested Loops 2 Task 1

# Objective
# The aim of this assignment is to practicce sing nested loops in Python.abs# You will   # correct a nested loop cde sippet, simulate a mood tracker, and generate a multiplcation
# table.  

# Simulate a mood tracker that records your mood at three different time of the day
# (morning, afternoon, evening) for each day of the week. Use nested loops to 
# implement this: the outer loop should iterate over the days, and the inner loop
# should iterate over the times of the day. For each time, randomlly select a mood from
# a predefined list and print it. 

days_of_week = ['Monday', 'Tuesday', 'Wednesday', 'Thurday', 'Friday', 'Saturday', 'Sunday']
times_of_day = ['Morning', 'Afternoon', "Evening"]
moods = ['Happy', 'Sad', 'Energetic', 'Calm' ]
import random

for day in days_of_week:
  for time in times_of_day:
    mood = random.choice(moods)
    print(f'On {day}, in the {time}, you felt {mood}!')
    
    