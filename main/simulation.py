import time
import subprocess
import msvcrt
from functions import next_generation,display_grid

def parse_grid(filename:str) -> list[list[bool]]:
     # Read each line, remove the newline character,and convert the line into a list of characters
    with open(filename, "r") as file:
        # Convert @ to True and * to False for each cell
        grid = [[cell == "@" for cell in line.strip()]
            for line in file]
    return grid



def run_simulation(filename: str, generations: int) -> None:

    grids = parse_grid(filename)

    for generation in range(generations):
        # Clear the terminal
        subprocess.run("cls", shell=True)
       
        # Print the generation number
        print(f"Generation {generation+1}")
        display_grid(grids)
       
        # Wait for one second
        time.sleep(0.5)

        # Check if a key has been pressed
        if msvcrt.kbhit():
            msvcrt.getch()
            print("\nSimulation terminated by user.")
            return

        # Generate the next grid
        grids = next_generation(grids)

if __name__ == "__main__":
    run_simulation("configurationfile.txt", 100)


