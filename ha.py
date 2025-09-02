
def wordchecker(word):
    vowel = "aeiou"
    for letter in word:
        if letter.isalpha():
            case = "capital" if letter.isupper else "not capital"
            if letter.lower() in vowel:
                print(f"{letter} ({case} letter) is a vowel")
            else:
                print(f"{letter} ({case} letter) is a consonant")
        else:
            print(f"{letter} is not a letter.")

while(True):
    word = input("Enter string: ")
    if word == "x":
        print("Program Closed.")
        break
    wordchecker(word)