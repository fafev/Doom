import string
import random

# Generate combinations of letters and numbers from '_.a0' to '_.z9'
combinations = [f"_{letter}{number}." for letter in 'abcdefghijklmnopqrstuvwxyz' for number in range(10)]

# Save the combinations to a file named 'random_words.txt'
with open('random_words.txt', 'w') as file:
    file.write('\n'.join(combinations))

print("Random words saved to 'random_words.txt'")
