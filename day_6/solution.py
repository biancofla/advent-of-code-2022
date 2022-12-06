def load_data(filename):
    """
        Load data from file.

        Args:
            * filename (str): file's name.

        Returns:
            * (str): file's data.
    """
    with open(filename, "r") as f:
        data = f.read()
    return data

def step_1():
    """
        Step 1 implementation.

        Returns:
            * (int): step 1 solution.
    """
    datastream = load_data("./input_2.txt")

    splitted_datastream = _split_using_moving_window(
        datastream, 
        4
    )

    occurrences = _compute_char_occurences(splitted_datastream)

    start_of_packet_marker = 4
    for o, idx in zip(occurrences, range(len(occurrences))):
        condition = [
            True if item == 1 
            else False 
            for item in o.values()
        ]
        if all(condition):
            start_of_packet_marker += idx
            break

    return start_of_packet_marker

def step_2():
    """
        Step 2 implementation.

        Returns:
            * (int): step 2 solution.
    """
    datastream = load_data("./input_2.txt")

    splitted_datastream = _split_using_moving_window(
        datastream, 
        14
    )

    occurrences = _compute_char_occurences(splitted_datastream)

    start_of_message_marker = 14
    for o, idx in zip(occurrences, range(len(occurrences))):
        condition = [
            True if item == 1 
            else False 
            for item in o.values()
        ]
        if all(condition):
            start_of_message_marker += idx
            break
    
    return start_of_message_marker

def _split_using_moving_window(data, window_size):
    """
        Split a list using a moving window of a specific size.

        Args:
            * data (list): input list.
            * window_size (int): size of the moving window.

        Returns:
            * (list): splitted list.
    """
    splitted_data = []

    for idx in range(0, len(data) - window_size + 1):
        splitted_data.append(
            data[idx: idx + window_size]
        )

    return splitted_data

def _compute_char_occurences(data):
    """
        Compute occurrences for each string in a list.

        Args:
            * data (list): list containing strings.

        Returns:
            * (list): occurrences per string.
    """
    occurences = []

    for string in data:
        occurences_per_char = {}

        for c in string:
            if c not in occurences_per_char.keys():
                occurences_per_char[c] = 0
            occurences_per_char[c] += 1

        occurences.append(occurences_per_char)

    return occurences

if __name__ == "__main__":
    res_step_1 = step_1()
    print(res_step_1)

    res_step_2 = step_2()
    print(res_step_2)
    