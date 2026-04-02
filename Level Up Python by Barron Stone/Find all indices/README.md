# Find All Indices

This directory contains a Python script and unit tests for finding all index paths to a specific target value within an arbitrarily nested list structure.

## Implementation Details

`find_all_indices.py` includes the `index_all` function which takes a nested list and a target value.
The function is designed to recursively search the entire structure and return a list of paths (indices) where the target value is found.

- Initializes an empty list `result` to hold all identified paths.
- Uses a helper function `search` to recursively traverse the list elements and their indices.
- Tracks the `current_path` by appending the current index during each step.
- When an element matches the target, the current path is appended to the results.
- If an element is a nested list itself, it recursively calls `search` on that sub-list.

`test_find_all_indices.py` includes a `unittest` test suite covering various scenarios, including:

- Standard nested lists containing the target element
- Flat lists
- Empty lists and lists where the target isn't found
- Deeply nested configurations
- Targets of varying types (strings, lists, mixed elements)

## Running

You can run the script via the command line to see the provided example in action:

```bash
python find_all_indices.py
```

It will execute the function on an example nested list and print out all indices where the target `2` was found.

## Running the Tests

To run the unit test suite on the `index_all` function, execute:

```bash
python -m unittest test_find_all_indices.py
```
