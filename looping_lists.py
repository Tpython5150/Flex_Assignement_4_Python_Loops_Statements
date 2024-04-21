# Looping List - The Rythm of Repitition
 
# The for Loop DJ Set 5 Task 1
# Objecitve
# Dive into the heart of Python loops with a musica twist. Your task is to explore
# different ways of looping through lists, each with its uniquie style and purpose. 
# By the end of this assignment, you will be able to control your loops like a DJ
# controls the tracks, ensuring each element gets it time to shine.

# Using the provided genres list, write a for loop that prints out each genre with a
# custom message. Extend this task by adding a counter that displays the number of the
# track before the genre. 

genres = ['Jazz', 'Rock', 'Hip-hop', 'Classical']
for genre in genres:
  print("Now playing: " + genre)
  
genres = ['Jazz', 'Rock', 'Hip-hop', 'Classical']
for index in range(len(genres)):
  print("Track " + str(index + 1) + ": " + genres[index] + " - Music time!")

# The Remix Artist 5 task 2  while loop
# Convert the for loop from Task 1 nto a while loop. Ensure performs the same
# function but also includes a condition to stop the loop if a certain genre is
# played for instance hip-hop. 

genres = ['Jazz', 'Rock', 'Hip-hop', 'Classical']
index  = 0
 
while index < len(genres):
  print("Track " + str(index + 1) + ": " + genres[index] + " - Music time! ")
  if genres[index].lower() == 'hip-hop':
    break
  index += 1
  
# Light Show Techincian Loop 5 Task 3
# Using the range() function, looop through the genres list by index. For each
# genre, print out the track number and a message that the light show is ready.
# Modify the loop to skip a genre if its not suitable for the light show, for
# instance Classical genre. 

genres = ['Jazz', 'Rock', 'Hip-hop', 'Classical']
 
for track_number in range(len(genres)):
  genre = genres[track_number]
  if genre.lower()!= 'classical':
    print(f'Track  {track_number + 1}: {genre} - Light show is ready!')