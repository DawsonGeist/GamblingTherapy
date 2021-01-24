import random
import time
tokens = 100

def getWager():
    print('How much to wager? ' + str(tokens))
    wager = input()
    return wager


while tokens > 0:
    print('Tokens: ' + str(tokens))
    good = False
    while(good != True):
        try:
            wager = getWager()
            wager = int(wager)
            good = True
        except:
            print('Must be a number')
            good = False

    if(wager > tokens):
        print('invalid wager')
        wager = getWager()

    outcome = random.random()
    time.sleep(3)
    if(outcome >= 0.5):
        print('winner! ' + str(outcome))
        tokens += int(wager * (1+outcome))
    else:
        print('loser! ' + str(outcome))
        tokens = tokens - wager