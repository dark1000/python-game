import random

guesses_made=0
name=raw_input('hello what is your name?\n')

number=random.randint(1,20)

print 'well,{0},I am thinking of a number between 1~20'.format(name)

while guesses_made < 6:
     guess=int(raw_input('take a guess:'))
     guesses_made+=1

     if guess <number:
         print 'your guess is too low'

     if guess>number:
         print 'your guess is too big'

     if guess==number:
         break

if guess==number:
    print 'good job {0}!,you guess my number in {1} guessed'.format(name,guesses_made)
else:
    print 'sad,the number i want was {0}'.format(number)
    
    
