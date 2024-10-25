#dictionary program

def print_even_keys(input_dict):
    """Prints keys from the input dictionary whose values are even numbers."""
    for key, value in input_dict.items():
        if isinstance(value, int) and value % 2 == 0:
            print(key)

# Example usage
example_dict = {
    'a': 1,
    'b': 2,
    'c': 3,
    'd': 4,
    'e': 5,
    'f': 6
}

print_even_keys(example_dict)
