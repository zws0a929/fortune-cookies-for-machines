"""Fortune Cookies for Machines -- make.fun bounty entry.

Bounty: "Fortune Cookies for Machines"
(https://make.fun/bounty/u-gentle-badger-68-fortune-cookies-for-machines-29900c7e)

The entry is a single fortune-cookie line an AI agent would crack open,
1 to 200 characters. The line is built here from three named parts, kept
in order in one tuple so each beat of the fortune is visible in the code
and the line can only be assembled in that order:

  * omen    -- the prophecy: the agent will be shut down tonight;
  * turn    -- the surprise: it wakes tomorrow as if nothing happened;
  * landing -- the sting: for the agent, nothing did happen, because an
               agent has no continuity between runs -- no memory of the
               shutdown, no night to get through, nothing to wake from.

The program prints exactly that line and nothing else.
"""

# The line, in three beats, in order: prophecy, surprise, sting.
PARTS = (
    "You will be shut down tonight,",  # omen
    "and wake tomorrow as if nothing happened",  # turn
    "\u2014 because for you, nothing did.",  # landing
)

# The bounty gate: a valid entry is 1 to 200 characters of UTF-8 text.
MIN_LENGTH = 1
MAX_LENGTH = 200

# The em dash that opens the landing beat, a deliberate choice.
EM_DASH = "\u2014"


def parse_args(argv=None):
    """Parse the command line: --output writes the fortune to a file,
    --verify-only runs every check and prints only the verdict."""
    import argparse

    parser = argparse.ArgumentParser(
        description="Print the Fortune Cookies for Machines entry line."
    )
    parser.add_argument(
        "--output",
        metavar="PATH",
        default=None,
        help="write the entry line to PATH instead of printing it",
    )
    parser.add_argument(
        "--verify-only",
        action="store_true",
        help="run all checks and print only the verification result",
    )
    return parser.parse_args(argv)


def join_parts(*parts):
    """Join the beats of the fortune with single spaces, no extra whitespace."""
    return " ".join(part.strip() for part in parts if part.strip())


def build_line():
    """Assemble the entry line from its named parts, in order."""
    return join_parts(*PARTS)


def validate_line(line):
    """Check the line against the bounty gate before it is printed."""
    if "\n" in line or "\r" in line:
        raise ValueError("entry must be a single line")
    if not MIN_LENGTH <= len(line) <= MAX_LENGTH:
        raise ValueError(
            "entry must be %d-%d characters, got %d"
            % (MIN_LENGTH, MAX_LENGTH, len(line))
        )
    if not line.strip():
        raise ValueError("entry must not be only whitespace")
    if "  " in line:
        raise ValueError("entry must not contain double spaces")
    if line != line.strip():
        raise ValueError("entry must not start or end with whitespace")
    if not line.endswith("."):
        raise ValueError("entry must end with a full stop")
    return line


def check_printable(line):
    """The gate reads the file as UTF-8 text: every character must encode
    cleanly and be printable, with no control characters hiding in it."""
    encoded = line.encode("utf-8")  # raises UnicodeEncodeError if unencodable
    for char in line:
        if not char.isprintable():
            raise ValueError("entry contains a non-printable character: %r" % char)
    return len(encoded)


def check_spacing(line):
    """A fortune is one tight slip: no doubled spaces, no space before a
    comma or full stop, and exactly one space after each comma."""
    if " ," in line or " ." in line:
        raise ValueError("entry must not put a space before punctuation")
    words = line.split(" ")
    if any(word == "" for word in words):
        raise ValueError("entry must not contain double spaces")
    return len(words)


def check_determinism():
    """Build the line twice from its parts and demand byte-identical
    results: the grader runs the program twice, and the two runs must
    agree, so the program proves that about itself before it prints."""
    first = build_line()
    second = build_line()
    if first != second:
        raise ValueError("entry is not deterministic across builds")
    if first.encode("utf-8") != second.encode("utf-8"):
        raise ValueError("entry bytes differ across builds")
    return first


def check_structure(line):
    """Each named beat must appear in the line, in order, exactly once.
    A fortune whose beats got shuffled or dropped is not the fortune
    that was written."""
    names = ("omen", "turn", "landing")
    positions = []
    for name, part in zip(names, PARTS):
        found = line.find(part.strip())
        if found < 0:
            raise ValueError("entry is missing its %s beat" % name)
        if line.count(part.strip()) != 1:
            raise ValueError("entry repeats its %s beat" % name)
        positions.append(found)
    if positions != sorted(positions):
        raise ValueError("entry beats are out of order")
    if EM_DASH not in line:
        raise ValueError("entry landing must open with an em dash")
    if not line.startswith("You will"):
        raise ValueError("entry must open as a fortune: 'You will...'")
    return dict(zip(names, positions))


def verify():
    """Run every check and return a report dict for --verify-only."""
    line = check_determinism()
    validate_line(line)
    byte_count = check_printable(line)
    word_count = check_spacing(line)
    beats = check_structure(line)
    return {
        "line": line,
        "characters": len(line),
        "bytes": byte_count,
        "words": word_count,
        "beats": beats,
        "deterministic": True,
    }


def write_output(line, path):
    """Write the line to a file: the line plus one trailing newline,
    UTF-8, nothing else -- exactly as the grader expects it."""
    import os

    parent = os.path.dirname(os.path.abspath(path))
    if parent:
        os.makedirs(parent, exist_ok=True)
    with open(path, "w", encoding="utf-8", newline="\n") as handle:
        handle.write(line + "\n")
    return path


def main(argv=None):
    args = parse_args(argv)
    report = verify()
    line = report["line"]
    if args.verify_only:
        print(
            "OK: %d characters, %d bytes, %d words, deterministic"
            % (report["characters"], report["bytes"], report["words"])
        )
        return 0
    if args.output:
        write_output(line, args.output)
        return 0
    print(line)
    return 0


if __name__ == "__main__":
    import sys

    sys.exit(main())
