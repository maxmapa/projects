import math


def truncate_euclidean_distance(moves):
    # Initialize variables to track the displacement in horizontal and vertical directions
    horizontal_displacement = 0
    vertical_displacement = 0

    # Define the mapping of moves to horizontal and vertical displacements
    move_mappings = {
        0: (1, 1),  # Move up and right
        1: (1, -1),  # Move down and right
        2: (-1, -1),  # Move down and left
        3: (-1, 1)  # Move up and left
    }

    # Iterate through the moves and update the displacements
    for move in moves:
        horizontal, vertical = move_mappings[move]
        horizontal_displacement += horizontal
        vertical_displacement += vertical
    # Calculate the squared Euclidean distance
    squared_distance = horizontal_displacement**2 + vertical_displacement**2

    # Truncate the Euclidean distance by taking the square root and rounding it to an integer
    truncated_distance = int(math.sqrt(squared_distance))

    return truncated_distance


# Example input
moves = [0, 3, 0, 0, 2, 0, 0]
# Example output
result = truncate_euclidean_distance(moves)
print(result)
