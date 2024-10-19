import random
rock_asci="""
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
        """
paper_asci= """
    _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
        """
sesoric_asci="""
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
        """



print("welcom to the Rock , Paper, Scissors game:\n")
rules=input("Press enter to continue or type (help) for the rules\n").lower()
if rules=="help":
 print("""  help
         *********RULES*********     
      1- You choose and the computer chooses.
      2- Rock smashes scissors -> Rock wins.
      3- Scissors cut paper -> Scissors win.
      4- Paper covers rock -> Paper wins.
     """)
 #user choice
 user_choice=input("enter you choice (rock,paper.scissors)").lower()
 if user_choice not in ["rock","paper","scissors"]:
  print("invaled choice please run the program again and choice rock ,paper ,scissors")
 else:
  if user_choice=="rock":
   print(f"\nyour choic \n{rock_asci}")
  elif user_choice=="paper":
   print(f"\nyour choice\n{paper_asci}")
  else:
   print(f"/nyour choice \n{sesoric_asci}")
#computer choice
computer_choice=random.choice(["rock","paper","scissors"])
if computer_choice=="rock":
   print(f"\ncomputer choic \n{rock_asci}")
elif computer_choice=="paper":
   print(f"\ncomputer choice\n{paper_asci}")
else:
   print(f"\ncomputer choice \n{sesoric_asci}")
# match coice
if (user_choice == 'rock' and computer_choice == 'scissors') or \
       (user_choice == 'scissors' and computer_choice == 'paper') or \
       (user_choice == 'paper' and computer_choice == 'rock'):
        print("You win!")
elif user_choice==computer_choice:      
        print("try again")
else:
       print("you lose !")       


 


