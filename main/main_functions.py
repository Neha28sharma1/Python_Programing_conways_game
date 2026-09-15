
def create_grid(rows: int, cols: int) -> list[list[int]]:
    grid:list[list[int]] = []  #maingrid
    for _ in range(rows):
        new_row :list[int]= []
        for _ in range(cols):
            new_row.append(0) # Initialize each cell with bool false 
        grid.append(new_row)
    return grid
    
    
def count_neighbors(grid: list[list[int]], row: int, col: int) -> int:
    counter = 0
    
    for row_steps in [-1, 0, 1]: # -1 for row above , 0 for same row and +1 for row down 
        for col_steps in [-1, 0, 1]: # -1 for col above , 0 for same col and +1 for col down 
            neighbor_row = row + row_steps
            neighbor_col = col + col_steps
            
            if neighbor_row == row and neighbor_col == col: # we dnt want to count the current cell as neighbor 
                continue  # Skip the cell itself
            if neighbor_row < 0 or neighbor_row >= len(grid) or neighbor_col < 0 or neighbor_col >= len(grid[0]):
                continue #we do not want to count corners
            if grid[neighbor_row][neighbor_col] == 1:
                counter = counter + 1
    return counter  
            
def next_generation(grid: list[list[int]]) -> list[list[int]]:
    
    new_grid = create_grid(len(grid), len(grid[0]))  #grid for the next generation
    
    for row in range(len(grid)): #Go through the positions of all the rows in grid, one by one
        for col in range(len(grid[0])): #grid[0] represents the first row and we want to know how many col are there in the row 
            cell = grid[row][col]  # to get the value of one specific cell from the grid so that we can later check if it is true or false 
            neighbors = count_neighbors(grid,row,col)
            
            if cell == 1 and neighbors < 2:  # rules of Conway’s Game of Life 
                cell = 0
            elif cell == 1 and (neighbors == 2 or neighbors == 3):
                cell = 1
            elif cell == 1 and neighbors >3:
                cell = 0
            elif cell == 0 and neighbors == 3:
                cell = 1
            new_grid[row][col] = cell # replace the current value of the cell and adds the new value in new grid
                
    return new_grid


def display_grid(grid: list[list[bool]]) -> None:
    for row in grid:
        for cell in row:
            if cell == 1:
                print("@")
            else :
                print("*")
                    
                
            
                