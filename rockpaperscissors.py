import random

def play():
    player=input("what's your choice? \n rock(r) or paper(p) or scissors(s) \n")
    computer=random.choice(['r','p','s'])

    if(is_win(player,computer)):
        return 'you won!!'
    
    return 'you lostt'

def is_win(user,comp):
    if((user=='p' and comp=='r') or (user=='r' and comp=='s') or (user=='s' and comp=='p')):
        return True;
    else:
        return False;

print(play())