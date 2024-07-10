import random

def generate_underscore_number_letter_names(count):
    names = ['_.' + str(random.randint(0, 9)) + random.choice('abcdefghijklmnopqrstuvwxyz0123456789') for _ in range(count)]
    return names

# Number of names to generate
name_count = 1000

# Generate _x5 names
underscore_number_letter_names = generate_underscore_number_letter_names(name_count)

# Save names to random_words.txt
with open('random_words.txt', 'w') as file:
    for name in underscore_number_letter_names:
        file.write(name + '\n')

print(f"{name_count} _[one number][one letter] names generated and saved to random_words.txt.")
