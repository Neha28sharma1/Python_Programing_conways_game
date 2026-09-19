import time
import subprocess
import msvcrt
import random
from functions import next_generation,display_grid

def generate_random_grid(rows: int, cols: int, density: float=0.3):
    with open("glider.txt","w") as file:
        for _ in range(rows):
            row=""
            for _ in range(cols):
                # 30% chance that each cell will be alive
                if random.random()<density: 
                    row+="@"
                else:
                    row+="*"
            # Write the pattern to file
            file.write(row+"\n")
    print("Random World Generated and saved to the txt file.")

def parse_grid(filename: str) -> list[list[bool]]:
    # Create random integer in range 10 to 20 for the rows and cols
    rows=cols=random.randint(10,50)
    generate_random_grid(rows,cols)
    try:
        with open(filename, "r") as file:
            # Convert @ to True and * to False for each cell
            grid = [[cell == "@" for cell in line.strip()]
                for line in file]
    except FileNotFoundError:
        print(f"File '{filename}' was not found")
    return grid

def global_statistics(current_grid: list[list[bool]],next_grid: list[list[bool]]) ->None:
    living_cells=0
    births=0
    deaths=0
    for row in range(len(current_grid)):
        for col in range(len(current_grid[0])):
            current_cell=current_grid[row][col]
            next_cell=next_grid[row][col]
            if current_cell:
                living_cells+=1
            if not current_cell and next_cell:
                births+=1
            elif not next_cell and current_cell:
                deaths+=1
    print("Number of living cells: ",living_cells)
    print("Births in the current generation: ",births)
    print("Deaths in the current generation: ",deaths)
            
def run_simulation(filename: str, generations: int) -> None:

    grid = parse_grid(filename)
    death_count=[]
    for row in grid:
        death_count.append([0]*len(row))
    for generation in range(generations):
        # Clear the terminal
        subprocess.run("cls", shell=True)       
        # Print the generation number
        print(f"Generation {generation+1}")
        # Display the grid
        display_grid(grid,death_count)       
        # Wait for 0.5 second
        time.sleep(0.5)

        # Generate the next grid
        next_grid = next_generation(grid)
        for row in range(len(next_grid)):
            for col in range(len(next_grid[0])):
                if next_grid[row][col]:
                    death_count[row][col]=0
                else:
                    death_count[row][col]+=1
        global_statistics(grid,next_grid)
        grid=next_grid
        # Check if a key has been pressed
        if msvcrt.kbhit():
            msvcrt.getch()
            print("\nSimulation terminated by user.")
            return

