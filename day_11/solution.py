from functools import reduce

class Archive:

    def __init__(self):
        self.monkeys = []

    def add_monkey(self, monkey):
        self.monkeys.append(monkey)

    def do_one_round(self, manage_worry_level=True):
        """
            Simulate one round.

            Args:
                * manage_worry_level (bool, default=True): if True, the 
                worry level is managed dividing it by three and trunca-
                ting the result to the closest integer; if False, it is 
                managed with a modulo operation.
        """
        # Compute the product of each divisible factor.
        super_mod = reduce(
            lambda a, b: a * b,
            [m.get_divisible_by() for m in self.monkeys]
        )
        for monkey in self.monkeys:
            for idx in range(monkey.get_items_len()):
                throw_to = monkey.inspect_item(idx, super_mod, manage_worry_level)
                self.monkeys[throw_to].add_item(
                    monkey.get_item_in_pos(idx)
                )
            monkey.set_items([])

    def get_two_most_active_monkeys(self):
        """
            Get the product of the number of inspections of the two most 
            active monkeys.

            Returns:
                * (int): product of the number of inspections of the two 
                most active monkeys.
        """
        num_inspections_per_monkey = sorted(
            [
                monkey.get_num_inspections()
                for monkey in self.monkeys
            ]
        )
        return num_inspections_per_monkey[-1] * num_inspections_per_monkey[-2]

    def __str__(self):
        res = []
        for monkey, idx in zip(self.monkeys, range(len(self.monkeys))):
            res.append(f"Monkey #{idx}\n")
            res.append(f"{monkey}\n")
        return "".join(res)


class Monkey:

    def __init__(
        self,
        items,
        operation,
        operation_factor,
        divisible_by,
        throw_to
    ):
        self.items            = items
        self.operation        = operation
        self.operation_factor = operation_factor
        self.divisible_by     = divisible_by
        self.throw_to         = throw_to
        self.num_inspections  = 0

    def set_items(self, items):
        self.items = items

    def get_items_len(self):
        return len(self.items)

    def add_item(self, item):
        self.items.append(item)

    def get_item_in_pos(self, idx):
        return self.items[idx]

    def get_divisible_by(self):
        return self.divisible_by

    def get_num_inspections(self):
        return self.num_inspections

    def inspect_item(self, idx, super_mod, manage_worry_level=True):
        self.num_inspections += 1

        if   self.operation == "+":
            worry_level_after_inspection = \
                self.items[idx] + self.operation_factor
        elif self.operation == "*":
            worry_level_after_inspection = \
                self.items[idx] * self.operation_factor
        else:
            worry_level_after_inspection = \
                self.items[idx] * self.items[idx]

        if manage_worry_level:
            worry_level_after_inspection = \
                int(worry_level_after_inspection / 3)
        else:
            # This operation doesn't affect any other successive test.
            worry_level_after_inspection = \
                worry_level_after_inspection % super_mod

        self.items[idx] = worry_level_after_inspection

        if worry_level_after_inspection % self.divisible_by == 0:
            return self.throw_to[0]
        return self.throw_to[1]
        

    def __str__(self):
        return "".join(
            [
                f"Items           : {self.items}\n",
                f"Operation       : {self.operation}\n",
                f"Operation Factor: {self.operation_factor}\n",
                f"Division Factor : {self.divisible_by}\n",
                f"Throw to        : {self.throw_to}\n",
                f"# Inspections   : {self.num_inspections}\n",
            ]
        )


def load_data(filename):
    """
        Load data from file.

        Args:
            * filename (str): file's name.

        Returns:
            * (Archive): object containing all processed data.
    """
    archive = Archive()

    with open(filename, "r") as f:
        data = f.read().splitlines()

        for idx in range(len(data)):
            current_row = data[idx]
            if "Monkey" in current_row:
                items_raw        = data[idx + 1]
                operation_raw    = data[idx + 2]
                test_raw         = data[idx + 3]
                test_success_raw = data[idx + 4]
                test_failure_raw = data[idx + 5]

                items_raw = items_raw.replace(
                    "  Starting items: ",
                    ""
                )
                items = list(
                    map(
                        int,
                        items_raw.split(",")
                    )
                )

                operation_raw = operation_raw.replace(
                    "  Operation: new = old ",
                    ""
                )
                operation_raw_splitted = operation_raw.split(" ")
                operation              = operation_raw_splitted[0]
                operation_factor       = operation_raw_splitted[1]
                if operation_factor == "old":
                    operation        = "ˆ"
                    operation_factor = 2
                else:
                    operation_factor = int(operation_factor)

                test_raw = test_raw.replace(
                    "  Test: divisible by ",
                    ""
                )
                divisible_by = int(test_raw)

                test_success_raw = test_success_raw.replace(
                    "    If true: throw to monkey ",
                    ""
                )
                test_failure_raw = test_failure_raw.replace(
                    "    If false: throw to monkey ",
                    ""
                )
                throw_to = [
                    int(test_success_raw),
                    int(test_failure_raw)
                ]

                monkey = Monkey(
                    items,
                    operation,
                    operation_factor,
                    divisible_by,
                    throw_to
                )
                archive.add_monkey(monkey)

    return archive


def step_1():
    """
        Step 1 implementation.

        Returns:
            * (int): step 1 solution.
    """
    archive = load_data("./input_1.txt")

    for _ in range(20):
        archive.do_one_round()

    return archive.get_two_most_active_monkeys()

def step_2():
    """
        Step 2 implementation.

        Returns:
            * (int): step 2 solution.
    """
    archive = load_data("./input_1.txt")

    for _ in range(10000):
        archive.do_one_round(manage_worry_level=False)

    return archive.get_two_most_active_monkeys()

if __name__ == "__main__":
    res_step_1 = step_1()
    print(res_step_1)

    res_step_2 = step_2()
    print(res_step_2)
