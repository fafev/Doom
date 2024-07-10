import random

# Function to generate a random 4-digit word
def generate_random_word():
    return f'{random.randint(0, 9999):04d}'

# Generate 1000 random words
words = [generate_random_word() for _ in range(1000)]

# Create HTML code and save it to a file
with open('random_words.txt', 'w') as file:
    file.write('--name gen by nakhoda--\n')
    for word in words:
        file.write(f'{word}\n')
    file.write('--name gen by nakhoda--')

print("Random words saved to 'random_words.txt'")
