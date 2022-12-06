import pathlib
from typing import List

directory = pathlib.Path(__file__).parent.resolve()


def get_data(
    data_path: str,
):
    with open(data_path, "r") as f:
        ds_buffers = f.read().split("\n")
    return ds_buffers


def find_marker(
    ds_buffer: str,
    distinct_characters: int,
) -> int:
    for i in range(len(ds_buffer)):
        char_block = ds_buffer[i : i + distinct_characters]
        if len(set(char_block)) == distinct_characters:
            return i + distinct_characters


def answer(
    ds_buffers: List,
    distinct_characters: int,
    problem: str,
) -> int:
    answer = sum(
        find_marker(
            ds_buffer=ds_buffer,
            distinct_characters=distinct_characters,
        )
        for ds_buffer in ds_buffers
    )

    print(f"Problem {problem} answer: {answer}")


ds_buffers = get_data(f"{directory}/data.txt")

answer(ds_buffers=ds_buffers, distinct_characters=4, problem="one")
answer(ds_buffers=ds_buffers, distinct_characters=14, problem="two")
