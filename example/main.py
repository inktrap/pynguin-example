#!/usr/bin/env python3.9

# not necessary if this would be a proper package:
if __name__ != "__main__":
    import os
    import sys

    script_dir = os.path.dirname(os.path.realpath(__file__))
    sys.path.insert(0, os.path.join(script_dir))

from lib import ops


def main() -> None:
    """Main method.
    :returns: None

    """
    print(ops.plus(1, 2))
    print(ops.minus(1, 2))


if __name__ == "__main__":
    main()
