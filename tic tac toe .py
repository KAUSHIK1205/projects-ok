def count_change(amount, coins, index=0):
    # If amount is exactly 0, we found a valid way
    if amount == 0:
        return 1
    # If amount is negative or no coins left, this path is invalid
    if amount < 0 or index == len(coins):
        return 0

    # Recursive calls:
    # 1. Include coins[index] and stay on the same coin
    # 2. Exclude coins[index] and move to the next coin
    include = count_change(amount - coins[index], coins, index)
    exclude = count_change(amount, coins, index + 1)

    return include + exclude

# Example: Make ₹5 using ₹1, ₹2, ₹5 coins
coins = [1, 2, 5]
amount = 5
ways = count_change(amount, coins)
print(f"Number of ways to make ₹{amount} using {coins}: {ways}")





