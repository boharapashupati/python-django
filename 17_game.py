import random
random_number = random.randrange(1,100)
a = 1
while True:
  
  guess_number = int(input("guess any number :"))
  if guess_number== random_number:
   print("congratulation!!!your guess,")
   break
  elif guess_number <random_number:
    print("you guess is smaller ,please guess greater..")
  elif guess_number > random_number:
    print("you guess is greater ,please guess smaller ..")
    
  a = a+1
  if a>5:
    print("sorry ,you have used all your attempts.the correct number was",random_number)




