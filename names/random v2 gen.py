import string
import random

# Generate combinations of letters and numbers from 'aa' to 'a9'
combinations_10 = [f"_{prefix}{suffix}_" for prefix in 'abcdefghijklmnopqrstuvwxyz' for suffix in list('abcdefghijklmnopqrstuvwxyz0123456789')]

# Save the combinations to a file named 'random_words_10.txt'
with open('random_words.txt', 'w') as file:
    file.write('\n'.join(combinations_10))

print("Random words saved to 'random_words.txt'")