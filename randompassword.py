def recursive_length(lst):
    if lst == []:
        return 0
    return 1 + recursive_length(lst[1:])

# Example usage:
data = [4, 7, 2, 9, 5]
length = recursive_length(data)
print(f"Length of the list is: {length}")