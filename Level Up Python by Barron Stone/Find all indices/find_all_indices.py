def index_all(data, target):
    """
    Finds all index paths to a specific target value within a nested list structure.
    
    Args:
        data (list): The arbitrarily nested list to search.
        target (Any): The value to search for.
        
    Returns:
        list: A list of index paths (where each path is a list of integers) 
              leading to the target elements.
    """
    # Initialize the list that will hold all the found index paths
    result = []
    
    # Define a helper function to recursively search the structure
    def search(current_item, current_path):
        # Iterate over both the index and value for each item in the list
        for i, val in enumerate(current_item):
            # Form the new path by appending the current index
            new_path = current_path + [i]
            
            # If we found the target, add the path to our results
            if val == target:
                result.append(new_path)
            # If the current value is a list itself, recurse into it
            elif isinstance(val, list):
                search(val, new_path)
    
    # Start the recursive search with the given data and an empty initial path
    search(data, [])
    
    return result

if __name__ == "__main__":
    # Example usage
    example = [[[1, 2, 3], 2, [1, 3]], 2, [1, 2, 3]]
    target = 2
    print(index_all(example, target))
