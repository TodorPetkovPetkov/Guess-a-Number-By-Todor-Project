import random
nooftries = 3
maxn = 15
verification = 0
n = random.randint(1, maxn)
print('Welcome to guess the number game!')
print('Guess the number from 1 to %d.' % maxn)
print ()
guess = None
while (nooftries != 0):
    guess = int(input('Your try: '))
    nooftries -= 1
    if guess > n:
        print('Your input is higher than the number.')
        print ()
        print('You have %a chance(s) left.' % nooftries)
    if guess < n:
        print('Your input is lower than the number.')
        print ()
        print('You have %a chance(s) left.' % nooftries)
    if (guess == n):
        verification += 1
        break
if (verification == 1):
    print('Congratulations, you won!')
if (verification == 0):
    print('Oops, seems like you are not lucky this time!')
    print('It was %a.' % n)