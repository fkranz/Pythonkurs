gallows = ['\n\n\n\n\n--------\n', \
'\n      |\n      |\n      |\n      |\n--------\n', \
'  _____\n      |\n      |\n      |\n      |\n--------\n', \
'  _____\n     \|\n      |\n      |\n      |\n--------\n', \
'  _____\n  |  \|\n      |\n      |\n      |\n--------\n', \
'  _____\n  |  \|\n  O   |\n      |\n      |\n--------\n', \
'  _____\n  |  \|\n  O   |\n  Y   |\n      |\n--------\n', \
'  _____\n  |  \|\n  O   |\n  Y   |\n  ^   |\n--------\n']

#function for guessing one word
def guess_word(word):
        word = word.replace("\n","")
        word = word.upper()
        number = len(word)
        show = ["_"]*number
        wrong = 0
        right = 0
        letters = []
        while wrong < len(gallows)-1:
            print(gallows[wrong])
            print(" ".join(show), "\t \t Used letters:", letters)
            letter = input("Please enter one letter: ")
            if len(letter) > 1: 
                print("ONE letter!")
                continue
            if not letter.isalpha(): 
                print("one LETTER!")
                continue
            letter = letter.upper()
            if letter not in letters:
                letters.append(letter)
                if letter not in word:
                    wrong += 1
                else:
                    for pos,item in enumerate(word):
                        if(item == letter):
                            right += 1
                            show[pos] = letter
            if right == number:
                print("SUCCESS!!!")
                break
        else:
            print(gallows[len(gallows)-1])
            print("Oh noes, you died!! :(")
            print("The correct word was:", word)

#function for asking if user want to play again
def play_again():
    again = input("Play a new word? (Y/n) ")
    again = again.upper()
    if again == "N": return False
    else: return True


#main part of the program
filename = input("Welcome to Hangman, please enter a file, with some words to guess: ")
with open(filename, "r") as f:
    for word in f:
        guess_word(word)
        if play_again() == False: break

    else:
        print("I ran out of words!")
