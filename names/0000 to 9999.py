import random

def generate_ordered_words():
    words = [f"{number:04d}" for number in range(10000)]
    return words

def save_to_file(words, filename):
    with open(filename, 'w') as file:
        for word in words:
            file.write(word + '\n')

if __name__ == "__main__":
    # Generate ordered words from 0000 to 9999
    ordered_words = generate_ordered_words()

    # Save the words to a file
    save_to_file(ordered_words, "random_words.txt")

    print("Ordered words saved to random_words.txt")