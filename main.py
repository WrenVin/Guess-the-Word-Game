#Hangman
import random
import string
def main():
    hChars = ['     ', '0', '|', '/', '\\', '/', ' \\']
    words = ("beach", 'jerky', 'arise', 'space', 'cloud', 'house', 'trial', 'earth', 'money')
    finalWord = random.choice(words)
    hangman = '''{}{}
    {}{}{}
    {}{}'''.format(hChars[0], hChars[1], hChars[3], hChars[2], hChars[4], hChars[5], hChars[6])
    
    for i in range(len(finalWord)):
        pass
    

    a = string.ascii_letters
    a1 = finalWord[0]
    a2 = finalWord[1]
    a3 = finalWord[2]
    a4 = finalWord[3]
    a5 = finalWord[4]
    
    


    word = [a1]
    
    

  
    endWord = ""
    print("Welcome to Hangman Digital! Make sure to only enter lowercase letters. \nYou only have 20 tries. Make sure to only enter ONE letter at a time. \nHINT: The word is 5 letters long.")
    letterWord = ""
    for i in range(20):
        
        if endWord == finalWord:
            break
        if len(endWord) > 4:
            break
        letterInput = input(":{}".format(letterWord))
        for letter in word:
            if letterInput == letter:
                letterWord += letter
                if letterInput == a1:
                    endWord += letterInput
                    word.remove(a1)
                    word.append(a2)
                if letterInput == a2:
                    word.remove(a2)
                    word.append(a3)
                    endWord += letterInput
                if letterInput == a3:
                    word.remove(a3)
                    word.append(a4)
                    endWord += letterInput
                if letterInput == a4:
                    word.remove(a4)
                    word.append(a5)
                    endWord += letterInput
                if letterInput == a5:
                    word.remove(a5)
                    endWord += letterInput
    if endWord == finalWord:
        print("You have Won! Final word: {}".format(finalWord))
         
    elif endWord != finalWord:
        print("You Lost...")
    return endWord
                    
end = main()
def cls():
    print('\n' * 200)

def trueEnd(l):
    while True:        
        k = input("Play again?: yes/no:")  
        if k == "yes":
            cls()
            end = main()
        else:
            break
    
trueEnd(end)
























