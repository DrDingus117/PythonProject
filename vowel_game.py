def count_vowels():
    vowels = ["a", "e", "i", "o", "u"]

    word = input("Enter a word: ").lower()

    vowel_count = 0

    for letter in word:
        if letter in vowels:
            print(letter, "is a vowel.")
            vowel_count += 1
        else:
            print(letter, "is not a vowel.")

    if vowel_count == len(word):
        print("You won! Every letter in the word is a vowel.")
    else:
        print("There were", vowel_count, "vowel(s) in the word.")

count_vowels()