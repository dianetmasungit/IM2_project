def get_frequency(text):
    freq = {}  
    for char in text:
        if char.isalpha(): 
            if char in freq:
                freq[char] += 1
            else:
                freq[char] = 1
    return freq


def main():
    user_input = input("Enter string: ")

    strings = [s.strip() for s in user_input.split(",")]

    for s in strings:
        freq_dict = get_frequency(s)
        output = ", ".join([f"{ch}={cnt}" for ch, cnt in freq_dict.items()])
        print(output)


if __name__ == "__main__":
    main()
