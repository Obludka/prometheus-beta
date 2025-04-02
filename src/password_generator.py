import random
import string

def generate_password(length):
    """
    Generate a random password with the specified length.

    Args:
        length (int): The desired length of the password.

    Returns:
        str: A randomly generated password.

    Raises:
        ValueError: If the length is less than 1.
    """
    # Validate input
    if not isinstance(length, int):
        raise TypeError("Password length must be an integer")
    
    if length < 1:
        raise ValueError("Password length must be at least 1")

    # Define character sets
    lowercase = string.ascii_lowercase
    uppercase = string.ascii_uppercase
    digits = string.digits
    punctuation = string.punctuation

    # Combine all character sets
    all_characters = lowercase + uppercase + digits + punctuation

    # Special handling for very short passwords
    if length < 4:
        password = random.choices(all_characters, k=length)
        return ''.join(password)

    # Generate password ensuring at least one character from each set
    password = [
        random.choice(lowercase),
        random.choice(uppercase),
        random.choice(digits),
        random.choice(punctuation)
    ]

    # Fill the rest of the password with random characters
    password.extend(random.choice(all_characters) for _ in range(length - 4))

    # Shuffle the password to randomize the position of initial characters
    random.shuffle(password)

    # Convert list of characters to string
    return ''.join(password)