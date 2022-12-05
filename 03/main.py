import pathlib
import string
from typing import List

directory = pathlib.Path(__file__).parent.resolve()


def build_item_priorities() -> dict:
    item_priorities = {
        letter: string.ascii_letters.find(letter) + 1 for letter in string.ascii_letters
    }
    return item_priorities


def get_data(
    data_path: str,
    rucksack_type: str,
):
    with open(data_path, "r") as f:
        if rucksack_type == "compartments":
            rucksacks = [
                [rucksack[: len(rucksack) // 2], rucksack[len(rucksack) // 2 :]]
                for rucksack in f.read().split("\n")
            ]
            return rucksacks
        if rucksack_type == "groups":
            rucksacks = f.read().split("\n")
            rucksack_groups = [
                rucksacks[group : group + 3]
                for group in range(
                    0,
                    len(rucksacks),
                    3,
                )
            ]
            return rucksack_groups
    raise ValueError("""Answer should be "compartments" or "groups".""")


def find_repeat_value(
    compartment_one: str,
    compartment_two: str,
    item_priorities: dict,
) -> str:
    repeat = set(item for item in compartment_one if item in compartment_two)
    if len(repeat) > 1:
        raise ValueError(
            "Found more than one repeated item. There should only be one repeated item."
        )
    repeat = repeat.pop()
    repeat_value = item_priorities[repeat]
    return repeat_value


def find_repeat_badge_value(
    rucksack_one: str,
    rucksack_two: str,
    rucksack_three: str,
    item_priorities: dict,
):
    repeat = set(
        item
        for item in rucksack_one
        if (item in rucksack_two) and (item in rucksack_three)
    )
    if len(repeat) > 1:
        raise ValueError(
            "Found more than one repeated item. There should only be one repeated item."
        )

    repeat = repeat.pop()
    repeat_value = item_priorities[repeat]
    return repeat_value


def answer_one(
    rucksacks: List,
    item_priorities: dict,
):
    answer_one = sum(
        find_repeat_value(
            compartment_one=rucksack[0],
            compartment_two=rucksack[1],
            item_priorities=item_priorities,
        )
        for rucksack in rucksacks
    )

    print(f"Part one answer: {answer_one}")


# badge is item carried by all three elves
def answer_two(
    groups: List,
    item_priorities: dict,
):
    answer_two = sum(
        find_repeat_badge_value(
            rucksack_one=group[0],
            rucksack_two=group[1],
            rucksack_three=group[2],
            item_priorities=item_priorities,
        )
        for group in groups
    )

    print(f"Part two answer: {answer_two}")


item_priorities = build_item_priorities()

rucksacks = get_data(
    data_path=f"{directory}/data.txt",
    rucksack_type="compartments",
)

rucksack_groups = get_data(
    data_path=f"{directory}/data.txt",
    rucksack_type="groups",
)

answer_one(
    rucksacks=rucksacks,
    item_priorities=item_priorities,
)

answer_two(
    groups=rucksack_groups,
    item_priorities=item_priorities,
)
