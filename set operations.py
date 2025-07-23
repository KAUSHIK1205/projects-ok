def array_length_recursive(arr):
    # Base case: empty list
    if arr == []:
        return 0
    # Recursive step: count the first element and recurse on the rest
    return 1 + array_length_recursive(arr[1:])

# Example usage:
my_list = [10, 20, 30, 40, 50]
print(f"Length of the list: {array_length_recursive(my_list)}")