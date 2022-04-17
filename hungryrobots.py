
#Set up the constants
WIDTH = 20
HEIGHT = 40

WALL = chr(9617) #Unicode sequence
EMPTY_SPACE = ' '

def main():
    print("Welcome to Hungry Robots!") 
    input("Press Enter to begin...\n")

    board = getBoard()
    displayBoard(board)


def getBoard():
    """
    Return a dictionary with board positions.
    Key-value example(s): (20,20) -> WALL, (21,40) -> EMPTY_SPACE
    """
    board = {}
    
    for x in range(WIDTH):
        for y in range(HEIGHT):
            board[(x,y)] = WALL
    
    return board

def displayBoard(board):
    for x in range(WIDTH):
        for y in range(HEIGHT):
            print(board[(x,y)], end='')
        print()


if __name__ == "__main__":
    main()