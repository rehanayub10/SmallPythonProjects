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
BACKSIDE = 'backside'

def main():
    print("Welcome to Blackjack - PyTerminal Edition")

    money = 2000
    while True: #Main game loop

        #Check if player has run out of money
        if money <= 0:
            print("You're broke!")
            print("Good thing you weren't playing with real money.")
            print("Thanks for playing!")
            sys.exit()
        
        #Player to enter their bet for this round
        bet = getBet(money)

        #Give the dealer and the player two cards each
        deck = getDeck()
        dealerHand = [deck.pop(), deck.pop()]
        playerHand = [deck.pop(), deck.pop()]

        #Handle player actions
        print('Bet: ', bet)
        while True: #Keep looping until player stands or busts
            displayHands(playerHand, dealerHand, False)
            print()
            break



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


def getDeck():
    """Return a list of (rank,suit) tuples for all 52 cards."""
    deck = []
    for suit in (HEARTS, DIAMONDS, SPADES, CLUBS):
        for rank in range(2,11):
            deck.append((str(rank), suit)) #Add numbered cards
        for rank in ('J','Q','K','A'):
            deck.append((str(rank), suit)) #Add face and ace cards
    
    random.shuffle(deck)
    return deck

def displayHands(playerHand, dealerHand, showDealerHand):
    """
    Show the player's and dealer's cards. Hide the dealer's first card
    if showDealerHand is false.
    """
    print()
    if showDealerHand:
        print('Dealer: ', getHandValue(dealerHand))
        displayCards(dealerHand)
    else:
        print('Dealer: ???')
        #Hide the dealer's first card
        displayCards([BACKSIDE] + dealerHand[1:])
    
    #Show the player's cards
    print('Player: ', getHandValue(playerHand))
    displayCards(playerHand)


def getHandValue(cards):
    """
    Returns the value of the cards.
    Face cards are worth 10.
    Aces are worth 1 or 11 (this function picks the appropriate value)
    """
    value = 0
    numberOfAces = 0

    for card in cards:
        rank = card[0] #card is a tuple(rank, suit)
        if rank == 'A':
            numberOfAces += 1
        elif rank in ('J','Q','K'):
            value += 10
        else:
            value += int(rank)
    
    #Add the value for the aces
    value += numberOfAces
    for i in range(numberOfAces):
        #If another 10 can be added without busting, do so
        if value + 10 <= 21:
            value += 10
    
    return value

def displayCards(cards):
    """Display all the cards in the cards list."""
    rows = ['','','',''] #the text to display in each row

    for i, card in enumerate(cards):
        rows[0] += " __ " #top line of the card
        if card == BACKSIDE:
            #Print a card's back
            rows[1] += "|## | "
            rows[2] += "|###| "
            rows[3] += "|_##| "
        else:
            #Print the card's front
            rank, suit = card
            rows[1] += "|{} |".format(rank.ljust(2))
            rows[2] += "| {} |".format(suit)
            rows[3] += "|_{}|".format(rank.rjust(2, "_"))
    
    #Print each row on the screen
    for row in rows:
        print(row)



if __name__ == "__main__":
        main()