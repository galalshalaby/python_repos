def encryption_wordes( word , number):
 import string
 alphabet = string.ascii_lowercase
 encryption_word = ""

# Loop through each letter in the word
 for letter in word:
     if letter.lower() in alphabet :
    # Find the original position of the letter
      original_position = alphabet.index(letter.lower())
    
    # Calculate the new position (shifted by 2)
      new_position = (original_position +number ) % len(alphabet)
      if letter.isupper():
        encryption_word = encryption_word.upper()
    
    # Add the new letter to the encrypted word
      encryption_word += alphabet[new_position]
     else:
      encryption_word += letter
    

 print("Encrypted word:", encryption_word)


word = input("Please type a word: \n").lower()
shifte_number=int(input("Enter a Shifet number :\n "))


encryption_wordes(word,shifte_number)
