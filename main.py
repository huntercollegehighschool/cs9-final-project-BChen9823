"""
Name(s): Billy Chen
Name of Project: Hangman
"""
import random 

name = input("Welcome to Hangman! Please enter your name: ")
print("Hello,", name)

def round2():
  playagain = input('Do you want to play again? Enter "yes" or "no": ')
  while playagain != "yes" and playagain != "no":
    playagain = input('Do you want to play again? Enter "yes" or "no": ')
  if playagain == "yes":
    game()
  elif playagain == "no":
    exit()

def adding(lis):
  add = 1
  while add == 1:
    addto = input("Please enter a word: ")
    while addto.isalpha() is False:
      print("The word you have entered is not a word.")
      addto = input("Please enter a word: ")
    uappto = addto.upper()
    while uappto in lis:
      print("The word you have entered is already in the list.")
      addto = input("Please enter a different word: ")
      while addto.isalpha() is False:
        print("The word you have entered is not a word.")
        addto = input("Please enter a word: ")
      uappto = addto.upper()
    lis.append(uappto)
    cont = input('Do you want to enter another word? Enter "yes" or "no": ')
    while cont != "yes" and cont != "no":
      cont = input('Please enter "yes" or "no": ')
    if cont == "yes":
      add == 1
    elif cont == "no":
      add = 2

def game():
  print("Which list of words would you like to use? \n 1. Easy \n 2. Medium \n 3. Hard \n 4. Impossible \n 5. Create Your Own")
  choice = input("Enter 1, 2, 3, 4, or 5: ")
  while choice != "1" and choice != "2" and choice != "3" and choice != "4" and choice != "5":
    choice = input("Enter 1, 2, 3, 4, or 5: ")
  if choice == "1":
    from page1 import easy
    words = easy
  elif choice == "2":
    from page1 import medium
    words = medium
  elif choice == "3":
    from page1 import hard
    words = hard
  elif choice == "4":
    from page1 import impossible
    words = impossible
  elif choice == "5":
    from page1 import create
    if len(create) != 0:
      print("Your list currently has words in it.")
      print("Current Custom List:", create)
      clear = input('Would you like to clear your list? Enter "yes" or "no": ')
      while clear != "yes" and clear != "no":
        clear = input ('Please enter "yes" or "no": ')
      if clear == "yes":
        print("Understood. Clearing list.")
        create.clear()
      elif clear == "no":
        print("Understood. Keeping words on list.")
      cont = input('Do you want to enter another word? Enter "yes" or "no": ')
      while cont != "yes" and cont != "no":
        cont = input('Please enter "yes" or "no": ') 
      if cont == "no" and clear == "yes":
        print("Your list has no words in it.")
        adding(create)
      elif cont == "yes":
        adding(create)
    if len(create) == 0:
      adding(create)
    words = create
  guesses = 6
  word = random.choice(words)
  hi = len(word)
  desh = hi * "_"
  print("Word: ",desh)
  print("Guesses Remaining:", guesses)
  wrong = []
  used = []
  play2 = 5
  proof = list(word)
  werd = list(word)
  lest = list(desh)
  def check(a):
    for i in range(len(werd)):
      if werd.count(guess) > 1:
        if werd.index(guess) == i:
          lest.pop(i)
          lest.insert(i, guess)
          werd.pop(i)
          werd.insert(i, 1)
      elif werd.count(guess) == 1:
        if werd.index(guess) == i:
          lest.pop(i)
          lest.insert(i, guess)
    print("Word:",''.join(lest))
  
  def hangman():
    if guesses == 6:
      print("_____________")
      print("  |       \ |")
      print("           \|")
      print("            |")
      print("            |")
      print("            |")
      print("            |")
      print("            |")
      print("            |")
      print("=============")
    elif guesses == 5:
      print("_____________")
      print("  |       \ |")
      print("  O        \|")
      print("            |")
      print("            |")
      print("            |")
      print("            |")
      print("            |")
      print("            |")
      print("=============")
    elif guesses == 4:
      print("_____________")
      print("  |       \ |")
      print("  O        \|")
      print("  |         |")
      print("  |         |")
      print("            |")
      print("            |")
      print("=============")
    elif guesses == 3:
      print("_____________")
      print("  |       \ |")
      print("  O        \|")
      print(" /|         |")
      print("  |         |")
      print("            |")
      print("            |")
      print("=============")
    elif guesses == 2:
      print("_____________")
      print("  |       \ |")
      print("  O        \|")
      print(" /|\        |")
      print("  |         |")
      print("            |")
      print("            |")
      print("=============")
    elif guesses == 1:
      print("_____________")
      print("  |       \ |")
      print("  O        \|")
      print(" /|\        |")
      print("  |         |")
      print(" /          |")
      print("            |")
      print("=============")
    elif guesses == 0:
      print("_____________")
      print("  |       \ |")
      print("  O        \|")
      print(" /|\        |")
      print("  |         |")
      print(" / \        |")
      print("            |")
      print("=============")

  while guesses != 0 and proof != lest and play2 == 5:
    print("")
    hangman()
    print("")
    guess = input("Enter a letter: ")
    guess = guess.upper()
    while guess.isalpha() is False or len(guess) != 1 or guess in used:
      if len(used) > 1:
        used.sort()
      if len(wrong) > 1:
        wrong.sort()
      while guess.isalpha() is False:
        print("")
        print("You have entered an input that is not a letter.")
        print("Word:",''.join(lest))
        print("Past Guesses:", ','.join(used))
        print("Wrong Guesses:",','.join(wrong))
        print("Guesses Remaining: ", guesses)
        print("")
        hangman()
        print("")
        guess = input("Please enter a letter: ")
        guess = guess.upper()
        print()
      while len(guess) != 1:
        print("")
        print("You have entered multiple letters.")
        print("Word:",''.join(lest))
        print("Past Guesses:", ','.join(used))
        print("Wrong Guesses:",','.join(wrong))
        print("Guesses Remaining: ", guesses)
        print("")
        hangman()
        print("")
        guess = input("Please enter a single letter: ")
        guess = guess.upper()
        print()
      while guess in used:
        print("")
        print("You have already entered this letter.")
        print("Word:",''.join(lest))
        print("Past Guesses:", ','.join(used))
        print("Wrong Guesses:",','.join(wrong))
        print("Guesses Remaining: ", guesses)
        print("")
        hangman()
        print("")
        guess = input("Please enter another letter: ")
        guess = guess.upper()
        print()
    if werd.count(guess) == 0 and guess not in used:
      print("The letter IS NOT in the word.")
      guesses = guesses - 1
      wrong.append(guess)
    elif werd.count(guess) != 0 and guess not in used: 
      print("The letter IS in the word.")
    used.append(guess)
    check(guess)
    if len(used) > 1:
      used.sort()
    if len(wrong) > 1:
      wrong.sort()
    print("Past Guesses:", ','.join(used))
    print("Wrong Guesses:",','.join(wrong))
    print("Guesses Remaining: ", guesses)
    if guesses == 0:
      print("Out of guesses. The word was:", word)
      print("")
      hangman()
      print("")
      round2()
    if proof == lest:
      print("You have guessed the word! Good game!")
      round2()
      
game()