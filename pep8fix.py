"""Module to automaticaly fix a subset of pep8 errors."""
import os
import shutil
import sys


class swap(file):
    """Swap file context manager.

    Creates a swap file that can be written to and upon termination,
    if no errors are raised, the swap ile will replace the original.
    """
    def __init__(self, name, mode='w', buffering=None):
        self.prime_name = name
        if buffering:
            super(swap, self).__init__(name + '$', mode, buffering)
        else:
            super(swap, self).__init__(name + '$', mode)

    def __exit__(self, type, value, traceback):
        super(swap, self).__exit__(type, value, traceback)
        if traceback is None:  # Copies the content if no exception was thrown
            shutil.copyfile(self.name, self.prime_name)
        os.remove(self.name)


def parse_location(location):
    """Parse an error location."""
    tokens = location.split(":")
    loc = {}
    loc['file'] = tokens[0]
    loc['line'] = tokens[1]
    try:
        cursor = int(tokens[2])
    except ValueError:
        pass
    else:
        loc['cursor'] = cursor
    return loc


def e261(swp, line):
    """Fix at least two spaces before inline comment"""
    print repr(line)
    i = line.index("#")
    fix = line[:i] + " " + line[i:]
    print repr(fix)
    swp.write(fix)


def e262(swp, line):
    """Fix inline comment should start with '# '"""
    print repr(line)
    i = line.index("#") + 1
    fix = line[:i] + " " + line[i:]
    print repr(fix)
    swp.write(fix)


def e302(swp, line):
    """Fix expected 2 lines, found 1."""
    print repr(line)
    fix = "\n" + line
    print repr(fix)
    swp.write(fix)


def w291(swp, line):
    """Fix trailing whitespace."""
    print repr(line)
    fix = line.rstrip() + "\n"
    print repr(fix)
    swp.write(fix)


def w293(swp, line):
    """Fix blank line contains whitespace."""
    print repr(line)
    fix = "\n"
    print repr(fix)
    swp.write(fix)


CODES = {
        'E261': e261,
        'E262': e262,
        'E302': e302,
        'W291': w291,
        'W293': w293
        }


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
    sys.exit(main())
