# 1. Let's make it more idiomatic

Your task is to refactor the following report generation code to more idiomatic. The existing implementation was written by an unknown developer who did not know anything about the idioms of Python. Luckily the unkown developer documented the implementation decently and wrote some tests for it. 

### The specification of the report generation

This file content:
```
something
1
7
somEThing

2
wassup
woop
woop
something
WoOP
```

Should yield this report:
```
missing values: 1
highest number: 7.0
most common words: something, woop
occurrences of most common: 3
#####
numbers: [1.0, 7.0, 2.0]
words: ['something', 'something', 'wassup', 'woop', 'woop', 'something', 'woop']
```

Note:
* all numbers of the input file should be presented as floats in the report
* all words are presented as lowercased in the report
* while calculating the most common words, the count should be done as case insensitive (in other words, `'WoOp'` should be considered the same word as `'woop'`)
* if there are multiple different most common words, they should be presented in the format presented above
* there are more examples in the tests

Run the cell of the existing implementation and then run the tests to verify that it works correctly. Then make sure that you understand how the legacy implementation works. After that, start refactoring, a function by function. Good luck!

```python
def get_report(path):
    """
    Creates a report of the file specified as argument.

    :param path: path to file from which the report should be created (string)
    :return: the report (string)
    """
    data = _read_file(path)
    missing_count = data[0]
    numbers = data[1]
    words = data[2]
    report = _make_report(missing_count, numbers, words)
    return report


def _read_file(path):
    """
    Reads and returns the data from the file specified as argument.

    :param path: path to the file to be read.
    :return: a tuple containing
    1. the number of empty lines (int)
    2. numeric values (list of floats)
    3. non-numeric values (list of strings)
    """
    data_file = open(path)
    lines = data_file.readlines()
    line_count = len(lines)
    idx = 0
    empty_lines = 0
    words = []
    numbers = []
    while idx < line_count:
        line = lines[idx]
        line = line.strip()
        if line == "":
            empty_lines = empty_lines + 1
        else:
            is_number = False
            try:
                number = float(line)
                is_number = True
            except Exception:
                pass

            if is_number:
                numbers.append(number)
            else:
                words.append(line)
        idx = idx + 1
    data_file.close()

    return empty_lines, numbers, words


def _make_report(missing_values, numbers, words):
    """
    Creates and a report based on data given as arguments.

    :param missing_values: number of empty lines (int)
    :param numbers: numeric values (list of floats)
    :param words: non numeric values (list of strings)
    :return: the generated report (string)
    """
    max_value = _get_max_value(numbers)
    lower_case_words = _words_to_lowercase(words)
    most_common_info = _get_most_common_words(lower_case_words)
    most_common_words = most_common_info[0]
    most_common_count = most_common_info[1]

    most_common_str = ""
    for idx in range(len(most_common_words)):
        most_common_str += most_common_words[idx] + ", "
    # remove the last comma and space
    most_common_str = most_common_str[0 : len(most_common_str) - 2]

    report = (
        "missing values: {}\n"
        "highest number: {}\n"
        "most common words: {}\n"
        "occurrences of most common: {}\n"
        "#####\n"
        "numbers: {}\n"
        "words: {}"
    ).format(
        missing_values,
        max_value,
        most_common_str,
        most_common_count,
        numbers,
        lower_case_words,
    )

    return report


def _get_max_value(numbers):
    """
    Returns the greatest value of the list given as argument.

    :param numbers: numbers (list of numeric values)
    :return: greatest value of numbers, None if numbers is an empty list
    """
    max_value = None
    if len(numbers) > 0:
        max_value = numbers[0]
        for idx in range(len(numbers)):
            if numbers[idx] > max_value:
                max_value = numbers[idx]
    return max_value


def _words_to_lowercase(words):
    """
    :param words: words to be converted (list of strings)
    :return: lowercased words (list of strings)
    """
    lowercased = []
    for idx in range(len(words)):
        value = words[idx].lower()
        lowercased.append(value)
    return lowercased


def _get_most_common_words(words):
    """
    Finds the most common words in a list of words.
    If there are multiple different words with the same amount of occurrences,
    they are all included in the return value sorted alphabetically.
    In addition to returning the most common words, the return value
    includes also the count of occurrences of the most common words.

    :param words: list of words (list of strings)
    :return: a tuple containing:
    1. most common words (list of strings)
    2. the count of occurrences of the most common words (int)
    """
    word_counts = {}
    idx = 0
    while idx < len(words):
        value = words[idx]
        if value not in word_counts.keys():
            word_counts[value] = 1
        else:
            word_counts[value] += 1
        idx = idx + 1

    max_count = 0
    for value in word_counts.values():
        if value > max_count:
            max_count = value

    most_common_words = []
    for word in word_counts.keys():
        count = word_counts[word]
        if count == max_count:
            most_common_words.append(word)

    most_common_words = sorted(most_common_words)

    return most_common_words, max_count
```

Now it's time refactor the existing code to make it more idiomatic.

It's desirable that you do the refactoring in small chunks. Consider using the following workflow:
1. Copy-paste a single function from the above ugly implementation to the cell below
2. Refactor the function
3. Run the tests to verify that you did not break anything

This way you can consider each function as a separate sub task.

```python
# Your beautiful refactored, idiomatic, pythonic solution here
```

The tests are here. Run these often while refactoring!

```python
from pathlib import Path

CURRENT_DIR = Path.cwd()
DATA_DIR = CURRENT_DIR.parent / "data"

DATA_FILE1 = DATA_DIR / "misc_data1.txt"
DATA_FILE2 = DATA_DIR / "misc_data2.txt"
DATA_FILE3 = DATA_DIR / "empty.txt"


expected1 = """missing values: 2
highest number: 99.0
most common words: john
occurrences of most common: 4
#####
numbers: [1.0, 2.0, 99.0, 6.72, 2.0, 2.0, 2.0]
words: ['john', 'doe', 'john', 'john', 'was', 'here', 'this', 'is', 'totally', 'random', 'john']"""

expected2 = """missing values: 3
highest number: 101.0
most common words: doe, john
occurrences of most common: 4
#####
numbers: [1.0, 2.0, 101.0, 6.72, 2.0, 2.0, 67.0, 2.0]
words: ['john', 'doe', 'john', 'john', 'doe', 'was', 'doe', 'here', 'this', 'is', 'totally', 'random', 'john', 'doe']"""

expected3 = """missing values: 0
highest number: None
most common words: 
occurrences of most common: 0
#####
numbers: []
words: []"""

assert get_report(DATA_FILE1) == expected1
print("First one OK!")

assert get_report(DATA_FILE2) == expected2
print("Second one OK!")

assert get_report(DATA_FILE3) == expected3
print("All OK, woop woop!")
```

```python
# If the tests are failing, you can debug here.

report = get_report(DATA_FILE1)
print(report)
```

