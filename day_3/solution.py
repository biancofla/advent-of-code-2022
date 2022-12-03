ALPHABET = "abcdefghijklmnopqrstuvwxyz"

def load_data(filename):
    data = []

    with open(filename, "r") as f:
        for row in f.read().splitlines():
            data.append(row)
    
    return data

def step_1():
    """
        Step 1 implementation.

        Returns:
            * (int): step 1 solution.
    """
    rucksacks = load_data("./input_1.txt")

    total_priority = 0
    for rucksack in rucksacks:
        num_items = len(rucksack)

        first_compartment  = set(
            rucksack[0: num_items // 2]
        )
        second_compartment = set(
            rucksack[num_items // 2:  ]
        )

        compartment_intersection = \
            first_compartment.intersection(second_compartment).pop()
        
        total_priority += _item_to_priority(compartment_intersection)

    return total_priority
    
def step_2():
    """
        Step 2 implementation.

        Returns:
            * (int): step 2 solution.
    """
    rucksacks = load_data("./input_1.txt")

    total_priority = 0
    for i in range(0, len(rucksacks), 3):
        triplet = [set(r) for r in rucksacks[i: i + 3]]
        
        badge = triplet[0].intersection(triplet[1]).intersection(triplet[2]).pop()
        
        total_priority += _item_to_priority(badge)

    return total_priority

def _item_to_priority(item):
    """
        Convert rucksack item to priority.

        Args:
            * (str): rucksack's item.

        Returns:
            * (int): item's priority.
    """
    is_lower_case = item.islower()

    if is_lower_case: 
        idx = ALPHABET.find(item)
        priority = idx + 1
    else:
        idx = ALPHABET.find(item.lower())
        priority = idx + 1 + 26

    return priority

if __name__ == "__main__":
    res_step_1 = step_1()
    print(res_step_1)

    res_step_2 = step_2()
    print(res_step_2)