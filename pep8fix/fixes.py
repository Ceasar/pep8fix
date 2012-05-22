import re


CODES = {}


class Fix(object):
    def __init__(self, issue):
        self.issue = issue

    def __call__(self, func):
        def fix(swp, line):
            print repr(line)
            fix = func(line)
            print repr(fix)
            swp.write(fix)
        CODES[self.issue] = fix


# be careful with ordering since first match is returned
_OPERATORS = (
    '<<', '<=', '<',
    '>=', '>',
    '\+=', '-=', '==', '!=', '=',
    '\*\*', '\*',
    '//', '/',
    '\+', '-', '%', '&', '\^', '~', '\|')


@Fix('E225')
def e225(line):
    """Fix missing whitespace around operator."""
    for operator in _OPERATORS:
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


@Fix('E231')
def e231(line):
    """Fix missing white space after ','"""
    tokens = re.split(",(\S)", line)
    return "".join(", ".join(tokens[i:i + 2]) for i in range(0, len(tokens), 2))


@Fix('E261')
def e261(line):
    """Fix at least two spaces before inline comment"""
    i = line.index("#")
    return line[:i] + " " + line[i:]


@Fix('E262')
def e262(line):
    """Fix inline comment should start with '# '"""
    i = line.index("#") + 1
    return line[:i] + " " + line[i:]


@Fix('E302')
def e302(line):
    """Fix expected 2 lines, found 1."""
    return "\n" + line


# @Fix('E303')
def e303(line):
    """Fix too many blank lines (2)"""
    return ""


# @Fix('E701')
def e701(line):
    """Fix multiple statements on one line (colon)"""
    i = line.index(":")
    return line[:i] + "\n" + line[i:]


@Fix('W191')
def w191(line):
    """Fix W191 indentation contains tabs."""
    return line.expandtabs()


@Fix('W291')
def w291(line):
    """Fix trailing whitespace."""
    return line.rstrip() + "\n"


@Fix('W293')
def w293(line):
    """Fix blank line contains whitespace."""
    return "\n"


if __name__ == "__main__":
    import doctest
    doctest.testmod()
