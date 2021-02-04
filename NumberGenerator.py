import random

print('Hello! what is your name?')
name = input() 

print('Welcome ' + name + ' I am thinking of a number between 1 and 20')
secretNum = random.randint(1,20)

for guessesTaken in range(1,7):
  print('Take a guess')
  guess = int(input())

  if guess < secretNum:
    print('Your guess is too low')
  elif guess > secretNum:
    print('Your guess is too high')
  else:
    break; #stops loop for either a correct guess or out of guesses

if guess == secretNum:
  print('congratulations ' + name + ' you have guessed my number in ' + str(guessesTaken) + ' guesses!!')
else:
  print('I am sorry to say you did not guess my number which was ' + str(secretNum))