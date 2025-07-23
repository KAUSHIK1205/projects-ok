def count_maze_paths(maze, x=0, y=0):
    n = len(maze)

    # Base case: reached destination
    if x == n - 1 and y == n - 1:
        return 1

    # If out of bounds or hitting a wall, return 0
    if x >= n or y >= n or maze[x][y] == 0:
        return 0

    # Move right and down recursively
    right = count_maze_paths(maze, x, y + 1)
    down = count_maze_paths(maze, x + 1, y)

    return right + down

# Example Maze (5x5)
maze = [
    [1, 0, 0, 0, 1],
    [1, 1, 0, 1, 1],
    [0, 1, 1, 0, 0],
    [1, 1, 0, 1, 1],
    [0, 1, 1, 1, 1]
]

ways = count_maze_paths(maze)
print(f"Number of ways to escape the maze: {ways}")