#RocK_Paper_Scissor GAME
#Rules:ROCK wins against Scissors; Scissors wins against Paper;Paper wins against Rock...

import random
users_choice=int(input("Enter your choice: Type 0 for Rock, 1 for Paper, 2 for Scissors"))
if users_choice>=3 or users_choice<0:
 print("You entered invalid number")
else:
 computers_choice=random.randint(0,2)
print("Computer Chose:")
print(computers_choice)
if computers_choice==users_choice:
 print("Its Draw")
elif computers_choice==0 and users_choice==2:
 print("You Lose")
elif users_choice==0 and computers_choice==2:
 print("You Win")
elif computers_choice>users_choice:
 print("You Lose")
elif users_choice>computers_choice:
 print("You Win")