# Advanced Looping Techniques 6 task 1

# The Selective DJ
# Loop through a lice of the genres list from the previous question and print out the
# genres. Use slicing to create a sublist of genres from the second t the fourth track.

genres = ['Jazz', 'Rock', 'Hip-hop', 'Classical']
full_playlist = ['Free Bird', 'Sister Christian', 'Jump', 'Alive', 'Judith']
#index = 0
print(genres)
print(full_playlist)

for genre in genres[1:2]:
  print(genre)
for tracks in full_playlist[2:4]:
  print(tracks)
  
  print(f'The folowing tracks are {tracks} of the {genre} genre.')

#for index in range(len(genres)):
#  print("Track " + str(index + 1) + ": " + genres[index])

# Advanced Looping Techinqies 6 task 2
# Use a list comprehension to create a new list that contains each genre with the word 
# Music appended to it Print this new list.  

#genres = ['Jazz', 'Rock', 'Hip-Hop', 'Classical']
#result = []
#for genre in genres:
  #result = [genre + ' Music']
  #result.append(genre)
  #print(result)
  
# worked out problem like this so I cold understand
  
genres = ['Jazz', 'Rock', 'Hip-Hop', 'Classical']
result = []
result = [genre + ' Music' for genre in genres]
print(result)

 
# Write a loop using range to print out a countdown from 10 to 1, followed by the message
# The beat drops now!.

nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for nums in range(10, 0, -1):
  print(nums)
print("The beat drops now!")
