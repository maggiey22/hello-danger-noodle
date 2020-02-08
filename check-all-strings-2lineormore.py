#! /usr/bin/env python3

import pyperclip

text = str(pyperclip.paste())
anagrams = text.split('\n\n')

for a in anagrams:
    if (not ('\n' in a)):
        print(a + " is wrong!")


print("All done!")
