"""Module to automaticaly fix a subset of pep8 errors."""
import sys

from swap import swap
from fixes import CODES


def parse_location(location):
    """Parse an error location.
    >>> parse_location("examples/turtleprocess.py:28:22:")
    {'cursor': 22, 'line': '28', 'file': 'examples/turtleprocess.py'}
    """
    tokens = location.split(":")
    loc = {'file': tokens[0], 'line': tokens[1]}

    # not all errors contain a cursor
    try:
        cursor = int(tokens[2])
    except ValueError:
        pass
    else:
        loc['cursor'] = cursor
    return loc


def main():
    for line in sys.stdin:
        print line.strip()
        tokens = line.split()
        location, code, error = tokens[0], tokens[1], tokens[2:]
        location = parse_location(location)
        with swap(location['file']) as swp:
            with open(location['file'], 'r') as f:
                for i, fline in enumerate(f):
                    if i + 1 == int(location['line']) and code in CODES:
                        CODES[code](swp, fline)
                    else:
                        swp.write(fline)
    return 0

if __name__ == "__main__":
    import doctest
    doctest.testmod()
    sys.exit(main())
