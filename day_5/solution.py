def load_data(filename):
    """
        Load data from file.

        Args:
            * filename (str): file's name.

        Returns:
            * (list, list): starting stack raw data
            and rearrangement procedure raw data.
    """
    with open(filename, "r") as f:
        splitted_raw_data = f.read().splitlines()

    idx = splitted_raw_data.index("")
    # Starting stack raw data.
    raw_starting_stacks = splitted_raw_data[:idx]
    # Rearrangement procedure raw data.
    raw_rearrangement_procedure = splitted_raw_data[idx + 1:]

    # Process starting stack raw data.
    num_cranes = int(
        raw_starting_stacks[-1].split(" ")[-2]
    )
    starting_stacks = [
        [] 
        for _ in range(0, num_cranes)
    ]
    for i in range(idx - 2, -1, -1):
        cranes_row = raw_starting_stacks[i]
        for j, k in zip(range(0, len(cranes_row), 4), range(num_cranes)):
            if cranes_row[j] == "[":
                starting_stacks[k].append(
                    cranes_row[j + 1]
                )
    # Process rearrangement procedure raw data.
    rearrangement_procedure = []
    for row in raw_rearrangement_procedure:
        row = row.replace("move", "")
        row = row.replace("from", "")
        row = row.replace("to"  , "")

        rearrangement_procedure.append(
            [int(c) for c in row.split(" ") if c != ""]
        )
        
    return starting_stacks, rearrangement_procedure

def step_1():
    """
        Step 1 implementation.

        Returns:
            * (str): step 1 solution.
    """
    stacks, rearrangement_procedure = load_data("./input_1.txt")

    for movement in rearrangement_procedure:
        num_cranes = movement[0]
        move_from  = movement[1] - 1
        move_to    = movement[2] - 1

        for _ in range(0, num_cranes):
            popped_item = stacks[move_from].pop()
            stacks[move_to].append(popped_item)

    return "".join(
        [s[-1] for s in stacks if len(s) > 0]
    )

def step_2():
    """
        Step 2 implementation.

        Returns:
            * (str): step 2 solution.
    """
    stacks, rearrangement_procedure = load_data("./input_1.txt")

    for movement in rearrangement_procedure:
        num_cranes = movement[0]
        move_from  = movement[1] - 1
        move_to    = movement[2] - 1

        popped_items = stacks[move_from][-1: -num_cranes -1: -1]
        popped_items.reverse()
        stacks[move_to].extend(popped_items)
            
        stacks[move_from] = \
            stacks[move_from][:len(stacks[move_from]) - num_cranes]

    return "".join(
        [s[-1] for s in stacks if len(s) > 0]
    )

if __name__ == "__main__":
    res_step_1 = step_1()
    print(res_step_1)

    res_step_2 = step_2()
    print(res_step_2)