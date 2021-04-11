from pprint import pprint  # All this function does is print dictionaries nicely. You don't have to use it.


def get_word_counts(filepath):
    """
    Returns a dictionary containing the work frequencies of a corpus contained in a file pointed to by filepath.

    :param filepath: A string containing the location of a file.
    :return: A dictionary of word frequencies.
    """
    try:
        with open(filepath, 'r') as file:
            word_counts = {}
            for line in file:
                line = line.lower()
                line = line.strip()
                for word in line.split(" "):
                    if word in word_counts:
                        word_counts[word] = word_counts[word] + 1
                    else:
                        word_counts[word] = 1

        return word_counts

    except FileNotFoundError as e:
        empty = {}
        return empty


def main():
    """
    Some sample behavior based on the README.
    """

    filepath = "lyrics.txt"
    word_counts = get_word_counts(filepath)
    pprint(word_counts)


# DO NOT WRITE CODE BELOW THIS LINE


if __name__ == '__main__':
    main()
