#!/usr/bin/env python3
"""
PassGen – Simple Secure Password Generator
"""

import argparse
import math
import string
import sys
from secrets import choice, randbelow


DEFAULT_SYMBOLS = "!@#$%^&*()-_=+[]{};:,.?/"
AMBIGUOUS = set("O0oIl1|`'\"{}[]()<>;:,./\\")


def build_charsets(lower=True, upper=True, digits=True, symbols=True, avoid_ambiguous=False):
    charsets = []

    def _filter(chars):
        return "".join(c for c in chars if c not in AMBIGUOUS) if avoid_ambiguous else chars

    if lower:
        charsets.append(_filter(string.ascii_lowercase))
    if upper:
        charsets.append(_filter(string.ascii_uppercase))
    if digits:
        charsets.append(_filter(string.digits))
    if symbols:
        charsets.append(_filter(DEFAULT_SYMBOLS))

    return [s for s in charsets if s]


def generate_password(length, charsets):
    if length < len(charsets):
        raise ValueError("Length too short for the selected character classes.")

    pwd = [choice(cs) for cs in charsets]  # guarantee at least one from each class
    pool = "".join(charsets)
    pwd.extend(choice(pool) for _ in range(length - len(pwd)))

    # Fisher–Yates shuffle
    for i in range(len(pwd) - 1, 0, -1):
        j = randbelow(i + 1)
        pwd[i], pwd[j] = pwd[j], pwd[i]

    return "".join(pwd)


def entropy(length, pool_size):
    return length * math.log2(pool_size) if pool_size > 1 else 0


def main():
    parser = argparse.ArgumentParser(description="Generate secure random passwords.")
    parser.add_argument("-l", "--length", type=int, default=16, help="Password length (default: 16)")
    parser.add_argument("-n", "--count", type=int, default=1, help="Number of passwords (default: 1)")
    parser.add_argument("--no-lower", action="store_true", help="Exclude lowercase")
    parser.add_argument("--no-upper", action="store_true", help="Exclude uppercase")
    parser.add_argument("--no-digits", action="store_true", help="Exclude digits")
    parser.add_argument("--no-symbols", action="store_true", help="Exclude symbols")
    parser.add_argument("-a", "--avoid-ambiguous", action="store_true", help="Avoid look-alike characters (O/0, l/1, |)")
    parser.add_argument("-o", "--out", help="Write passwords to a file")
    parser.add_argument("--append", action="store_true", help="Append instead of overwrite")

    args = parser.parse_args()

    charsets = build_charsets(
        not args.no_lower,
        not args.no_upper,
        not args.no_digits,
        not args.no_symbols,
        args.avoid_ambiguous,
    )

    if not charsets:
        sys.exit("Error: No character classes selected.")

    passwords = [generate_password(args.length, charsets) for _ in range(args.count)]
    ent = entropy(args.length, len(set("".join(charsets))))

    header = [
        f"# Generated {len(passwords)} password(s)",
        f"# Length: {args.length}, Entropy: {ent:.1f} bits",
    ]
    output = "\n".join(header + passwords)

    if args.out:
        mode = "a" if args.append else "w"
        with open(args.out, mode, encoding="utf-8") as f:
            f.write(output + "\n")
        print(f"Saved {len(passwords)} password(s) to {args.out}")
    else:
        print(output)


if __name__ == "__main__":
    main()
