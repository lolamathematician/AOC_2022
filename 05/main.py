import pathlib
from typing import List

directory = pathlib.Path(__file__).parent.resolve()


def get_data(
    data_path: str,
):
    with open(data_path, "r") as f:
        stack_input, moves_input = f.read().split("\n\n")
        moves_input = [
            [int(i) for i in move.split(" ")[1::2]] for move in moves_input.split("\n")
        ]
        stack_input = stack_input.split("\n")
        # extract the stack numbers from the input data
        stack_numbers = [
            int(stack_number.replace(" ", ""))
            # pop the final element so the stack numbers are not included in the item stacks
            for stack_number in stack_input.pop().split("   ")
        ]
        # put the items from the stacks into lists
        # top of the stack is first element in the list
        item_stacks = []
        for stack_number in stack_numbers:
            # with an offset of 1 every fourth stack number along the row string is in that stack
            item_stacks.append(
                [
                    line[1 + (stack_number - 1) * 4]
                    for line in stack_input
                    if line[1 + (stack_number - 1) * 4] != " "
                ]
            )

    return moves_input, item_stacks


def perform_move(
    item_stacks: List,
    number_of_items: int,
    from_stack: int,
    to_stack: int,
):
    for number in range(number_of_items):
        item = item_stacks[from_stack - 1][0]
        item_stacks[to_stack - 1].insert(0, item)
        item_stacks[from_stack - 1].pop(0)

    return item_stacks


def perform_move_9001(
    item_stacks: List,
    number_of_items: int,
    from_stack: int,
    to_stack: int,
):
    for number in range(number_of_items - 1, -1, -1):
        item = item_stacks[from_stack - 1][number]
        item_stacks[to_stack - 1].insert(0, item)
        item_stacks[from_stack - 1].pop(number)

    return item_stacks


def answer_one(
    moves: List,
    item_stacks: List,
):
    for move in moves:
        item_stacks = perform_move(
            item_stacks=item_stacks,
            number_of_items=move[0],
            from_stack=move[1],
            to_stack=move[2],
        )

    top_items = [item_stack[0] for item_stack in item_stacks if len(item_stack) > 0]
    print(top_items)
    s = "".join(top_items)
    print(s)


def answer_two(
    moves: List,
    item_stacks: List,
):
    for move in moves:
        print(item_stacks)
        print(move)
        item_stacks = perform_move_9001(
            item_stacks=item_stacks,
            number_of_items=move[0],
            from_stack=move[1],
            to_stack=move[2],
        )

    top_items = [item_stack[0] for item_stack in item_stacks if len(item_stack) > 0]
    s = "".join(top_items)
    print(s)


moves, item_stacks = get_data(f"{directory}/data.txt")

# answer_one(moves=moves, item_stacks=item_stacks)
answer_two(moves=moves, item_stacks=item_stacks)
