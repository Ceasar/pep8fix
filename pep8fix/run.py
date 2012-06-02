"""Module to automatically fix a subset of pep8 errors."""
from collections import defaultdict
import sys

import fixes
from swap import swap


class Error(object):
    """A pep8 error."""

    def __init__(self, filename, line, cursor, code, msg):
        self.filename = filename
        self.line = line
        self.cursor = cursor
        self.code = code
        self.msg = msg

    def __str__(self):
        return "%s:%s:%s: %s %s" % (self.filename, self.line, self.cursor, self.code, self.msg)


def parse_location(location):
    """Parse an error location.
    >>> parse_location("examples/turtleprocess.py:28:22:")
    'examples/turtleprocess.py', 28, 22
    """
    tokens = location.split(":")
    filename, line, cursor = tokens[0], int(tokens[1]), None

    # not all errors contain a cursor
    try:
        cursor = int(tokens[2])
    except ValueError:
        pass
    return filename, line, cursor


def parse_error(line):
    """Parse an error message.
    >>> parse_error('test.py:5:8: E225 missing whitespace around operator')
    """
    tokens = line.split()
    location, code = tokens[0], tokens[1]
    msg = " ".join(tokens[2:])
    filename, line, cursor = parse_location(location)
    return Error(filename, line, cursor, code, msg)


def fix_file(filename, errors):
    """Fix all the errors in a file."""
    line_errors = dict((error.line, error) for error in errors)
    with swap(filename) as swp:
        with open(filename, 'r') as f:
            for i, line in enumerate(f):
                # Is there an error on this line?
                try:
                    error = line_errors[i + 1]
                except KeyError:
                    continue
                else:
                    print error
                    # Can we fix it?
                    code = error.code.lower()
                    try:
                        fix = getattr(fixes, code)
                    except AttributeError:
                        print "No known solution."
                        swp.write(line)
                    else:
                        print repr(line)
                        fixed = fix(line)
                        print repr(fixed)
                        swp.write(fixed)


def main():
    # Group errors by file
    file_errors = defaultdict(list)
    for line in sys.stdin:
        error = parse_error(line)
        file_errors[error.filename].append(error)

    # Fix files
    for filename, errors in file_errors.iteritems():
        fix_file(filename, errors)

    return 0

if __name__ == "__main__":
    sys.exit(main())
