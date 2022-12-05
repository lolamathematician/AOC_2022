import pathlib
from typing import List

directory = pathlib.Path(__file__).parent.resolve()

# key beats value
losing_hand = {
    "R": "S",
    "S": "P",
    "P": "R",
}

# key loses to value
winning_hand = {
    "R": "P",
    "P": "S",
    "S": "R",
}

opponent_dict = {
    "A": "R",
    "B": "P",
    "C": "S",
}

player_dict = {
    "X": "R",
    "Y": "P",
    "Z": "S",
}

hand_score = {
    "R": 1,
    "P": 2,
    "S": 3,
}

result_score = {
    "W": 6,
    "D": 3,
    "L": 0,
}

# R > S, S > P, P > R
lhs_win = [
    ("R", "S"),
    ("S", "P"),
    ("P", "R"),
]


def get_data(
    data_path: str,
) -> List[List[str, str]]:
    with open(data_path, "r") as f:
        hands = [game.split(" ") for game in f.read().split("\n")]
    return hands


def get_player_score_one(
    player_hand: str,
    opponent_hand: str,
):
    # convert hand codes to R, P, S
    player_hand = player_dict[player_hand]
    opponent_hand = opponent_dict[opponent_hand]

    # draw
    if opponent_hand == player_hand:
        player_result = "D"
    # player wins
    if (player_hand, opponent_hand) in lhs_win:
        player_result = "W"
    # player loses
    if (opponent_hand, player_hand) in lhs_win:
        player_result = "L"

    player_score = hand_score[player_hand] + result_score[player_result]

    return player_score


def part_one():
    hands = get_data(f"{directory}/data.txt")

    player_scores = [
        get_player_score_one(
            player_hand=hand[1],
            opponent_hand=hand[0],
        )
        for hand in hands
    ]

    answer_one = sum(player_scores)

    print(f"Part one answer: {answer_one}")


def get_player_score_two(
    player_clue: str,
    opponent_hand: str,
):
    opponent_hand = opponent_dict[opponent_hand]
    # if X lose
    if player_clue == "X":
        player_hand = losing_hand[opponent_hand]
        player_result = "L"

    # if Y draw
    if player_clue == "Y":
        player_hand = opponent_hand
        player_result = "D"

    # if Z win
    if player_clue == "Z":
        player_hand = winning_hand[opponent_hand]
        player_result = "W"

    player_score = hand_score[player_hand] + result_score[player_result]

    return player_score


def part_two():
    hands = get_data(f"{directory}/data.txt")

    player_scores = [
        get_player_score_two(
            player_clue=hand[1],
            opponent_hand=hand[0],
        )
        for hand in hands
    ]

    answer_one = sum(player_scores)

    print(f"Part two answer: {answer_one}")


part_one()
part_two()
