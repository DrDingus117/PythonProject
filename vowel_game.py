## 1. Define a list of vowels
## 2. Ask the user to input a word
## 3. Loop through the word and check if each letter is a vowel
## 4. If the letter is a vowel, print it
## 5. If the letter is not a vowel, tell the player it is not a vowel
## 6. If player gets all the vowels in the word, tell them they won

def count_vowels(text: str) -> int:
    vowels: str = "aeiouAEIOU"
    count: int = 0

    for char in text:
        if char in vowels:
            count += 1

    return count

input_text: str = input("Enter a word: ").strip()
print(f"The number of vowels in '{input_text}' is: {count_vowels(input_text)}")