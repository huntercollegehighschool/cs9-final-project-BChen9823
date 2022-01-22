#Use of this page is optional. If you use code here, make sure either import page3 or from page3 import * appear on your main.py page.
def again():
  proof = list(wordz)
  guessess = 10
  wrong = []
  used = []
  werd = list(wordz)
  print("Word: ",desh)
  print("Guesses Remaining:", guessess)
  while guessess != 0 and proof != lest:
    print("")
    guess = input("Enter a capital letter: ")
    if guess in used:
      guess = input("You have already entered this letter. Please enter another letter: ")
    if werd.count(guess) == 0:
      guessess = guessess - 1
      wrong.append(guess)
    used.append(guess)
    check(guess)
    print("Wrong Guesses:",''.join(wrong))
    print("Guesses Remaining: ", guessess)