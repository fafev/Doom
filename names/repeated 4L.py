import random
import string

def generate_random_word():
    characters = string.ascii_lowercase  # You can customize the character set as needed
    char1 = random.choice(characters)
    char2 = random.choice(characters)
    
    # Ensure that char1 and char2 are distinct
    while char1 == char2:
        char2 = random.choice(characters)
    
    word = char1 + char2 + char2 + char2
    return word

# Generate and save 5 random 4-character words with two repeated characters to a text file
output_file_path = "random_words.txt"
with open(output_file_path, "w") as file:
    for _ in range(1000):
        random_word = generate_random_word()
        file.write(random_word + "\n")

print(f"Random words with two repeated characters have been saved to {output_file_path}")
