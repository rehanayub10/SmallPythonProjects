# A seven-segment number display module

def getSevSegStr(number, minWidth=0):
    """
    Return a seven-segment representation of number inputted by the user.
    Pad with zeros until desired width is reached
    """

    #Convert to str
    number = str(number).zfill(minWidth)

    rows = ['','','']
    for i, digit in enumerate(number):
        if digit == '.': #render the decimal point
            rows[0] += " "
            rows[1] += " "
            rows[2] += "."
        elif digit == '0': #render the digit 0
            rows[0] += " __ "
            rows[1] += "|  |"
            rows[2] += "|__|"
        elif digit == '1': #render the digit 1
            rows[0] += "    "
            rows[1] += "  | "
            rows[2] += "  | "
        elif digit == '2': #render the digit 2
            rows[0] += " __ "
            rows[1] += " __|"
            rows[2] += "|__ "
        elif digit == '3': #render the digit 3
            rows[0] += " __ "
            rows[1] += " __|"
            rows[2] += " __|"
        elif digit == '4': #render the digit 4
            rows[0] += "   "
            rows[1] += "|__|"
            rows[2] += "   |"
        elif digit == '5': #render the digit 5
            rows[0] += " __ "
            rows[1] += "|__"
            rows[2] += " __|"
        elif digit == '6': #render the digit 6
            rows[0] += " __ "
            rows[1] += "|__ "
            rows[2] += "|__|"
        elif digit == '7': #render the digit 7
            rows[0] += " __ "
            rows[1] += "   |"
            rows[2] += "   |"
        elif digit == '8': #render the digit 8
            rows[0] += " __ "
            rows[1] += "|__|"
            rows[2] += "|__|"
        elif digit == '9': #render the digit 9
            rows[0] += " __ "
            rows[1] += "|__|"
            rows[2] += " __|"
        
        if i < len(number) - 1:
            rows[0] += " "
            rows[1] += " "
            rows[2] += " "
        
    return "\n".join(rows)

if __name__ == "__main__":
    print(getSevSegStr(92.8,2))

