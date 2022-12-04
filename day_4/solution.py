def load_data(filename):
    """
        Load data from file.

        Args:
            * filename (str): file's name.

        Returns:
            * (list): file's data.
    """
    data = []
    with open(filename, "r") as f:
        for row in f.read().splitlines():
            splitted_row = row.split(",")
            data.append(
                [
                    list(
                        map(
                            int,
                            sr.split("-")
                        )
                    )
                    for sr in splitted_row
                ]
            )
    return data

def step_1():
    """
        Step 1 implementation.

        Returns:
            * (int): step 1 solution.
    """
    pairs = load_data("./input_1.txt")

    num_fully_contains = 0
    for pair in pairs:
        first_pair = set(
            range(
                pair[0][0], 
                pair[0][1] + 1
            )
        )
        second_pair = set(
            range(
                pair[1][0], 
                pair[1][1] + 1
            )
        )
        
        if (first_pair.issubset(second_pair) or 
            first_pair.issuperset(second_pair)):
           num_fully_contains += 1

    return num_fully_contains

def step_2():
    """
        Step 1 implementation.

        Returns:
            * (int): step 1 solution.
    """
    pairs = load_data("./input_1.txt")

    num_overlaps = 0
    for pair in pairs:
        first_pair = set(
            range(
                pair[0][0], 
                pair[0][1] + 1
            )
        )
        second_pair = set(
            range(
                pair[1][0], 
                pair[1][1] + 1
            )
        )
        
        if len(first_pair.intersection(second_pair)) > 0:
            num_overlaps += 1

    return num_overlaps

if __name__ == "__main__":
    res_step_1 = step_1()
    print(res_step_1)

    res_step_2 = step_2()
    print(res_step_2)