'''
This program will help the user win at games such as blackjack, poker, etc.
by analyzing charts that offer the probability of success from the user's input of the table setting.
'''

dealerCard_column = {
    '2': 0,
    '3': 1,
    '4': 2,
    '5': 3,
    '6': 4,
    '7': 5,
    '8': 6,
    '9': 7,
    '10': 8,
    'A': 9
}

pairCard_row = {            # Rows used when they have a pair
    'A': 17,
    '2': 18,
    '3': 19,
    '4': 20,
    '5': 21,
    '6': 22,
    '7': 23,
    '8': 24,
    '9': 25,
    '10': 26
}

cardW_A_row = {  # 10-16 rows = A
    '10': 10,
    '9': 10,
    '8': 10,
    '7': 11,
    '6': 12,
    '5': 13,
    '4': 14,
    '3': 15,
    '2': 16
}

cardN_row = {  # 0-9 rows for cards that don't match and don't have an Ace
    '19': 0,
    '18': 0,
    '17': 0,
    '16': 1,
    '15': 2,
    '14': 3,
    '13': 4,
    '12': 5,
    '11': 6,
    '10': 7,
    '9': 8,
    '8': 9,
    '7': 9,
    '6': 9,
    '5': 9
}

table = [
        ["STAND", "STAND", "STAND", "STAND", "STAND", "STAND", "STAND", "STAND", "STAND", "STAND"],
        ["STAND", "STAND", "STAND", "STAND", "STAND", "HIT", "HIT", "HIT", "HIT", "HIT"],
        ["STAND", "STAND", "STAND", "STAND", "STAND", "HIT", "HIT", "HIT", "HIT", "HIT"],
        ["STAND", "STAND", "STAND", "STAND", "STAND", "HIT", "HIT", "HIT", "HIT", "HIT"],
        ["STAND", "STAND", "STAND", "STAND", "STAND", "HIT", "HIT", "HIT", "HIT", "HIT"],
        ["HIT", "HIT", "STAND", "STAND", "STAND", "HIT", "HIT", "HIT", "HIT", "HIT"],#LINE 12
        ["DOUBLE", "DOUBLE", "DOUBLE", "DOUBLE", "DOUBLE", "DOUBLE", "DOUBLE", "DOUBLE", "DOUBLE", "HIT"],#line 11 on chart 
        ["DOUBLE", "DOUBLE", "DOUBLE", "DOUBLE", "DOUBLE", "DOUBLE", "DOUBLE", "DOUBLE", "HIT", "HIT"],# 10
        ["HIT", "DOUBLE", "DOUBLE", "DOUBLE", "HIT", "HIT", "HIT", "HIT", "HIT", "HIT"],#9
        ["HIT", "HIT", "HIT", "HIT", "HIT", "HIT", "HIT", "HIT", "HIT", "HIT"],# Line 5-8
        ["STAND", "STAND", "STAND", "STAND", "STAND", "STAND", "STAND", "STAND", "STAND", "STAND"],#line A 5-8
        ["STAND", "DOUBLE", "DOUBLE", "DOUBLE", "DOUBLE", "STAND", "STAND", "HIT", "HIT", "HIT"],# A 7
        ["HIT", "DOUBLE", "DOUBLE", "DOUBLE", "DOUBLE", "HIT", "HIT", "HIT", "HIT", "HIT"],#LINE A 6
        ["HIT", "HIT", "DOUBLE", "DOUBLE", "DOUBLE", "HIT", "HIT", "HIT", "HIT", "HIT"],# A 5
        ["HIT", "HIT", "DOUBLE", "DOUBLE", "DOUBLE", "HIT", "HIT", "HIT", "HIT", "HIT"],# A 4
        ["HIT", "HIT", "HIT", "DOUBLE", "DOUBLE", "HIT", "HIT", "HIT", "HIT", "HIT"],# A 3
        ["HIT", "HIT", "HIT", "DOUBLE", "DOUBLE", "HIT", "HIT", "HIT", "HIT", "HIT"],#A 2
        ["SPLIT", "SPLIT", "SPLIT", "SPLIT", "SPLIT", "SPLIT", "SPLIT", "SPLIT", "SPLIT", "SPLIT"],# A A
        ["SPLIT", "SPLIT", "SPLIT", "SPLIT", "SPLIT", "SPLIT", "SPLIT", "SPLIT", "SPLIT", "SPLIT"],# 8 8
        ["STAND", "STAND", "STAND", "STAND", "STAND", "STAND", "STAND", "STAND", "STAND", "STAND"],#10 10
        ["SPLIT", "SPLIT", "SPLIT", "SPLIT", "SPLIT", "STAND", "SPLIT", "SPLIT", "STAND", "STAND"],# 9 9
        ["SPLIT", "SPLIT", "SPLIT", "SPLIT", "SPLIT", "SPLIT", "HIT", "HIT", "HIT", "HIT"],# 7 7 ,We already did 8 8 above
        ["SPLIT", "SPLIT", "SPLIT", "SPLIT", "SPLIT", "HIT", "HIT", "HIT", "HIT", "HIT"],# 6 6
        ["DOUBLE", "DOUBLE", "DOUBLE", "DOUBLE", "DOUBLE", "DOUBLE", "DOUBLE", "DOUBLE", "HIT", "HIT"],#5 5
        ["HIT", "HIT", "HIT", "SPLIT", "SPLIT", "HIT", "HIT", "HIT", "HIT", "HIT"],#4 4
        ["SPLIT", "SPLIT", "SPLIT", "SPLIT", "SPLIT", "SPLIT", "HIT", "HIT", "HIT", "HIT"],# 3 3
        ["SPLIT", "SPLIT", "SPLIT", "SPLIT", "SPLIT", "SPLIT", "HIT", "HIT", "HIT", "HIT"],#2 2

    ];
    
    
    
print('''This program's goal is to help the player win their current game of blackjack.
Its purpose is solely to win and NOT gamble. The responses might not align with what common gamblers will think.
The cards J, Q, K are to be entered as values of 10, not their symbols.
''')


userInput = input("Do you have a pair? (yes or no): ").lower()

if userInput == 'yes':
    print("Great, you have a pair")
    cards = input("Enter the value you have for both cards: ")
    dealerCard = input("Enter a value for the Dealer card: ").strip()
    print("Both cards have a value of:", cards)

    # Check if the input values are in the dictionaries
    if cards in pairCard_row and dealerCard in dealerCard_column:
        row_index = pairCard_row[cards]
        col_index = dealerCard_column[dealerCard]

        # Access the cell in the table
        cell_value = table[row_index][col_index]

        print(f"The suggested move for your pair ({cards}) against the dealer's {dealerCard} is to: {cell_value}")
        print(f"Row: {row_index}, Column: {col_index}")  # Use for debugging

    else:
        print("Invalid input values. Please enter valid card values.")

elif userInput == 'no':
    userInput = input("Is one of your cards an Ace? (yes or no): ").lower()

    if userInput == 'yes':
        print("You have an Ace in one of your cards")
        non_ace_card = input("Enter the card you have that's not the Ace: ")
        dealerCard = input("Enter the value of the dealer's up card: ").strip()
        print(f"Your hand is A: {non_ace_card}")

        # Start of checking for card values
        if non_ace_card in cardW_A_row and dealerCard in dealerCard_column:
            row_index = cardW_A_row[non_ace_card]
            col_index = dealerCard_column[dealerCard]

            # Access the cell in the table
            cell_value = table[row_index][col_index]

            print(f"The suggested move for your hand A:({non_ace_card}) against the dealer's {dealerCard} is to: {cell_value}")
            print(f"Row: {row_index}, Column: {col_index}")  # Use for debugging
    elif userInput == 'no':
        cards = input("Enter the sum of your cards")
        dealerCard = input("Enter the value for the Dealers card: ").strip()
        print(f"Your hand total is: {cards}")
        
        #start checking for cards value 
        if cards in cardN_row and dealerCard in dealerCard_column:
            row_index = cardN_row[cards]
            col_index = dealerCard_column[dealerCard]
            #access cell in table
            cell_value = table[row_index][col_index]
            
            print(f"The suggested move for your hand:({cards}) against the dealer's {dealerCard} is to: {cell_value}")
            print(f"Row:{row_index}, Column: {col_index}")#shows you what cell was selected
        
        
        
    else:
        print("error invalid input")

else:
    print("Error: Invalid answer")

    