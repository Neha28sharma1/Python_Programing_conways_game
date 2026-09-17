from functions import create_grid, count_neighbors, next_generation


def test_create_grid():
    grid = create_grid(3, 4)

    expected_grid = [
        [False, False, False, False],
        [False, False, False, False],
        [False, False, False, False],
    ]
    assert grid == expected_grid


def test_count_neighbors():
    grid = [[False, False, False], [True, True, True], [False, False, True]]

    count = count_neighbors(grid, 1, 1)
    assert count == 3


def test_next_generation():
    grid = [
        [False, False, False, False],
        [True, False, False, False],
        [True, True, True, True],
    ]

    newgrid = next_generation(grid)

    assert newgrid == [
        [False, False, False, False],
        [True, False, True, False],
        [True, True, True, False],
    ]
