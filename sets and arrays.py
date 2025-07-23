def power_of_two(n):
    if n == 0:
        print(1)
        return 1

    # Recursive call
    prev = power_of_two(n - 1)
    curr = 2 * prev

    print(curr)
    return curr

# Example usage:
power_of_two(5)