import random

def generate_dot_xx_names(count):
    names = ['_' + ''.join(random.choices('abcdefghijklmnopqrstuvwxyz0123456789', k=2)) + '_' for _ in range(count)]
    return names

# Number of names to generate
name_count = 1000

# Generate .xx. names
dot_xx_names = generate_dot_xx_names(name_count)

# Save names to random_words.txt
with open('random_words.txt', 'w') as file:
    for name in dot_xx_names:
        file.write(name + '\n')

print(f"{name_count} .xx. names generated and saved to random_words.txt.")
