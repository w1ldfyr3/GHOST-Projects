""" Turn a word into its Pig Latin equivalent"""
import sys


VOWELS= "aeiou"

while True:
    word = input("Type a word: ")

    if not word:
        print("No input provided. Exiting...", file=sys.stderr)
        sys.exit()
    if not word.isalpha():
        print("Please Enter a word. :)\n")
        continue

    if word[0] in VOWELS:
        pig_latin = word + 'way'
    else:
        pig_latin = word[1:] + word[0] + 'ay'
    print()
    print(f"{pig_latin}", file=sys.stderr)

    try_again = input("\nTry again? (Press Enter to close else n to stop)\n ")
    if try_again.lower == 'n':
        sys.exit()
