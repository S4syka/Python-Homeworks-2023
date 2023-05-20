from random import randint # Do not delete this line

def initList():
    with open(".\hangman-ascii.txt", 'r') as file:
        return file.readlines()
    

def OutputFormFile(i, j):
    lst = initList();
    for k in range(i,j):
        print(lst[k], end="")


def displayIntro():
    OutputFormFile(0, 22)
    pass


def displayEnd(result):
    if result is True:
        OutputFormFile(190, 203)
    else:
        OutputFormFile(99, 112)
    pass


def displayHangman(state):
    if state == 1:
        OutputFormFile(23, 33)
    if state == 2:
        OutputFormFile(36, 46)
    if state == 3:
        OutputFormFile(49, 59)
    if state == 4:
        OutputFormFile(62, 72)
    if state == 5:
        OutputFormFile(75, 85)
    if state == 6:
        OutputFormFile(88, 97)


def getWord():
    with open(".\hangman-words.txt", 'r') as file:
        lst = file.read().split()
        return lst[randint(0, len(lst) - 1)]


def valid(c):
    if len(c) == 1 and c.isalpha() and c.islower():
        return True
    else:
        return False


def outputinfo (guessedWord):
    print(f"Guess the word: {guessedWord}")
    print("Enter the letter: ", end="")
    return input()


def containsChar(word, chr):
    for s in word:
        if s == chr:
            return True
        
    return False    


def play():
    word = getWord()
    i = 1
    guessedWord = "_"*len(word)
    while True:
        if i == 6:
            displayHangman(6)
            print(f"Hidden word was {word}")
            return False
        elif word == guessedWord:
            print(f"Hidden word was {word}")
            return True

        displayHangman(i)
        c = outputinfo(guessedWord)

        if valid(c) is False:
            print("Invalid character, try again")
            continue
        
        if containsChar(word, c) is False:
            i = i + 1
            continue
        
        for k in range(len(word)):
            if word[k] == c:
                l = list(guessedWord)
                l[k] = c
                guessedWord = "".join(l)


def hangman():
    while True:
        displayIntro()
        result = play()
        displayEnd(result)
        print("Do you want to play again? Y/N")
        c = input()
        if c == "Y":
            continue
        if c == "N":
            break

if __name__ == "__main__":
     hangman()