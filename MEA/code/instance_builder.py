import os
import random

N = 200
capacity = N // 2  # 25

# base profits p_i = i (index 0 unused)
base_profits = list(range(0, N + 1))

# reproducible randomness (change seed if you want different pairs)
random.seed(42)

first_half = list(range(1, 101))   # 1..25
second_half = list(range(101, N + 1))  # 26..50

random.shuffle(first_half)
random.shuffle(second_half)

# we only need 9 pairs
swap_pairs = list(zip(first_half[:9], second_half[:9]))

def build_instance_text(k, profits):
    """Return knapsack instance k as a single string."""
    name = f"simple200-TTP-mut{k}"
    lines = []
    lines.append(f"PROBLEM NAME:  {name}")
    lines.append("KNAPSACK DATA TYPE: bounded strongly corr")
    lines.append("DIMENSION:  0")
    lines.append(f"NUMBER OF ITEMS:   {N}")
    lines.append(f"CAPACITY OF KNAPSACK:   {capacity}")
    lines.append("MIN SPEED:\t0.1")
    lines.append("MAX SPEED:\t1")
    lines.append("RENTING RATIO:\t5.61")
    lines.append("EDGE_WEIGHT_TYPE:\tCEIL_2D")
    lines.append("NODE_COORD_SECTION\t(INDEX, X, Y):")
    lines.append("1\t288\t149")
    lines.append("2\t288\t129")
    lines.append("3\t270\t133")
    lines.append("4\t256\t141")
    lines.append("5\t256\t157")
    lines.append("6\t246\t157")
    lines.append("7\t236\t169")
    lines.append("8\t228\t169")
    lines.append("9\t228\t161")
    lines.append("10\t220\t169")
    lines.append("ITEMS SECTION (INDEX, PROFIT, WEIGHT, ASSIGNED NODE NUMBER):")
    for i in range(1, N + 1):
        node = (i - 1) % 10 + 1  # 1..10 repeating
        lines.append(f"{i}\t{profits[i]}\t1\t{node}")
    lines.append("")  # blank line at end
    return "\n".join(lines)

def write_instances_to_folder(folder_name="n200w1k10"):
    """Create output folder under ../instances and write each instance file there."""
    here = os.path.dirname(__file__)
    instances_root = os.path.abspath(os.path.join(here, "..", "instances"))
    out_dir = os.path.join(instances_root, folder_name)
    os.makedirs(out_dir, exist_ok=True)

    # work from base profits
    profits = base_profits[:]

    # write base (no swaps) instance
    base_text = build_instance_text(0, profits)
    base_filename = f"n{N}w1k1.txt"
    base_path = os.path.join(out_dir, base_filename)
    with open(base_path, "w") as fh:
        fh.write(base_text)
    print(f"Wrote base instance {base_path}")

    for k in range(1, 10):  # mutations 1..9
        a, b = swap_pairs[k - 1]

        # apply this mutation (cumulative from previous)
        profits[a], profits[b] = profits[b], profits[a]

        # build text and write to file
        text = build_instance_text(k, profits)
        filename = f"n{N}w1k{k+1}.txt"
        out_path = os.path.join(out_dir, filename)
        with open(out_path, "w") as fh:
            fh.write(text)

        # optional small log
        print(f"Wrote {out_path} (swapped {a} <-> {b})")

if __name__ == "__main__":
    write_instances_to_folder()
