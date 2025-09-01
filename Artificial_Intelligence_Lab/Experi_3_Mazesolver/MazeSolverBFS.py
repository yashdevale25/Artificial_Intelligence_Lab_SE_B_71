import collections

def solve_maze_bfs(maze):
    """
    Solves a maze using Breadth-First Search (BFS).

    Args:
        maze (list of lists): The maze represented as a 2D grid.
                              'S' for start, 'E' for end, '#' for wall, ' ' for path.

    Returns:
        list of tuples: The path from start to end, or None if no path exists.
    """
    rows = len(maze)
    cols = len(maze[0])
    start = None
    end = None

    # Find start and end points
    for r in range(rows):
        for c in range(cols):
            if maze[r][c] == 'S':
                start = (r, c)
            elif maze[r][c] == 'E':
                end = (r, c)

    if not start or not end:
        print("Start or End point not found in maze.")
        return None

    queue = collections.deque([(start, [start])])  # (current_position, path_taken)
    visited = set([start])

    while queue:
        (r, c), path = queue.popleft()

        if (r, c) == end:
            return path

        # Define possible movements (up, down, left, right)
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        for dr, dc in directions:
            nr, nc = r + dr, c + dc

            # Check if the new position is valid
            if 0 <= nr < rows and 0 <= nc < cols and maze[nr][nc] != '#' and (nr, nc) not in visited:
                visited.add((nr, nc))
                new_path = path + [(nr, nc)]
                queue.append(((nr, nc), new_path))
    return None


def print_path(maze, path):
    """
    Prints the maze with the solved path marked.
    """
    if not path:
        print("No path found.")
        return

    maze_copy = [list(row) for row in maze] # Create a copy to modify
    for r, c in path:
        if maze_copy[r][c] not in ['S', 'E']:
            maze_copy[r][c] = '*' # Mark the path

    for row in maze_copy:
        print("".join(row))

# Example Usage:
if __name__ == "__main__":
    # Example Maze (using '#' for walls, ' ' for paths, 'S' for start, 'E' for end)
    maze_example = [
        ['#', '#', '#', '#', '#', '#', '#'],
        ['#', 'S', ' ', ' ', ' ', ' ', '#'],
        ['#', ' ', '#', '#', '#', ' ', '#'],
        ['#', ' ', '#', 'E', '#', ' ', '#'],
        ['#', ' ', '#', ' ', '#', ' ', '#'],
        ['#', ' ', ' ', ' ', ' ', ' ', '#'],
        ['#', '#', '#', '#', '#', '#', '#']
    ]

    print("Original Maze:")
    for row in maze_example:
        print("".join(row))
    print("\n" + "="*30 + "\n")

    print("Solving with BFS:")
    bfs_path = solve_maze_bfs(maze_example)
    if bfs_path:
        print("Path found with BFS:")
        print_path(maze_example, bfs_path)
    else:
        print("No path found with BFS.")

    print("\n" + "="*30 + "\n")

    # Another example where no path exists
    no_path_maze = [
        ['#', '#', '#', '#', '#', '#', '#'],
        ['#', 'S', ' ', ' ', '#', ' ', '#'],
        ['#', '#', '#', ' ', '#', ' ', '#'],
        ['#', ' ', '#', 'E', '#', ' ', '#'],
        ['#', ' ', '#', ' ', '#', ' ', '#'],
        ['#', ' ', ' ', ' ', ' ', ' ', '#'],
        ['#', '#', '#', '#', '#', '#', '#']
    ]
    print("Original Maze (No Path Example):")
    for row in no_path_maze:
        print("".join(row))
    print("\n" + "="*30 + "\n")

    print("Solving with BFS (No Path):")
    bfs_no_path = solve_maze_bfs(no_path_maze)
    print_path(no_path_maze, bfs_no_path)

   
