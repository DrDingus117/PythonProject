def text_analysis():
    text = input("Enter a sentence or paragraph: ")

    text = text.lower()
    text = text.strip()
    text = text.replace(",", "")
    text = text.replace(".", "")
    text = text.replace("!", "")

    words = text.split()

    total_words = len(words)

    total_letters = 0

    for word in words:
        total_letters += len(word)

    average_length = total_letters / total_words

    print("\nText Analysis Summary")
    print("---------------------")
    print("Total words:", total_words)
    print(f"Average word length: {average_length:.2f}")

text_analysis()