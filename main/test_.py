
from functions import create_grid,count_neighbors,next_generation

def test_create_grid():
    grid = create_grid(3,4)
    
    expected_grid = [[False,False,False,False],
                     [False,False,False,False],
                     [False,False,False,False]]
    assert grid == expected_grid
    
def test_count_neighbors():
   
    grid = [[0,0,0],
            [1,1,1],
            [0,0,1]]
    
    count = count_neighbors(grid,1,1)
    assert count == 3
    
def test_next_generation():
    grid = [[0,0,0,0],
            [1,0,0,0],
            [1,1,1,1]]
    
    newgrid=next_generation(grid)
    
    assert newgrid == [
    [0, 0, 0, 0],
    [1, 0, 1, 0],
    [1, 1, 1, 0],
]