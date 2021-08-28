import random

def guess(x):
    random_num=random.randint(1,x)
    guess1=0
    guess1=int(input( f'guess a num between 1 and {x}:' ))
    #print(guess1)
    #print(random_num)
    while(guess1!=random_num):
        if(guess1>random_num):
            print("too big!try again")
            guess1=int(input("guess again:"))
        if(guess1<random_num):
            print("too small!try again")
            guess1=int(input("guess again:"))
        if(guess1==random_num):
            print("found")

def computer_guess(x):
    print(f'think of a number between 1 and {x}:')
    feedback=''
    low=1
    high=x
    while(feedback!='c'):
        if low!=high:
            guess=random.randint(low,high)
        else:
            guess=low
        feedback=input(f'is {guess} too high(H) or too low(L) or correct(C)?').lower()
        if(feedback=='h'):
            high=guess-1
        elif(feedback=='l'):
            low=guess+1
    print(f'yay the computer guessed the correct number,i.e., {guess}')

#guess(100)
computer_guess(50)

        