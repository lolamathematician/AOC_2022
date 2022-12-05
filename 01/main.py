import pathlib

directory = pathlib.Path(__file__).parent.resolve()

with open(f"{directory}/data.txt", "r") as f:
    elf_invs = [[int(i) for i in inv.split("\n")] for inv in f.read().split("\n\n")]

elf_calories = [sum(elf_inv) for elf_inv in elf_invs]
max_elf_calories = max(elf_calories)

print(f"Part one answer: {max_elf_calories}")

elf_calories.sort(reverse=True)

top_three_elf_calories = sum(elf_calories[:3])

print(f"Part two answer: {top_three_elf_calories}")
