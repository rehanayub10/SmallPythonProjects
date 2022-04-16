#Nested Loops

#Print the top row
print("   |  0   1   2   3   4   5   6   7   8   9  10  11  12")
print("------------------------------------------------------------")

#Print vertical multipliers
for number1 in range(13):
    print(str(number1).rjust(2), end=' ')
    print("|", end='')

    for number2 in range(13):
        print(str(number1*number2).rjust(3), end=' ')
    
    print()

