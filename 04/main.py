import pathlib
from typing import List

directory = pathlib.Path(__file__).parent.resolve()


def get_data(
    data_path: str,
):
    with open(data_path, "r") as f:
        elf_ass_pairs = [line.split(",") for line in f.read().split("\n")]
    # elf_ass_pairs = [
    #     elf_assignments[group : group + 1]
    #     for group in range(0, len(elf_assignments), 2)
    # ]
    return elf_ass_pairs


def complete_overlap(
    elf_ass_one: str,
    elf_ass_two: str,
) -> int:

    # LOGIC:
    # 1   a - b
    # 2   c - d

    # 1 in 2
    # a > c and b < d

    # 2 in 1
    # a < c and b > d

    # print(elf_ass_one, elf_ass_two, sep="\t")

    a = int(elf_ass_one.split("-")[0])
    b = int(elf_ass_one.split("-")[1])
    c = int(elf_ass_two.split("-")[0])
    d = int(elf_ass_two.split("-")[1])

    if (a >= c) and (b <= d):
        return 1
    if (a <= c) and (b >= d):
        return 1
    return 0


def any_overlap(
    elf_ass_one: str,
    elf_ass_two: str,
) -> int:

    # LOGIC:
    # 1   a - b
    # 2   c - d

    # a <= c <= b
    # a <= d <= b

    # c <= a <= d
    # c <= b <= d

    # print(elf_ass_one, elf_ass_two, sep="\t")

    a = int(elf_ass_one.split("-")[0])
    b = int(elf_ass_one.split("-")[1])
    c = int(elf_ass_two.split("-")[0])
    d = int(elf_ass_two.split("-")[1])

    if (a <= c) and (c <= b):
        return 1
    if (a <= d) and (d <= b):
        return 1
    if (c <= a) and (a <= d):
        return 1
    if (c <= b) and (b <= d):
        return 1
    return 0


def answer_one(
    elf_ass_pairs: List,
):
    count_total_overlap = sum(
        complete_overlap(
            elf_ass_one=elf_ass_pair[0],
            elf_ass_two=elf_ass_pair[1],
        )
        for elf_ass_pair in elf_ass_pairs
    )

    print(f"Problem one answer: {count_total_overlap}")


def answer_two(
    elf_ass_pairs: List,
):
    count_total_overlap = sum(
        any_overlap(
            elf_ass_one=elf_ass_pair[0],
            elf_ass_two=elf_ass_pair[1],
        )
        for elf_ass_pair in elf_ass_pairs
    )

    print(f"Problem two answer: {count_total_overlap}")


elf_ass_pairs = get_data(f"{directory}/data.txt")

answer_one(elf_ass_pairs=elf_ass_pairs)
answer_two(elf_ass_pairs=elf_ass_pairs)
