# Sophie Rokosz (01941527)
# Intro to Python Programming (Info2030) w/ Prof Bryant Moscon
# Assignment 3: Mastermind Game

#Purpose: Correctly guess the sequence of four randomly generated colors out of eight total colors.

print('')
print("Welcome to Mastermind!")
print("Enter four, nonrepeating colors from the following list: R G B Y W O M V (ex. RGBY)")
print('')
print("Clues:")
print("White = Correct Color, Correct Position")
print("Red = Correct Color, Incorrect Position")
print("_ = Incorrect Color, Incorrect Position")
print('')

def mastermind():
    legal_colors = ['R', 'G', 'B', 'Y', 'W', 'O', 'M', 'V']
    def generate_color_sequence():
        import random
        random.seed()
        sequence = random.sample(range(len(legal_colors)), 4)
        return [legal_colors[i] for i in sequence]
    colors = generate_color_sequence()
    #print(colors)

    peg_clue = [] #append() fills this list based on player input to give player clues i.e. (White, Red, _)
    guess = ''

    attempts = 5
    start = 0
    while attempts != start:
        peg_clue.clear()  # Clears all elements from peg clue list
        guess = list(input('Enter your guess: '))  # Player input

       #Player input error logic check
        if len(guess) != 4: #invalid input for anything other than 4 characters
            print("Please enter four, nonrepeating colors (ex. RGBY)")
            continue

        isValid = True
        for i, v in enumerate(guess):
            upper_v = v.upper() #reformats all
            if upper_v not in legal_colors: #checks if input is a color within legal colors (checks numbers and letters)
                isValid = False
                print("Please select four, nonrepeating colors from the following list: R G B Y W O M V (ex. RGBY) ")
            if isValid is False: #if error logic does not check, breaks out of for loop to allow restart of while loop below
                break
        if isValid is False:
            continue #if above conditions are not met, restarts while loop without counting attempt

        if isValid is True: #player input passes logic check
            start = start + 1 #start (i.e.) starting attempt increase if guess is valid
            print("Attempt ", start)

        for i, v in enumerate(guess):
            #Peg logic
            upper_v = v.upper()
            if upper_v == colors[i]:
                 peg_clue.append('White') #Clue: correct color, correct position
            elif upper_v in colors:
                peg_clue.append('Red') #Clue: correct color, incorrect position
            else:
                peg_clue.append('_') #Clue: incorrect color, incorrect position
        print(peg_clue) #Peg clue list
        if guess == colors: #if user input matches color sequence & order, wins game
            print('You are the winner!')
            break
        elif attempts == start: #if user has used all allowable guesses, loses game
            print("You lose!")

while True:
    mastermind()
    if input('Play again? (Y/N): ').lower() == 'n': #Default case is play again
        break