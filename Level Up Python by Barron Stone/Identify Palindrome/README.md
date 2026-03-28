# Identify Palindrome

This directory contains a Python script and unit tests to determine whether a given phrase is a valid palindrome.

## Implementation Details

`is_palidrome.py` includes the `is_palindrome` function and a simple interactive command-line interface.
The function is designed to check for palindromic phrasing while explicitly ignoring any non-alphabetic characters.

- Extracted and normalized input strings to lower case.
- Strips out all spaces, numbers, and punctuation symbols before evaluation.

`test_is_palindrome.py` includes a `unittest` test suite with 9 different test cases, including edge case validation such as:

- Number-only inputs
- Alphanumeric strings containing both letters and digits
- Completely non-alphabetic strings containing just punctuation

## Running

You can interactively check strings via the command line:

```bash
python is_palidrome.py
```

It will prompt `Enter a phrase:` and output either `True` or `False`.

## Running the Tests

To run the unit test suite on the `is_palindrome` function, execute:

```bash
python test_is_palindrome.py
```
