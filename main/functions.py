


def create_grid(rows: int, cols: int) -> list[list[int]]:
    grid = [] # main grid 
    for _ in range(rows):
        new_row = [] # grid for each row 
        for _ in range(cols):
            new_row.append(0)  # Initialize each cell with 0
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
                continue
            if grid[neighbor_row][neighbor_col] == 1:
                counter = counter + 1
    return counter  
            