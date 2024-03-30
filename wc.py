import argparse
import os
import sys


# Return File Pointer to be used by other functions
def file_pointer(filename):
    if os.path.isfile(filename):
        return open(filename, encoding="utf-8")
    else:
        sys.exit(f"{filename} not found. Please give correct filename!")


# Returns the number of bytes in the file
def number_of_bytes(cursor):
    cursor.seek(0, 2)
    return cursor.tell()


# Return the number of lines in the file
def number_of_lines(cursor):
    cursor.seek(0)
    return sum(1 for _ in cursor)


# Returns the number of characters in the file
def number_of_characters(cursor):
    cursor.seek(0)
    characterCount = 0
    for line in cursor:
        characterCount += len(line.strip())
    return characterCount


# Returns the number of words in the file
def number_of_words(cursor):
    cursor.seek(0)
    wordcounter = 0
    for line in cursor:
        wordcounter += sum(1 for _ in line.split())
    return wordcounter


# Create a CLI arguments parser
parser = argparse.ArgumentParser(
    description="A wc utility similar to Unix Systems",
    add_help=True,
)

# Defining Flags and Arguments
parser.add_argument('filename', help="Name of the file")
parser.add_argument("-l", "--lines", action='store_true', help="Number of lines in the file")
parser.add_argument("-w", "--words", action='store_true', help="Number of words in the file")
parser.add_argument("-c", "--characters", action='store_true', help="Number of characters in the file")
parser.add_argument("-b", "--bytes", action='store_true', help="Number of bytes in the file")


# Main function
if __name__ == '__main__':
    args = parser.parse_args()
    filePointer = file_pointer(args.filename)
    if args.lines:
        print(number_of_lines(filePointer))
    elif args.words:
        print(number_of_words(filePointer))
    elif args.characters:
        print(number_of_characters(filePointer))
    elif args.bytes:
        print(number_of_bytes(filePointer))
    else:
        print("Lines: ", number_of_lines(filePointer), "Words: ", number_of_words(filePointer), "Characters: ",
              number_of_characters(filePointer), "Bytes: ", number_of_bytes(filePointer))
