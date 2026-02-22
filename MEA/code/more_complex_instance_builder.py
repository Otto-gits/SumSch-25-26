#!/usr/bin/env python3
"""
Generate a chain of TTP instances where each new file is ONE additional profit-swap away
from the previous file.

Example:
  python make_swap_chain.py /mnt/data/a280-TTP-1.txt --max-swaps 50 --outdir ./chain --seed 42

Output filenames:
  a280-TTP-1.txt, a280-TTP-2.txt, ..., a280-TTP-50.txt
where:
  - file k has k-1 swaps applied relative to the starting file content
  - file (k+1) differs from file k by exactly one extra profit-swap
"""

from __future__ import annotations

import argparse
import random
import re
from dataclasses import dataclass
from pathlib import Path
from typing import List, Tuple


ITEMS_HEADER_RE = re.compile(r"^\s*ITEMS SECTION\s*\(.*\)\s*:\s*$", re.IGNORECASE)
PROBLEM_NAME_RE = re.compile(r"^\s*PROBLEM NAME:\s*(.+?)\s*$", re.IGNORECASE)
ITEM_LINE_RE = re.compile(r"^\s*(\d+)\s+(\-?\d+)\s+(\-?\d+)\s+(\-?\d+)\s*$")


@dataclass
class ItemRow:
    line_index_in_file: int
    idx: int
    profit: int
    weight: int
    node: int


def find_problem_name(lines: List[str]) -> str:
    for line in lines:
        m = PROBLEM_NAME_RE.match(line.rstrip("\n"))
        if m:
            # Preserve the canonical name portion after "PROBLEM NAME:"
            return m.group(1).strip()
    # Fallback if missing
    return "TTP"


def parse_items(lines: List[str]) -> List[ItemRow]:
    header_idx = None
    for i, line in enumerate(lines):
        if ITEMS_HEADER_RE.match(line.rstrip("\n")):
            header_idx = i
            break
    if header_idx is None:
        raise ValueError("Could not find 'ITEMS SECTION (...) :' header line.")

    items: List[ItemRow] = []
    for j in range(header_idx + 1, len(lines)):
        s = lines[j].rstrip("\n")
        if s.strip() == "":
            break

        m = ITEM_LINE_RE.match(s)
        if not m:
            break

        idx, profit, weight, node = map(int, m.groups())
        items.append(ItemRow(j, idx, profit, weight, node))

    if len(items) < 2:
        raise ValueError("Need at least 2 items in ITEMS SECTION.")
    return items


def format_item_line(idx: int, profit: int, weight: int, node: int) -> str:
    # Tab-separated is common in TTP files; this keeps it neat and consistent.
    return f"{idx}\t{profit}\t{weight}\t{node}\n"


def write_instance(
    base_lines: List[str],
    items: List[ItemRow],
    profits: List[int],
    out_path: Path,
) -> None:
    out_lines = base_lines[:]  # copy
    for i, it in enumerate(items):
        out_lines[it.line_index_in_file] = format_item_line(it.idx, profits[i], it.weight, it.node)
    out_path.write_text("".join(out_lines), encoding="utf-8")


def main() -> None:
    ap = argparse.ArgumentParser(description="Create chained TTP instances with cumulative profit swaps.")
    ap.add_argument("input", type=str, help="Path to starting TTP file (e.g. a280-TTP-1.txt)")
    ap.add_argument("--outdir", type=str, default="swap_chain", help="Directory to write chain files")
    ap.add_argument("--max-swaps", type=int, required=True,
                    help="Generate files 1..max-swaps (file k has k-1 cumulative swaps vs the input file)")
    ap.add_argument("--seed", type=int, default=None, help="Random seed for reproducibility")
    ap.add_argument("--avoid-repeat-pairs", action="store_true",
                    help="Try to avoid swapping the exact same item pair more than once.")
    args = ap.parse_args()

    in_path = Path(args.input).expanduser().resolve()
    outdir = Path(args.outdir).expanduser().resolve()
    outdir.mkdir(parents=True, exist_ok=True)

    base_text = in_path.read_text(encoding="utf-8", errors="replace")
    base_lines = base_text.splitlines(keepends=True)

    problem_name = find_problem_name(base_lines)
    items = parse_items(base_lines)

    rng = random.Random(args.seed)

    # This is the evolving state: profits[i] corresponds to items[i]
    profits = [it.profit for it in items]

    # Track swapped pairs if requested
    used_pairs = set()

    manifest = ["file\tstep_swap\n"]

    # We produce files named problem_name-1.txt ... problem_name-max_swaps.txt
    # File 1 corresponds to the starting state (0 swaps applied).
    for k in range(1, args.max_swaps + 1):
        out_path = outdir / f"{problem_name}-{k}.txt"

        if k == 1:
            # Write the starting file as "-1" (0 swaps applied).
            write_instance(base_lines, items, profits, out_path)
            manifest.append(f"{out_path.name}\t-\n")
            continue

        # Apply exactly ONE new swap to move from state (k-1) -> (k)
        tries = 0
        while True:
            a, b = rng.sample(range(len(items)), 2)
            pair = tuple(sorted((items[a].idx, items[b].idx)))
            tries += 1

            if args.avoid_repeat_pairs and pair in used_pairs:
                if tries > 10_000:
                    raise RuntimeError("Could not find a new pair to swap after many tries.")
                continue

            # Do the swap of PROFITS ONLY
            profits[a], profits[b] = profits[b], profits[a]
            used_pairs.add(pair)
            manifest.append(f"{out_path.name}\t{pair[0]}<->{pair[1]}\n")
            break

        write_instance(base_lines, items, profits, out_path)

    (outdir / "manifest.tsv").write_text("".join(manifest), encoding="utf-8")
    print(f"Done. Wrote {args.max_swaps} chained instances to: {outdir}")
    print(f"Manifest: {outdir / 'manifest.tsv'}")


if __name__ == "__main__":
    main()