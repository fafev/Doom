import random

def generate_random_name():
    # Define lists of possible values for each position
    first_letter = random.choice('abcdefghijklmnopqrstuvwxyz')
    last_letter = random.choice('abcdefghijklmnopqrstuvwxyz')
    number = random.randint(0, 9)
    
    # Generate the name based on the pattern n_ln
    name = f"{first_letter}.{number}{first_letter}"
    
    return name

def save_names_to_file(filename, names, mode='w'):
    with open(filename, mode) as file:
        for name in names:
            file.write(name + '\n')

# Generate 10 random names
random_names = [generate_random_name() for _ in range(1000)]

# Save the names to random_names.txt
save_names_to_file('random_words.txt', random_names)
