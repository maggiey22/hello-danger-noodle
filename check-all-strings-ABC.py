#! /usr/bin/env python3

import pyperclip

def checkStringABC(tgt):
    charBefore = tgt[0];

# need to do for loop from 1 to the end of the string    
    for x in range(1, len(tgt)):
        if (tgt[x] < tgt[x-1]):
            return False

    return True

def checkAllStrings():
    text = str(pyperclip.paste())
    words = text.split('\n')

    for w in words:
        if (not(checkStringABC(w))):
            print(w + " is not alphabetized")


    print("Done checking!")


#check that all strings in clipboard are alphabetized
checkAllStrings()

