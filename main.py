import pandas as pd
import random
print("Welcome to Word Guessing Game! You are given a sequence of dash and you have to guess it. Let's begin!!!")


def main():
    # Just a predefined list;)
    data = pd.read_csv("data.csv")
    data.head()
    l = data.iloc[:,0]
    word = random.choice(l)
    word.strip()
    # create dashed form for the word
    dash = blank(word)
    print("The word is ", dash)
    print("you have 8 attempts to guess the word")
    # attempt counter variable
    a = 8
    while a != 0:
        ch = input("Enter your guess: ")
        if ch.upper() in word or ch.lower() in word:
            print("That guess was correct")
            dash = replacedash(word, dash, ch)
            print("now the word looks like", dash)
            print("you have ", a, "attempts left")
        else:
            print("There are no ", ch, "'s in the word")
            a = a - 1
            print("you have ", a, "attempts left")
        if dash == word:
            print("Congratulations, the word is ", word)
            break
    else:
        print("Sorry, you lost. The secret word was: ", word)

'''randomlist- function gentrates a list of 1,2 or 3 numbers. At the numbers in the generated list the character
is shown to the player'''



def randomlist(w1):
    m=random.randint(1,3)
    gcl=[]#givencharacterlist
    for i in range(m+1):
        t = random.randint(0, len(w1) - 1)
        gcl.append(t)
    return(gcl)

'''blank- this function creates a dashed form of the word i.e. for cute it gives ----'''



def blank(w):
    d = ""
    t=randomlist(w)
    for i in range(len(w)):
        if i in t:
            d = d + w[i]
        else:
            d = d + "-"
    return d


'''replacedash- If the guess is correct this function prints the positions of the guessed letter'''


def replacedash(w, d1, c):
    list1 = occur(w, c)
    k = len(w) - 2
    for i in list1:
        if i >= 1 and i <= k:
            sub1 = d1[:i]
            sub2 = d1[i + 1:]
        elif i < 1:
            sub1 = ""
            sub2 = d1[i + 1:]
        else:
            sub1 = d1[:i]
            sub2 = ""
        d1 = sub1 + c + sub2
        sub1 = []
        sub2 = []
    return d1


'''Occur: This returns a list of all occurances of the character in the list'''


def occur(w1, c1):
    a = []
    for i in range(len(w1)):
        if w1[i] == c1:
            a.append(i)
    return a


if __name__ == '__main__':
    main()