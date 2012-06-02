from functools import wraps
import re

import pep8


def e225(line, cursor):
    """fixes missing whitespace around operator."""
    # iterate through operators in reverse length order
    for operator in sorted(pep8.OPERATORS, reverse=True):
        escaped = re.escape(operator)
        pattern = "(\S)(%s)(\S)" % (escaped)
        match = re.search(pattern, line)
        if match is None:
            pattern_l = "(\S)(%s)" % escaped
            pattern_r = "(%s)(\S)" % escaped
            match_l = re.search(pattern_l, line)
            match_r = re.search(pattern_r, line)
            match = match_l or match_r
            if match is not None:
                return line.replace(match.group(), "%s %s" % match.groups())
            else:
                continue
        else:
            return line.replace(match.group(), "%s %s %s" % match.groups())
    raise ValueError("No operator found! '%s'" % line)


def e231(line, cursor):
    """fixes missing white space after ','"""
    tokens = re.split(",(\S)", line)
    return "".join(", ".join(tokens[i:i + 2]) for i in range(0, len(tokens), 2))


def e261(line, cursor):
    """fixes at least two spaces before inline comment"""
    i = line.rfind("#")
    return line[:i] + " " + line[i:]


def e262(line, cursor):
    """fixes inline comment should start with '# '"""
    i = line.rfind("#") + 1
    return line[:i] + " " + line[i:]


def e302(line, cursor):
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


def w191(line, cursor):
    """fixes W191 indentation contains tabs."""
    return line.expandtabs()


def w291(line, cursor):
    """fixes trailing whitespace."""
    return line.rstrip() + "\n"


def w293(line, cursor):
    """fixes blank line contains whitespace."""
    return "\n"


if __name__ == "__main__":
    import doctest
    doctest.testmod()
