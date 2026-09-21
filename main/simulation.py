import time
import subprocess
import msvcrt
import random
from functions import next_generation, display_grid


def generate_random_grid(rows: int, cols: int, density: float = 0.3):
    """
    Generate a random grid and save it to a text file.
    Each cell has a probability specified by density of being alive.
    Alive cells are represented by '@' and dead cells by '*'.
    Args:
        rows: Number of rows in the generated grid.
        cols: Number of columns in the generated grid.
        density: Probability that a cell will be alive. The default value is 0.3 (30%).
    Returns: None. The generated grid is saved to 'glider.txt'.
    """
    with open("glider.txt", "w") as file:
        for _ in range(rows):
            row = ""
            for _ in range(cols):
                # The cell is alive if the number is less than density.
                if random.random() < density:
                    row += "@"
                else:
                    row += "*"
            # Write the pattern to file
            file.write(row + "\n")
    print("Random World Generated and saved to the txt file.")


def parse_grid(filename: str) -> list[list[bool]]:
    """
    Read the grid from a text file.
    The '@' character represents an alive cell (True), while '*' represents a dead cell (False).
    Args:
      filename: Name of the text file containing the grid.
    Returns: A 2D list of Boolean values representing the grid.
    """
    # Create random integer in range 10 to 20 for the rows and cols
    rows = cols = random.randint(10, 20)
    generate_random_grid(rows, cols)
    try:
        with open(filename, "r") as file:
            # Convert @ to True and * to False for each cell
            grid = [[cell == "@" for cell in line.strip()] for line in file]
    except FileNotFoundError:
        print(f"File '{filename}' was not found")
        return []
    return grid


def global_statistics(current_grid: list[list[bool]], next_grid: list[list[bool]]) -> None:
    """
    Calculate and display statistics for the current generation.
    The function counts:- The number of living cells in the current generation.
                        - The number of cells that become alive.
                        - The number of cells that die.
    Args:
        current_grid: The current generation of the grid.
        next_grid: The next generation of the grid.
    Returns: None. The statistics are printed to the terminal.
    """
    living_cells = 0
    births = 0
    deaths = 0
    for row in range(len(current_grid)):
        for col in range(len(current_grid[0])):
            current_cell = current_grid[row][col]
            next_cell = next_grid[row][col]
            # Count cells that are alive in the current generation
            if current_cell:
                living_cells += 1
            # A birth occurs when a dead cell becomes alive
            if not current_cell and next_cell:
                births += 1
            # A death occurs when a living cell becomes dead
            elif not next_cell and current_cell:
                deaths += 1
    # Display the calculated statistics
    print("Number of living cells: ", living_cells)
    print("Births in the current generation: ", births)
    print("Deaths in the current generation: ", deaths)


def run_simulation(filename: str, generations: int) -> None:
    """
    The simulation reads the initial grid, displays each generation, calculates statistics, and generates the next generation.
    The simulation can be stopped early by pressing any key.
    Args:
        filename: Name of the file containing the initial grid.
        generations: Number of generations to simulate.
    Returns: None. The simulation output is displayed in the terminal.
    """

    grid = parse_grid(filename)
    # Create a grid to keep track of how many consecutive generations each cell has remained dead.
    death_count = []
    for row in grid:
        death_count.append([0] * len(row))
    for generation in range(generations):
        # Clear the terminal
        subprocess.run("cls", shell=True)
        # Print the generation number
        print(f"Generation {generation + 1}")
        # Display the grid
        display_grid(grid, death_count)
        # Wait for 0.5 second
        time.sleep(0.5)

        # Generate the next grid
        next_grid = next_generation(grid)
        for row in range(len(next_grid)):
            for col in range(len(next_grid[0])):
                # Reset the death count when the cell is alive
                if next_grid[row][col]:
                    death_count[row][col] = 0
                # Increase the death count when the cell is dead
                else:
                    death_count[row][col] += 1
        global_statistics(grid, next_grid)
        # Replace the current grid with the newly generated grid
        grid = next_grid
        # Check if a key has been pressed
        if msvcrt.kbhit():
            msvcrt.getch()
            print("\nSimulation terminated by user.")
            return
