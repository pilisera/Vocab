import random

""" Represents a Flashcard
Has a front 'German' side, and a back 'English' side, given as a list of two 
(or more) strings. Any extra elements are ignored, and no errors are thrown if 
they are not strings (although the guessing will always be wrong).

Handles guessing the value of the opposite side of the card from the console.

Also stores whether or not the card has been guessed correctly already.

"""
class Flashcard:	
    def __init__(self, words):
        # Grab the first two elements of the list
        self.words = words[0:2]
        self.correct = False

	""" Has the user guess the other side of the card from the console. """
    def guess(self):
        # Define the clue and answer based on the mode
        if Flashcard.mode is None:
            n = random.randint(0, 1)
        else:
            n = Flashcard.mode
        
        clue = self.words[n]
        answer = self.words[(n + 1) % 2]
        
        # Interact with user
        print(clue)
        response = raw_input()

        # React to user
        if response == answer:
            print('Match!')
            self.correct = True
        else:
            print(''.join(['Does Not Match, other side is: ', answer]))

        # Extra line to look nice
        print(' ')
