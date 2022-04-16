# RULES:
#   Try to get as close to 21 without going over.
#   Kings, Queens, Jacks worth 10 points.
#   Aces worth 1 or 11 points.
#   Cards 2 through 10 are worth their face value
#   (H)it to take another card.
#   (S)tand to stop taking cards.
#   On your first play, you can (D)ouble-down to increase your bet but must hit exactly one more time
#   before standing.
#   In case of a tie, the bet is returned to the player.
#   The dealer stops hitting at 17.

import random, sys

#Set up the constants
HEARTS = chr(9829)
DIAMONDS = chr(9830)
SPADES = chr(9824)
CLUBS = chr(9827)

def main():
    print("Welcome to Blackjack - PyTerminal Edition")

    money = 2000
    while True:
        #Check if player has run out of money
        if money <= 0:
            print("You're broke!")
            print("Good thing you weren't playing with real money.")
            print("Thanks for playing!")
            sys.exit()
        
        #Player to enter their bet for this round
        bet = getBet(money)


def getBet(maxBet):
    """Ask the player how much they want to bet for this round."""
    while True: #keep asking until they enter a valid amount
        print('How much do you bet? (1-{}, or QUIT)'.format(maxBet))
        bet = input('> ').upper().strip()
        
        if bet == 'QUIT':
            print("Thanks for playing!")
            sys.exit()
        
        if not bet.isdecimal():
            continue #if the player didn't enter a number, ask again
        
        bet = int(bet)
        if 1 <= bet <= maxBet:
            return bet
        
        print("You don't have enough money!")



if __name__ == "__main__":
        main()