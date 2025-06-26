import itertools
import os
from utils import leetspeak_variants

def generate_wordlist(name, birthdate, petname):
    base_words = [name, birthdate, petname]
    patterns = ["", "123", "@123", "2025", "!"]
    words = set()

    for word in base_words:
        for pat in patterns:
            words.add(word + pat)
            words.add(pat + word)
            words.update(leetspeak_variants(word + pat))

    with open("custom_wordlist.txt", "w") as f:
        for word in words:
            f.write(word + "\n")
    print(f"Generated {len(words)} words in custom_wordlist.txt")

if __name__ == "__main__":
    name = input("Enter your name: ")
    birth = input("Enter your birthdate (YYYY): ")
    pet = input("Enter your pet's name: ")
    generate_wordlist(name, birth, pet)
