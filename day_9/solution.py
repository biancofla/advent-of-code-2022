def load_data(filename):
    """
        Load data from file.

        Args:
            * filename (str): file's name.

        Returns:
            * (list): motion's data.
    """
    with open(filename, "r") as f:
        data = [
            row.split(" ")
            for row in f.read().splitlines()
        ]
    return data

def step_1():
    """
        Step 1 implementation.

        Returns:
            * (int): step 1 solution.
    """
    motions = load_data("./input_1.txt")

    head_position, tail_position = [0, 0], [0, 0]

    tail_unique_positions = set()
    tail_unique_positions.add("0,0")

    for motion in motions:
        direction = motion[0]
        length    = int(motion[1])

        for _ in range(1, length + 1):
            new_head_position = head_position.copy()

            if   direction == "L":
                new_head_position[0] -= 1
            elif direction == "U":
                new_head_position[1] += 1
            elif direction == "R":
                new_head_position[0] += 1
            else:
                new_head_position[1] -= 1

            is_adjacent = _check_adjacency(
                new_head_position,
                tail_position
            )

            if not is_adjacent:
                deltas = _compute_xy_delta(
                    tail_position,
                    new_head_position
                )
                tail_position[0] += deltas[0]
                tail_position[1] += deltas[1]

                tail_unique_positions.add(
                    f"{tail_position[0]},{tail_position[1]}"
                )

            head_position = new_head_position

    return len(tail_unique_positions)

def step_2():
    """
        Step 2 implementation.

        Returns:
            * (int): step 2 solution.
    """
    motions = load_data("./input_1.txt")

    positions = [[0, 0] for _ in range(10)]

    tail_unique_positions = set()
    tail_unique_positions.add("0,0")

    for motion in motions:
        direction = motion[0]
        length    = int(motion[1])

        for _ in range(length):    
            if   direction == "L":
                positions[0][0] -= 1
            elif direction == "U":
                positions[0][1] += 1
            elif direction == "R":
                positions[0][0] += 1
            else:
                positions[0][1] -= 1

            for idx in range(len(positions) - 1):
                head_position = positions[idx    ]
                tail_position = positions[idx + 1]

                if (
                    not _check_adjacency(
                        head_position,
                        tail_position
                    )
                ):
                    deltas = _compute_xy_delta(
                        tail_position,
                        head_position
                    )
                    positions[idx + 1][0] += deltas[0]
                    positions[idx + 1][1] += deltas[1]

                    tail_unique_positions.add(
                        f"{positions[-1][0]},{positions[-1][1]}"
                    )
                else:
                    break

    return len(tail_unique_positions)

def _check_adjacency(position_1, position_2):
    """
        Check if two positions are adjacent.

        Args
            * position_1 (list): first position.
            * position_2 (list): second position.

        Returns:
            * (bool): True, if the the two positions
            are ajacent; False, otherwise.
    """
    adjacency_positions = [
        # Same position.
        position_2,
        # Left.
        [position_2[0] - 1, position_2[1]],
        # Top.
        [position_2[0], position_2[1] + 1],
        # Right.
        [position_2[0] + 1, position_2[1]],
        # Bottom.
        [position_2[0], position_2[1] - 1],
        # Top-Left.
        [position_2[0] - 1, position_2[1] + 1],
        # Top-Right.
        [position_2[0] + 1, position_2[1] + 1],
        # Bottom-Left.
        [position_2[0] - 1, position_2[1] - 1],
        # Bottom-Right.
        [position_2[0] + 1, position_2[1] - 1],
    ]
    for ap in adjacency_positions:
        if (
            position_1[0] == ap[0] and
            position_1[1] == ap[1]
        ):
            return True
    return False

def _compute_xy_delta(position_1, position_2):
    """
        Compute the step necessary to one position
        to reach a second position.

        Args
            * position_1 (list): first position.
            * position_2 (list): second position.

        Returns:
            * (list): step to be performed.
    """
    deltas = [0, 0]

    delta_x = position_2[0] - position_1[0]
    delta_y = position_2[1] - position_1[1]

    # Same position.
    if delta_x == 0 and delta_y == 0: deltas = [0, 0]

    if   delta_x == 0:
        # Same row. Move up or down.
        if delta_y > 0: deltas = [0,  1]
        else:           deltas = [0, -1]
    elif delta_y == 0:
        # Same column. Move right or left.
        if delta_x > 0: deltas = [ 1, 0]
        else:           deltas = [-1, 0]
    else:
        # Move diagonally.
        if delta_x > 0 and delta_y > 0: deltas = [ 1,  1]
        if delta_x < 0 and delta_y < 0: deltas = [-1, -1]
        if delta_x > 0 and delta_y < 0: deltas = [ 1, -1]
        if delta_x < 0 and delta_y > 0: deltas = [-1,  1]

    return deltas

if __name__ == "__main__":
    res_step_1 = step_1()
    print(res_step_1)

    res_step_2 = step_2()
    print(res_step_2)

