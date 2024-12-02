#!/usr/bin/python3
""" Island Perimeter """


def island_perimeter(grid):
    """ Island Perimeter """
    counter = 0
    grid_max = len(grid) - 1  # Index of the last list in the grid
    lst_max = len(grid[0]) - 1  # Index of the last square in the list

    for lst_idx, lst in enumerate(grid):
        for square_idx, square in enumerate(lst):
            if square == 1:
                # left and right
                if square_idx == 0:
                    # left side
                    counter += 1

                    # right side
                    if lst[square_idx + 1] == 0:
                        counter += 1
                elif square_idx == lst_max:
                    # left side
                    if lst[square_idx - 1] == 0:
                        counter += 1

                    # right side
                    counter += 1
                else:
                    # left side
                    if lst[square_idx - 1] == 0:
                        counter += 1

                    # right side
                    if lst[square_idx + 1] == 0:
                        counter += 1

                # top and bottom
                if lst_idx == 0:
                    # top side
                    counter += 1

                    # bottom side
                    if grid[lst_idx + 1][square_idx] == 0:
                        counter += 1
                elif lst_idx == grid_max:
                    # top side
                    if grid[lst_idx - 1][square_idx] == 0:
                        counter += 1

                    # bottom side
                    counter += 1
                else:
                    # top side
                    if grid[lst_idx - 1][square_idx] == 0:
                        counter += 1

                    # bottom side
                    if grid[lst_idx + 1][square_idx] == 0:
                        counter += 1

    return counter
