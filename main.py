from collections import Counter

def count_chars(s):
    return Counter(s.lower())

def word_count(s):
    return len(s.split())


def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        print(f"--- Begin report of books/frankenstein.txt ---")
        print(f"{word_count(file_contents)} words found in the document")
        print()

        for char, count in sorted(count_chars(file_contents).items(), key=lambda x: x[1], reverse=True):
            print(f"The '{char}' character was found {count} times")

main()