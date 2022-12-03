def load_data(filename):
    """
        Load data from file.

        Args:
            * filename (str): file's name.

        Returns:
            * (list): file's processed data.
    """
    with open(filename, "r") as f:
        data = f.readlines()
        
    processed_data, last_idx = [], 0
    for item, idx in zip(data, range(0, len(data))):
        if item == "\n": 
            calories_per_elf = sum(
                [
                    int(d)
                    for d in data[last_idx: idx]
                ]
            )
            processed_data.append(calories_per_elf)
            last_idx = idx + 1

    return processed_data

def step_1():
    """
        Step 1 implementation.

        Returns:
            * (int): step 1 solution.
    """
    data = load_data("./input_1.txt")
    return max(data)

def step_2():
    """
        Step 2 implementation.

        Returns:
            * (int): step 2 solution.
    """
    data = load_data("./input_1.txt")
    return sum(
        sorted(data)[-3:]
    )
        
if __name__ == "__main__":
    res_step_1 = step_1()
    print(res_step_1)

    res_step_2 = step_2()
    print(res_step_2)
    