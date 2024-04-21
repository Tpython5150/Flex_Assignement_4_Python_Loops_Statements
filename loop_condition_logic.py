# Loop Condition Logic 3 task 1
# Loop Condition Exploration

# Objective

# THe aim of this assignment is to explore the importance of the loop condition in
# while loops. You  will create loops with different conditions to see how they
# influence the behavior of the loop. 

# Write a while  loop with a conditin that will never be false(an infinite loop). 
# Inside the loop, print a statement.  Then, use a break statement to exit the loop after 
# 5 iterations. 

electric_models = ['X', 'Y', '3', 'Tesla Sedan', 'ID4', "EV6", 'Ionic']
#regular_models = ['Toyota', 'Nissan', 'Kia', 'Jeep', 'Honda']
#jeep_model = 0
model = 0
#iterations = 0


while True:
  for car in electric_models:
    print(f"The model being sold: {car}.")
    if car == 'X':
      model += 1
      if model == 4:
        print('One more X to go!')
  if model == 5:
    break
    
  #iterations += 1
  #if iterations == 5:
     

# Loop Conditon Logic 3 Task 2
# Loop conditonal exit
electric_models = ['X', 'Y', '3', 'Tesla Sedan', 'ID4', "EV6", 'Ionic']
model = 0


while model < 5:
  for car in electric_models: 
    print(f"The model being sold: {car}.")
    if car == 'X':
      model += 1
      if  model == 4:
        print('One more X to go!')

          
  
  