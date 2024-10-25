#reverse string program

def reverse_strings(string_list):
    return [s[::-1] for s in string_list]

# Example usage:
input_list = ["hello", "world", "python"]
reversed_list = reverse_strings(input_list)
print(reversed_list)
