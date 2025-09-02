def wordchecker(word):
    vowel = "aeiou"
    for letter in word:
        if letter.isalpha():
            case = "capital" if letter.isupper() else "small"
            if letter.lower() in vowel:
                print(f"{letter} ({case} letter) is a vowel")
            else:
                print(f"{letter} ({case} letter) is a consonant")
        else:
            print("Not a letter.")

word = input("Enter word: ")
wordchecker(word)
