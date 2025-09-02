input = input("Enter String: ")
vowels = "aeiou"
for x in input:
    if x.isalpha():
        if x.lower() in vowels:
            a = "vowel"
        else:
            a = "consonant"
        if x.isupper():
            b = "uppercase"
        else:
            b = "lowercase"

        print(f"{x} is a {a} & {b}")
    else:
        print(f"{x} is not a letter")