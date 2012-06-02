from functools import wraps
import re

import pep8


def e225(line):
    """fixes missing whitespace around operator."""
    # iterate through operators in reverse length order
    for operator in reversed(list(pep8.BINARY_OPERATORS)):
        escaped = re.escape(operator)
        pattern = "(\S)(%s)(\S)" % re.escape(escaped)
        match = re.search(pattern, line)
        if match is None:
            pattern = "(\S)(%s)" % escaped
            match = re.search(pattern, line)
            if match is None:
                match = re.search("(%s)(\S)" % (escaped), line)
                if match is None:
                    continue
                else:
                    return line.replace(match.group(), "%s %s" % match.groups())
            else:
                return line.replace(match.group(), "%s %s" % match.groups())
        else:
            return line.replace(match.group(), "%s %s %s" % match.groups())


def e231(line):
    """fixes missing white space after ','"""
    tokens = re.split(",(\S)", line)
    return "".join(", ".join(tokens[i:i + 2]) for i in range(0, len(tokens), 2))


def e261(line):
    """fixes at least two spaces before inline comment"""
    i = line.rfind("#")
    return line[:i] + " " + line[i:]


def e262(line):
    """fixes inline comment should start with '# '"""
    i = line.rfind("#") + 1
    return line[:i] + " " + line[i:]


def e302(line):
    """fixes expected 2 lines, found 1."""
    return "\n" + line


'''
def e303(line):
    """fixes too many blank lines (2)"""
    return ""
'''


'''
def e701(line):
    """fixes multiple statements on one line (colon)"""
    i = line.index(":")
    return line[:i] + "\n" + line[i:]
'''


def w191(line):
    """fixes W191 indentation contains tabs."""
    return line.expandtabs()


def w291(line):
    """fixes trailing whitespace."""
    return line.rstrip() + "\n"


def w293(line):
    """fixes blank line contains whitespace."""
    return "\n"


if __name__ == "__main__":
    import doctest
    doctest.testmod()
