import nltk
import random
import string

def download_wordnet():
    try:
        nltk.data.find('corpora/wordnet.zip')
    except LookupError:
        nltk.download('wordnet')

def generate_random_word():
    alphabet = string.ascii_lowercase
    word_length = random.randint(3, 10)
    return ''.join(random.choice(alphabet) for _ in range(word_length))

def generate_words(num_words):
    download_wordnet()
    words = set()

    while len(words) < num_words:
        random_word = generate_random_word()

        if nltk.corpus.wordnet.synsets(random_word):
            words.add(random_word)

    return list(words)[:num_words]

def save_to_file(words, filename):
    try:
        with open(filename, 'w') as file:
            file.write('\n'.join(words))
        print(f"Words saved to {filename}")
    except IOError as e:
        print(f"Error writing to {filename}: {e}")

# Generate 10,000 words
num_words = 10000
random_words = generate_words(num_words)

# Save the generated words to a file
save_to_file(random_words, 'dictionary_words.txt')

# Display the generated words
for i, word in enumerate(random_words):
    print(f"{i + 1}. {word}")
