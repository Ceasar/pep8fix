from functools import wraps
import re

from pep8 import BINARY_OPERATORS


CODES = {}


def fixes(code):
    def wrapper(func):
        @wraps(func)
        def fix(swp, line):
            print repr(line)
            fix = func(line)
            print repr(fix)
            swp.write(fix)
        CODES[code] = fix
        fix.func = func
    return wrapper


@fixes('E225')
def e225(line):
    """fixes missing whitespace around operator."""
    for operator in BINARY_OPERATORS:
        pattern = "(\S)(%s)(\S)" % operator
        match = re.search(pattern, line)
        if match is None:
            pattern = "(\S)(%s)" % operator
            match = re.search(pattern, line)
            if match is None:
                match = re.search("(%s)(\S)" % (operator), line)
                if match is None:
                    continue
                else:
                    return line.replace(match.group(), "%s %s" % match.groups())
            else:
                return line.replace(match.group(), "%s %s" % match.groups())
        else:
            return line.replace(match.group(), "%s %s %s" % match.groups())


@fixes('E231')
def e231(line):
    """fixes missing white space after ','"""
    tokens = re.split(",(\S)", line)
    return "".join(", ".join(tokens[i:i + 2]) for i in range(0, len(tokens), 2))


@fixes('E261')
def e261(line):
    """fixes at least two spaces before inline comment"""
    i = line.rfind("#")
    return line[:i] + " " + line[i:]


@fixes('E262')
def e262(line):
    """fixes inline comment should start with '# '"""
    i = line.rfind("#") + 1
    return line[:i] + " " + line[i:]


@fixes('E302')
def e302(line):
    """fixes expected 2 lines, found 1."""
    return "\n" + line


# @fixes('E303')
def e303(line):
    """fixes too many blank lines (2)"""
    return ""


# @fixes('E701')
def e701(line):
    """fixes multiple statements on one line (colon)"""
    i = line.index(":")
    return line[:i] + "\n" + line[i:]


@fixes('W191')
def w191(line):
    """fixes W191 indentation contains tabs."""
    return line.expandtabs()


@fixes('W291')
def w291(line):
    """fixes trailing whitespace."""
    return line.rstrip() + "\n"


@fixes('W293')
def w293(line):
    """fixes blank line contains whitespace."""
    return "\n"


if __name__ == "__main__":
    import doctest
    doctest.testmod()
