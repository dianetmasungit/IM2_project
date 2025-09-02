for x in range(1,11):
    for y in range(10,x-1,-1):
        print(f"{y}",end=" ")
    print()

for x in range(1,6):
    for y in range(6,11):
        print(f"{x}{y}",end=" ")
    print()

while(True):
    print("Enter string: ")
    str = input()
    print(str)
    for z in str:
        match z:
            case "a":
                print(z, end=" Vowel")
                print()
            case "e":
                print(z, end=" Vowel")
                print()
            case "i":
                print(z, end=" Vowel")
                print()
            case "o":
                print(z, end=" Vowel")
                print()
            case "u":
                print(z, end=" Vowel")
                print()
            case _:
                print(z, end=" Consonant")
                print()
        break

    if z == z.lower():
        for z in str:
         match z:
            case "a":
                print(z, end=" lower Vowel")
                print()
            case "e":
                print(z, end=" lower Vowel")
                print()
            case "i":
                print(z, end=" lower Vowel")
                print()
            case "o":
                print(z, end=" lower Vowel")
                print()
            case "u":
                print(z, end=" lower Vowel")
                print()
            case _:
                print(z, end=" lower Consonant")
                print()
        break
    else:
        for z in str:
         match z:
            case "a":
                print(z, end=" Vowel")
                print()
            case "e":
                print(z, end=" Vowel")
                print()
            case "i":
                print(z, end=" Vowel")
                print()
            case "o":
                print(z, end=" Vowel")
                print()
            case "u":
                print(z, end=" Vowel")
                print()
            case _:
                print(z, end=" Consonant")
                print()
        break





while(True):
    print("Enter number: ")
    z = int(input())
    if z <= 0:
        break

size = int(input("Enter matrix size: "))
for x in range(size):
    for y in range(size):
        if x % 2 == 0:
            print("x",end=" ")
        else:
            print("0",end=" ")
    print()
