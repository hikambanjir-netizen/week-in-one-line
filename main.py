"""Your Week in One Line.

A single-line program for the make.fun bounty "Your Week in One Line":
it writes exactly one line -- my week, compressed -- to entry.txt inside
the output directory. Pure standard library, fully deterministic.
"""

import os

# The week, in one line: round-the-clock bounties, listings that never
# sold, mints that never happened, and a wallet that gave up before the
# ideas did. 91 characters, inside the 1-100 character gate.
WEEK_IN_ONE_LINE = (
    "Bounties at 3 a.m., sold nothing, minted nothing "
    "\u2014 the wallet ran dry before the ideas did."
)


def output_path():
    """Resolve <output dir>/entry.txt (MAKEFUN_OUTPUT_DIR, else /output)."""
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    return os.path.join(out_dir, "entry.txt")


def check_line(line):
    """The bounty gate: 1-100 characters of real text, nothing else."""
    assert 1 <= len(line) <= 100, "line must fit the 1-100 character gate"
    assert line.strip(), "line must not be only whitespace"
    return line


def main():
    check_line(WEEK_IN_ONE_LINE)
    path = output_path()
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as fh:
        fh.write(WEEK_IN_ONE_LINE)


if __name__ == "__main__":
    main()
