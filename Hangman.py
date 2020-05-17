import random
print("---------This is Hangman Game---------")
print("---------Python Project-3-------------")

def hangman():
    word = random.choice(["dragon","avengers","thor","sniper","tiger","black","criminal","ghost","love","hacking"])
    validLetters = "abcdefghijklmnopqrstuvwxyz"
    turns = 10
    guessmade = ''
    while len(word) > 0:
        main = ""
        missed = 0

        for letter in word:
            if letter in guessmade:
                main = main + letter
            else:
                main = main + "_" + " "

        if main == word:
            print(main)
            print("---------Congrats You are win!!---------")
            print("---------Thanks for Playing-------------")
            break
        print("Guess the word:",main)
        guess = input()

        if guess in validLetters:
            guessmade = guessmade + guess
        else:
            print("Enter a valid character")
            guess = input()

        if guess not in word:
            turns = turns - 1
            if turns == 9:
                print("9 turns left")
                print(" ---------  ")

            if turns == 8:
                print("8 turns left")
                print(" ---------  ")
                print("     O      ")

            if turns == 7:
                print("7 turns left")
                print(" ---------  ")
                print("     O      ")
                print("     |      ")

            if turns == 6:
                print("6 turns left")
                print(" ---------  ")
                print("     O      ")
                print("     |      ")
                print("    /       ")

            if turns == 5:
                print("5 turns left")
                print(" ---------  ")
                print("     O      ")
                print("     |      ")
                print("    / \     ")

            if turns == 4:
                print("4 turns left")
                print(" ---------  ")
                print("   \ O      ")
                print("     |      ")
                print("    / \     ")

            if turns == 3:
                print("3 turns left")
                print(" ---------  ")
                print("   \ O /    ")
                print("     |      ")
                print("    / \     ")

            if turns == 2:
                print("2 turns left")
                print(" ---------  ")
                print("   \ O /|   ")
                print("     |      ")
                print("    / \     ")

            if turns == 1:
                print("1 turns left")
                print("Last Breath Counting, Take care!")
                print(" ---------  ")
                print("   \ O_|/   ")
                print("     |      ")
                print("    / \     ")

            if turns == 0:
                if turns == 0:
                    print("You Loose")
                    print("You let a kind man die")
                    print(" ---------  ")
                    print("     O_|    ")
                    print("   / | \    ")
                    print("    / \     ")
                break

name = input("Enter your name: ")
print("welcome", name)
print("----------------------")
print("Try to Guess the word in less than 10 attempts")
hangman()
print()