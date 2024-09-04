import hashlib
import itertools
import string

# Function to hash a password using a specified algorithm
def hash_password(password, algorithm='md5'):
    if algorithm == 'md5':
        return hashlib.md5(password.encode()).hexdigest()
    elif algorithm == 'sha1':
        return hashlib.sha1(password.encode()).hexdigest()
    elif algorithm == 'sha256':
        return hashlib.sha256(password.encode()).hexdigest()
    else:
        raise ValueError("Unsupported hashing algorithm")

# Dictionary attack using a wordlist
def dictionary_attack(hashed_password, wordlist_file, algorithm='md5'):
    with open(wordlist_file, 'r') as file:
        for word in file:
            word = word.strip()
            hashed_word = hash_password(word, algorithm)
            if hashed_word == hashed_password:
                return word
    return None

# Brute force attack with specified character set and length range
def brute_force_attack(hashed_password, algorithm='md5', charset=string.ascii_lowercase, min_len=1, max_len=6):
    for length in range(min_len, max_len + 1):
        for guess in itertools.product(charset, repeat=length):
            guess = ''.join(guess)
            hashed_guess = hash_password(guess, algorithm)
            if hashed_guess == hashed_password:
                return guess
    return None

# Main function to choose attack method and run the cracker
def main():
    # Example hashed password (hash of 'password123' using MD5)
    hashed_password = '482c811da5d5b4bc6d497ffa98491e38'
    
    # Path to the wordlist
    wordlist_file = 'rockyou_reduced.txt'
    
    # Choose the attack method
    attack_method = input("Choose attack method (1: Dictionary, 2: Brute Force): ").strip()

    if attack_method == '1':
        result = dictionary_attack(hashed_password, wordlist_file)
        if result:
            print(f"Password cracked using dictionary attack: {result}")
        else:
            print("Password not found in wordlist.")
    elif attack_method == '2':
        result = brute_force_attack(hashed_password)
        if result:
            print(f"Password cracked using brute force attack: {result}")
        else:
            print("Password not found within the given brute force constraints.")
    else:
        print("Invalid choice. Please select 1 or 2.")

if __name__ == "__main__":
    main()
