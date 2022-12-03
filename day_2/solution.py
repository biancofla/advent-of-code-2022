CONVERSION_TABLE = {
    "A": 0,
    "B": 1,
    "C": 2,
    "X": 0,
    "Y": 1,
    "Z": 2
}

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
            splitted_plays = row.split(" ")
            data.append(
                [
                    CONVERSION_TABLE[splitted_plays[0]],
                    CONVERSION_TABLE[splitted_plays[1]]
                ]
            )
    return data

def step_1():
    """
        Step 1 implementation.

        Returns:
            * (int): step 1 solution.
    """
    games = load_data("./input_1.txt")

    total_score = 0
    for g in games:
        total_score += _compute_score(g[0], g[1])

    return total_score

def step_2():
    """
        Step 2 implementation.

        Returns:
            * (int): step 2 solution.
    """
    games = load_data("./input_1.txt")

    total_score = 0
    for g in games:
        your_play = _compute_your_play(g[0], g[1])
        total_score += _compute_score(g[0], your_play)

    return total_score

def _compute_score(opponent_play, your_play):
    """
        Compute game score.

        Args:
            * opponent_play (int): opponent's play.
            * your_play (int): yours play.

        Returns:
            * (int): score obtained.

    """
    score = your_play + 1

    if (opponent_play + 1) % 3 == your_play:
        score += 6
    elif (your_play + 1) % 3 == opponent_play:
        score += 0
    else:
        score += 3

    return score

def _compute_your_play(opponent_play, game_result):
    """
        Compute play according to the the game result.

        Args:
            * opponent_play (int): opponent's play.
            * game_result (int): game's result.

        Returns:
            * (int): computed play.
    """
    your_play = 0

    if   game_result == 0:
        your_play = opponent_play - 1
        if your_play < 0: your_play = 2
    elif game_result == 2:
        your_play = opponent_play + 1
        if your_play > 2: your_play = 0
    else:
        your_play = opponent_play

    return your_play

if __name__ == "__main__":
    res_step_1 = step_1()
    print(res_step_1)

    res_step_2 = step_2()
    print(res_step_2)