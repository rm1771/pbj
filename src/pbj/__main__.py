"""Command-line entry point: ``python -m pbj`` (or the ``make-pbj`` script).

Assumption: the CLI just makes one default sandwich. A "real" CLI might take
flags for bread type, PB style, jelly flavor, etc. -- left out here to keep
the demo package small; a natural extension exercise for students.
"""

from .sandwich import PBJ


def main() -> None:
    """Build and make a default PB&J sandwich."""
    sandwich = PBJ()
    sandwich.make()


if __name__ == "__main__":
    main()
