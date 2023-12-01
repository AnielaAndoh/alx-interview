#!/usr/bin/python3
"""Defines island perimeter finding function."""


def island_perimeter(grid):
    """Return the perimiter of an island.
    The grid represents water by 0 and land by 1.
    Args:
        grid (list): A list of list of integers representing an island.
    Returns:
        The perimeter of the island defined in grid.
    """
    if not grid or not grid[0]:
        return 0

    rows, cols = len(grid), len(grid[0])
    perimeter = 0

    if rows > 100 or cols > 100:
        raise ValueError("Grid exceed the maximum limit of 100x100")

    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 1:
                perimeter += 4  # Assume all four sides are land

                # Check left neighbor
                if j > 0 and grid[i][j - 1] == 1:
                    perimeter -= 2

                # Check top neighbor
                if i > 0 and grid[i - 1][j] == 1:
                    perimeter -= 2

    return perimeter
