import random
words=["office","panda","cabin","ginger"]
HANGMANPICS = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']

final_resuelt=[]
random_words=random.choice(words)
display=["-"] * len(random_words)
#for letter in random_words :
    # display.append("-")
print('  '.join(display))
print(HANGMANPICS[0])
lives=6
guessed_letters=[]
while "-" in display and lives > 0 :  
 guessed=input("please guess a letter :").lower()
 if guessed in guessed_letters:
    print("you already guesse that . try again.")
    print(f"you have {lives}more tries")
    continue
 guessed_letters.append(guessed)
 if guessed not in random_words:
     lives-= 1 
 for posation in range(len(random_words)):
      if random_words[posation]==guessed:
          display[posation]=guessed
 print(display)
 print(f"you have {lives} mmore tries")
 print('  '.join(display))
 print(HANGMANPICS[6 - lives])  # Show hangman based on lives

# End game result
if lives > 0:
    print("Congratulations, you won!")
else:
    print("Sorry, you lost. The word was:", random_words)
    print(HANGMANPICS[6])
 