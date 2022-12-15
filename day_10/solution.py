def load_data(filename):
    """
        Load data from file.

        Args:
            * filename (str): file's name.

        Returns:
            * (list): processed data.
    """
    with open(filename, "r") as f:
        data = [
            row
            for row in f.read().splitlines()
        ]

    processed_data = []
    for row in data:
        splitted_row = row.split(" ")
        if len(splitted_row) > 1:
            processed_data.append(
                [
                    splitted_row[0],
                    int(splitted_row[1])
                ]
            )
        else:
            processed_data.append(
                [
                    splitted_row[0]
                ]
            )

    return processed_data


def step_1():
    """
        Step 1 implementation.

        Returns:
            * (int): step 1 solution.
    """
    data = load_data("./input_1.txt")

    signal_strenght_per_cycle = {}
    x, current_cycle = 1, 0
    for cmd in data:
        if cmd[0] == "noop":
            current_cycle += 1
            if current_cycle in [20, 60, 100, 140, 180, 220]:
                signal_strenght_per_cycle[current_cycle] = x
        else:
            current_cycle += 1
            if current_cycle in [20, 60, 100, 140, 180, 220]:
                signal_strenght_per_cycle[current_cycle] = x
            current_cycle += 1
            if current_cycle in [20, 60, 100, 140, 180, 220]:
                signal_strenght_per_cycle[current_cycle] = x
            x += cmd[1]

    return sum(
        [
            k * v
            for k, v in signal_strenght_per_cycle.items()
        ]
    )


def step_2():
    """
        Step 2 implementation.

        Returns:
            * (str): step 2 solution.
    """
    data = load_data("./input_1.txt")

    crt = [
        [
            "."
            for col in range(40)
        ]
        for row in range (6)
    ]

    signal_strenght_per_cycle = {}
    x, current_cycle = 1, 0
    for cmd in data:
        if cmd[0] == "noop":
            current_cycle += 1
            signal_strenght_per_cycle[current_cycle] = x
        else:
            for _ in range(2):
                current_cycle += 1
                signal_strenght_per_cycle[current_cycle] = x
            x += cmd[1]

    for k, v in signal_strenght_per_cycle.items():
        current_row = int(k - 1) // 40
        current_col = int(k - 1) % 40

        sprite_col_range = list(
            range(v - 1, v + 2)
        )

        if current_col in sprite_col_range:
            crt[current_row][current_col] = "#"

    return crt


if __name__ == "__main__":
    res_step_1 = step_1()
    print(res_step_1)

    res_step_2 = step_2()
    for row in range(len(res_step_2)):
        for col in range(len(res_step_2[0])):
            print(res_step_2[row][col], end="")
        print()
