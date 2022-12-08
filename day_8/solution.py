import numpy as np

def load_data(filename):
    """
        Load data from file.

        Args:
            * filename (str): file's name.

        Returns:
            * (np.ndarray): resulting grid.
    """
    grid = []

    with open(filename, "r") as f:
        data = f.read().splitlines()
    
    grid = [
        list(
            map(
                int,
                list(row)
            )
        )
        for row in data
    ]

    return np.array(grid)

def step_1():
    """
        Step 1 implementation.

        Returns:
            * (int): step 1 solution.
    """
    grid = load_data("./input_1.txt")

    counter = 0
    for i in range(grid.shape[0]):
        for j in range(grid.shape[1]):
            height = grid[i][j]

            if j - 1 > -1: trees_height_left = grid[i, j - 1:: -1]
            else: trees_height_left = [-1]
                
            if i - 1 > -1: trees_height_top = grid[i - 1:: -1, j]
            else: trees_height_top = [-1]

            if j + 1 < len(grid[0]): trees_height_right = grid[i, j + 1:]
            else: trees_height_right = [-1]

            if i + 1 < len(grid): trees_height_bottom = grid[i + 1:, j]
            else: trees_height_bottom = [-1]

            if (
                np.all(trees_height_left   < height) or
                np.all(trees_height_top    < height) or
                np.all(trees_height_right  < height) or
                np.all(trees_height_bottom < height)
            ):
                counter += 1

    return counter

def step_2():
    """
        Step 2 implementation.

        Returns:
            * (int): step 2 solution.
    """
    grid = load_data("./input_1.txt")

    scenic_scores = []
    for i in range(grid.shape[0]):
        for j in range(grid.shape[1]):
            height = grid[i, j]

            if j - 1 > -1: trees_height_left = grid[i, j - 1:: -1]
            else: trees_height_left = []
                
            if i - 1 > -1: trees_height_top = grid[i - 1:: -1, j]
            else: trees_height_top = []

            if j + 1 < len(grid[0]): trees_height_right = grid[i, j + 1:]
            else: trees_height_right = []

            if i + 1 < len(grid): trees_height_bottom = grid[i + 1:, j]
            else: trees_height_bottom = []

            if (
                len(trees_height_left  ) == 0 or
                len(trees_height_top   ) == 0 or 
                len(trees_height_right ) == 0 or 
                len(trees_height_bottom) == 0
            ):
                scenic_score = 0
            else:
                scenic_score = 1
                for direction in [
                    trees_height_left  , 
                    trees_height_top   ,
                    trees_height_right ,
                    trees_height_bottom
                ]:
                    trees_in_sight = 0
                    for tree_height in direction:
                        trees_in_sight += 1
                        if height <= tree_height:
                            break
                    scenic_score *= trees_in_sight

            scenic_scores.append(scenic_score)
    
    return max(scenic_scores)
            
if __name__ == "__main__":
    res_step_1 = step_1()
    print(res_step_1)

    res_step_2 = step_2()
    print(res_step_2)