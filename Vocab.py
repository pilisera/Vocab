from Flashcard import Flashcard
import random

""" Constants """
keep_order_string = "Keep Order"
flashcard_mode_string = "Flashcard Mode"

def main():
    keep_order = load_options()
    
    while(True):
        # Ask whether the program should run as-is, or whether options should be 
        # altered
        choices = ['R', 'O', 'E'];
        out = '(R)un, (O)ptions, (E)xit?'
        
        print(out)
        inp = raw_input()
        while(inp not in choices):
            print ''.join(["Please enter one of: ", choices[0], ", ", choices[1], ", ", choices[2]])
            print(out)
            inp = raw_input()
        
        if (inp.upper() == 'R'):
            run(keep_order)
        elif (inp.upper() == 'O'):
            print("Keep order? (Y/N)")
            inp = raw_input()
            if (inp.upper() == 'Y'):
                print("no longer shuffling")
                keep_order = True
            elif (inp.upper() == 'N'):
                print("no longer keeping order")
                keep_order = False
                print(keep_order)
            else:
                print("no change")

            print("Which side comes first? (0/1/R)")
            inp = raw_input()
            if (inp == '0'):
                print("showing side 0 first")
                Flashcard.mode = 0
            elif (inp == '1'):
                print("showing side 1 first")
                Flashcard.mode = 1
            elif (inp.upper() == 'R'):
                print("randomly showing either side first")
                Flashcard.mode = None
            else:
                print("no change")

            save_options(keep_order)

        elif (inp.upper() == 'E'):
            return
        

""" Run the quiz! """
def run(keep_order):
    cardlist = setup_cardlist(keep_order)
    
    # Start the quiz
    quiz(cardlist)

    # Check if the user guessed everything correctly
    while not check_perfect(cardlist):
        # If not, rearrange it a bit
        if not keep_order:
            random.shuffle(cardlist)
        # And requiz
        quiz(cardlist)
    
    print('You finished!')

""" Loads in the options, returns ones that are not class variables. """
def load_options():
    optfile = open("options.txt", 'r')
    lines = optfile.readlines()
    for line in lines:
        words = line.split(": ")
        strip(words)
        if words[0].upper() == keep_order_string.upper():
            keep_order = (words[1] == "True")
        elif words[0].upper() == flashcard_mode_string.upper():
            if words[1].isdigit():
                Flashcard.mode = int(words[1])
            else:
                Flashcard.mode = None
    
    optfile.close()

    return keep_order

""" Defines the cardlist. """
def setup_cardlist(keep_order):
    cardlist = list()

    dictfile = open("dictionary.txt", 'r')
    lines = dictfile.readlines()
    for line in lines:
        words = line.split('=')
        strip(words)
        cardlist.append(Flashcard(words))

    # Rearrange the list
    if not keep_order:
        random.shuffle(cardlist)

    return cardlist

def strip(words):
    for i in range(len(words)):
        words[i] = words[i].strip()

""" Asks the user to guess the opposite side of each card. """
def quiz(cardlist):
    for card in cardlist:
        if not card.correct:
            card.guess()

""" Checks if every card in the list has been answered correctly """
def check_perfect(cardlist):
    for card in cardlist:
        if not card.correct:
            return False
    return True

def save_options(keep_order):
    optfile = open("options.txt", 'w')
    optfile.write(''.join([keep_order_string, ": ", str(keep_order), "\n"]))
    optfile.write(''.join([flashcard_mode_string, ": ", str(Flashcard.mode), "\n"]))
    optfile.close()

if __name__ == '__main__':
    main()
