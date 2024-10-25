def keys_greater_than_n(input_dict, n):
    """
    Returns a list of keys from the dictionary where the value is greater than n.

    Args:
    input_dict (dict): The dictionary to check.
    n (int): The threshold value.

    Returns:
    list: List of keys with values greater than n.
    """
    return [key for key, value in input_dict.items() if value > n]


# Example usage:
example_dict = {'a': 5, 'b': 12, 'c': 3}
result = keys_greater_than_n(example_dict, 4)
print(result)  # Output: ['a', 'b']
