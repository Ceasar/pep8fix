from functools import wraps
import re
import tokenize

import pep8

def _iden(x):
    yield x


def e225(line, cursor):
    """fixes missing whitespace around operator."""
    # iterate through operators in reverse length order
    tokens = tokenize.generate_tokens(_iden(line).next)
    return ' '.join(token for _, token, _, _, _ in tokens)


def e231(line, cursor):
    """fixes missing white space after ','"""
    tokens = re.split(",(\S)", line)
    return "".join(", ".join(tokens[i:i + 2]) for i in range(0, len(tokens), 2))


def e261(line, cursor):
    """fixes at least two spaces before inline comment"""
    return line[:cursor].rstrip() + "  " + line[cursor:]


def e262(line, cursor):
    """fixes inline comment should start with '# '"""
    i = cursor + 1
    return line[:i] + " " + line[i:].lstrip()


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
