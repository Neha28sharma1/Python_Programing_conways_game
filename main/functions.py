def create_grid(rows: int, cols: int) -> list[list[bool]]:
    grid = []  # main grid
    for _ in range(rows):
        new_row = []  # grid for each row
        for _ in range(cols):
            new_row.append(False)  # Initialize each cell with bool false
        grid.append(new_row)
    return grid


def count_neighbors(grid: list[list[bool]], row: int, col: int) -> int:
    """
    Count the number of alive neighboring cells around a given cell.
    Each cell can have up to 8 neighbors: above, below, left, right, and the four diagonal positions.
    Args:
        grid: The current grid.
        row: Row index of the cell.
        col: Column index of the cell.
    Returns: The number of alive neighbors surrounding the specified cell.
    """
    counter = 0

    for row_steps in [
        -1,
        0,
        1,
    ]:  # -1 for row above , 0 for same row and +1 for row down
        for col_steps in [
            -1,
            0,
            1,
        ]:  # -1 for col above , 0 for same col and +1 for col down
            neighbor_row = row + row_steps
            neighbor_col = col + col_steps

            if (
                neighbor_row == row and neighbor_col == col
            ):  # we dnt want to count the current cell as neighbor
                continue  # Skip the cell itself
            if (
                neighbor_row < 0
                or neighbor_row >= len(grid)
                or neighbor_col < 0
                or neighbor_col >= len(grid[0])
            ):
                continue
            if grid[neighbor_row][neighbor_col]:
                counter = counter + 1
    return counter


def next_generation(grid: list[list[bool]]) -> list[list[bool]]:

    new_grid = create_grid(len(grid), len(grid[0]))  # grid for the next generation

    for row in range(
        len(grid)
    ):  # Go through the positions of all the rows in grid, one by one
        for col in range(
            len(grid[0])
        ):  # grid[0] represents the first row and we want to know how many col are there in the row
            cell = grid[
                row
            ][
                col
            ]  # to get the value of one specific cell from the grid so that we can later check if it is true or false
            neighbors = count_neighbors(grid, row, col)

            if cell == True and neighbors < 2:  # rules of Conway’s Game of Life
                cell = False
            elif cell and (neighbors == 2 or neighbors == 3):
                cell = True
            elif cell == True and neighbors > 3:
                cell = False
            elif not cell and neighbors == 3:
                cell = True
            new_grid[row][col] = (
                cell  # replace the current value of the cell and adds the new value in new grid
            )

    return new_grid


def display_grid(grid: list[list[bool]]) -> None:
    for row in grid:
        for cell in row:
            if cell == True:
                print("@", end="")
            else:
                # Dead cells in red gradient based on death count
                count = death_count[row][cell]
                # Limit the count to the range 1–10
                count = min(count, 10)
                # Red intensity increases as death count increases
                red = int(150 + (105 * (count) / 10))
                # Keep green and blue low to create shades of red
                green = 0
                blue = 0
                RED_GRADIENT = f"\033[38;2;{red};{green};{blue}m"
                print(f"{RED_GRADIENT}◼{RESET}", end=" ")
        print()
