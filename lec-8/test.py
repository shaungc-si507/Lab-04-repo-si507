from pathlib import Path
from itertools import permutations
import random

if __name__ == "__main__":
    book_title_file= Path("book_titles.txt")

    with book_title_file.open() as f:
        rawLine = f.readline()
        sanitizedLine = rawLine.strip()
        tokens = sanitizedLine.split()
        perms = permutations(tokens, 2)

        sampled_perms = list(perms)
        random.shuffle(sampled_perms)
        for per in sampled_perms[:3]:
            print(per)
        
        print("=====Title=====")

