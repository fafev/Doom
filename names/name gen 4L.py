import random



# Function to generate a random 3-character word with numbers, dots, and underscores

def generate_random_word():

    characters = 'abcdefghijklmnopqrstuvwxyz0123456789._'

    return ''.join(random.choice(characters) for _ in range(4))



# Generate 1000 random words

words = [generate_random_word() for _ in range(10000)]



# Create HTML code and save it to a file

with open('random_words.txt', 'w') as file:

    file.write('--name gen by nakhoda--\n')

    for word in words:

        file.write(f'{word}\n')

    file.write('--name gen by nakhoda--')



print("Random words saved to 'random_words.txt'")