import random
from re import M
from typing import final


class Game:
    def __init__(self):
        self.hangman = ['H', 'A', 'N', 'G', 'M', 'A', 'N']
        self.usedLetters = []
        self.chosenWord = []
        self.underscores = []
        self.finalGuess = ''
        self.finalTry = True

    def generateWord(self):
        with open('1-1000.txt', 'r') as f:
            data = f.read().split()
        self.chosenWord = list(random.choice(data))
        f.close()
        wordLength = len(self.chosenWord)
        while len(self.underscores) < wordLength:
            self.underscores.extend("_")
        return

    def checkWholeGuess(self):
        self.finalGuess = input("Please enter your final word guess: ")
        if self.finalGuess == ''.join(self.chosenWord):
            print('You guessed the correct word! You win!')
            main()
        else:
            self.finalTry = False
            print("That was not the correct word! You are unable to guess the full word again during this round.")
            guess(self)

    def checkGuess(self, userGuess):
        if userGuess in self.chosenWord:
            indexes = findIdx(userGuess, self.chosenWord)
            loop = 0
            for idx, x in enumerate(self.underscores):
                if idx in indexes:
                    self.underscores[idx] = userGuess
                    loop += 1
                    if '_' in self.underscores and loop == len(indexes):
                        guess(self)
                elif self.underscores == self.chosenWord:
                    print(f"You win! The word was: {''.join(self.chosenWord)}.")
                    main()
        else:
            print(f"{userGuess} does not exist in the word!") 
            self.usedLetters.append(userGuess)
            if len(self.hangman) == 1:
                print(f"HANGMAN! You lose, the word was: {''.join(self.chosenWord)}.")
                main()
            self.hangman.pop()
            print(self.hangman)
            print("Used Letters: ", self.usedLetters)
            guess(self)
        

def main():
    myObj = Game()
    myObj.generateWord()
    intro(myObj)
    


def guess(myObj):
    print(myObj.underscores)
    userGuess = input("Please type in a letter to guess: ")
    isChar = userGuess.isalpha() 
    isOne = len(userGuess) == 1
    if(userGuess == '3' and myObj.finalTry == True):
        myObj.checkWholeGuess()
    if(isChar == False or isOne == False):
        print("That is an incorrect entry, please use only single, alphabetical entries")
        guess(myObj)
    myObj.checkGuess(userGuess.lower())


def intro(myObj):
    introResponse = input("Hello and welcome to Hangman!\nPress '1' to read the instructions or '2' to continue to the game: ")
    if introResponse == '1':
        print('Rules: The rules are simple, guess the word before Hangman runs out!\nPlayers can only enter single, alphabetical entries. If a player wants a shot at guessing the whole word, enter 3 anytime! Beware however that users are only permitted one whole word guess once per game...')
        intro(myObj)
    elif introResponse == '2':
        guess(myObj)
    else:
        print("That is an incorrect entry")
        intro(myObj) 

def findIdx(userGuess, chosenWord):
        return [i for i in range(len(chosenWord)) if chosenWord[i] == userGuess]


if __name__ == "__main__":
    main()
