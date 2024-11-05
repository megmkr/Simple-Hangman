import random
import maskpass
# import getpass 

#blanks = "_ " * len(word) 
HANGMAN = (
"""
-----
|   |
|
|
|
|
|
|
|
--------
""",
"""
-----
|   |
|   0
|
|
|
|
|
|
--------
""",
"""
-----
|   |
|   0
|  -+-
|
|
|
|
|
--------
""",
"""
-----
|   |
|   0
| /-+-
|
|
|
|
|
--------
""",
"""
-----
|   |
|   0
| /-+-\ 
|
|
|
|
|
--------
""",
"""
-----
|   |
|   0
| /-+-\ 
|   | 
|
|
|
|
--------
""",
"""
-----
|   |
|   0
| /-+-\ 
|   | 
|   | 
|
|
|
--------
""",
"""
-----
|   |
|   0
| /-+-\ 
|   | 
|   | 
|  |
|
|
--------
""",
"""
-----
|   |
|   0
| /-+-\ 
|   | 
|   | 
|  | 
|  | 
|
--------
""",
"""
-----
|   |
|   0
| /-+-\ 
|   | 
|   | 
|  | | 
|  | 
|
--------
""",
"""
-----
|   |
|   0
| /-+-\ 
|   | 
|   | 
|  | | 
|  | | 
|
--------
""")
blanks = []

def print_blanks():
    blank_word = ""
    for character in blanks:
        blank_word += character + " "
    print(blank_word)

def main():
    print("Welcome to hangman! \n\nMake your selection:")
    selection = input("A. Input Custom Word\nB. Random Word\n")

    if(selection == "b"):
        word_list = ["hello", "apple", "bean", "happy"]
        word = random.choice(word_list)
    else:
        word = maskpass.askpass("Enter your custom word: ")
        #word = getpass.getpass("Enter your custom word: ")

    print("Your word is chosen! Let's play the game")

    for character in word:
        blanks.append("_")

    tries = 10
    guessed_letters = []
    while (tries > 0):
        print(HANGMAN[10-tries])
        print_blanks()
        print() # for aesthetics

        guess = input("Guess a letter: ")
        guessed_letters.append(guess)
        
        temp = 0 
        wrong = True
        for i in word:
            if guess == i:
                blanks[temp] = guess
                wrong = False
            temp+=1

        if wrong == True:
            tries-=1

        print("Guessed letters: ", guessed_letters)
        print("Tries remaining: ", tries)

        if "_" not in blanks: 
            break   

    if "_" not in blanks:
        print("You guessed the word!")
    else:
        print("You lose :(") 
        print(HANGMAN[10]) 

if __name__ == "__main__":
    main()