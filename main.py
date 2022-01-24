"""
Name(s): Matthew Fields
Name of Project: Wordle
"""
import random
print("Welcome to Worldle. You must guess a five letter word in six tries. \nOn your first guess, you will input a five letter word, and you will be shown with brackets if it is not in the word(()), in the word but in the wrong place ([]), or in the word and in the right place ({}). \nFor example, if you guess 'stare', and recieve (S)(T){A}[R][E], S and T are not in the word, R and E are in the word, but not in those positions, and A is in the word, in the same place as the guess. \nYour incorrect letters will be displayed above each guess. Each guess must have exactly five letters,  with no repeats of letters. This game was created by Josh Wardle. Good luck!")







word1 =["MEATS", "NIGHT", "WATER", "TRAIN", "WEIRD", "PEAKS", "MOVIE", "PROXY", "STAKE", "STAGE", "LIGHT", "FOUND"]

wordnum = random.randint(1,12)

word = word1[wordnum-1]

word = list(word)
end = ''.join(word)
guesses = 0
solve = 0
gray = ['Incorrect Letters:']
while guesses < 6 and solve != 1:
  print(" ")
  right = 0
  print(gray)
  guess = input("Enter Guess: ")
  print(" ")
  while len(guess) != 5:
    guess = input("That is not a five letter word. Please try again: ")
  for wrong in guess:
      while guess.count(wrong) > 1 or len(guess) != 5:
        guess = input("That is not a valid guess. Please reference the rules, then try again: ")
        print(" ")
  guess = guess.upper()
  guess = list(guess)
  check = 0
  for letter in guess:
    word.extend(guess)
    if word.index(letter) == guess.index(letter):
      print("{", end="")
      print(letter, end="") 
      print("}", end="")
      right += 1
    elif word.index(letter) <= 4:
      print("[", end ="")
      print(letter, end ="")
      print("]", end="")
    else:
      print("(", end="")
      print(letter, end="")
      print(")", end="")
      if gray.count(letter) < 1:
        gray.append(letter)
  guesses +=1
  if right == 5:
    print("")
    print("Congratulations. You have won in ", guesses, " guesses. ")
    solve = 1

if guesses == 6 and solve !=1:
  print(" ")
  print("You have lost. The word was ", end, ". Please restart with a different word. ")
#Write the main part of your program here. Use of the other pages is optional.

#import page1  # uncomment if you're using page1
#import page2  # uncomment if you're using page2
#import page3  # uncomment if you're using page3
#import page4  # uncomment if you're using page4
