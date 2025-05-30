import sys
from stats import (wordcount, 
                   charactercount,
                   sort_dict)

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {sys.argv[1]}...")
    print("----------- Word Count ----------")
    print(f"Found {wordcount(sys.argv[1])} total words")
    print("--------- Character Count -------")
    print(sort_dict(sys.argv[1]))
    print("============= END ===============")

main()

