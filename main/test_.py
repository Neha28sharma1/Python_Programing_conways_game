from functions import create_grid, count_neighbors, next_generation, display_grid


def test_create_grid():
    """
    Test that create_grid() creates a grid with the requested number of rows and columns.
    The newly created grid should contain only False values.
    """
    grid = create_grid(3, 4)

    expected_grid = [
        [False, False, False, False],
        [False, False, False, False],
        [False, False, False, False],
    ]
    assert grid == expected_grid


def test_count_neighbors():
    """
    Test that count_neighbors() correctly counts the number of alive neighboring cells around a specified cell.
    """
    grid = [
        [False, False, False],
        [True, True, True],
        [False, False, True],
    ]

    count = count_neighbors(grid, 1, 1)
    assert count == 3


def test_next_generation():
    """
    Test that next_generation() correctly applies the rules to produce the next generation.
    """
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


def test_display_grid(capsys):
    """
    Test that display_grid() prints the grid using the expected ANSI colour codes.
    capsys is a pytest fixture used to capture text printed to the terminal.
    """
    grid = [[True, False], [False, True]]
    death_count = [[0, 1], [10, 0]]
    display_grid(grid, death_count)
    # Capture everything printed to the terminal
    captured = capsys.readouterr()
    # Alive cells should be blue, while dead cells should use the appropriate red gradient.
    expected = (
        "\033[38;2;0;0;200m◼\033[0m "
        "\033[38;2;160;0;0m◼\033[0m \n"
        "\033[38;2;255;0;0m◼\033[0m "
        "\033[38;2;0;0;200m◼\033[0m \n"
    )
    assert captured.out == expected
