import random
import string

def generate_random_word():
    characters = string.ascii_lowercase  # Include both lowercase letters and digits
    char1 = random.choice(characters)
    char2 = random.choice(characters)
    
    # Ensure that char1 and char2 are distinct
    while char1 == char2:
        char2 = random.choice(characters)
    
    char3 = random.choice("." + characters + ".")  # Include dots and underlines in char3
    char4 = random.choice("_" + characters + "_")  # Include dots and underlines in char4
    
    word = char3 + char2 + char1 + char3
    return word 

# Generate and save 1000 random 4-character words with two repeated characters (including numbers) to a text file
output_file_path = "random_words.txt"
with open(output_file_path, "w") as file:
    for _ in range(1000):
        random_word = generate_random_word()
        file.write(random_word + "\n")

print(f"Random words with two repeated characters (including numbers) have been saved to {output_file_path}")
