# Sort String

This directory contains a Python script and unit tests to sort the words in a given phrase case-insensitively.

## Implementation Details

`sort_string.py` includes the `sort_string` function and a simple interactive command-line interface.
The function is designed to split a string into words and sort them alphabetically, ignoring case distinctions.

- Splits the string by spaces to extract individual words.
- Uses Python's built-in `sorted()` function with a lambda key to convert each word to lower case for comparison.
- Joins the sorted list of words back into a single string.

`test_sort_string.py` includes a `unittest` test suite covering various scenarios, including:

- Standard multi-word phrases
- Mixed casing of words
- All lowercase or all uppercase words
- Single words and empty strings

## Running

You can interactively sort strings via the command line:

```bash
python sort_string.py
```

It will prompt `Enter a string: ` and output the newly sorted string.

## Running the Tests

To run the unit test suite on the `sort_string` function, execute:

```bash
python -m unittest test_sort_string.py
```
