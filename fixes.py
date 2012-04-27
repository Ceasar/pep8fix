import re


CODES = {}


class Fix(object):
    def __init__(self, issue):
        self.issue = issue

    def __call__(self, func):
        CODES[self.issue] = func


@Fix('E231')
def e231(swp, line):
    """Fix missing white space after ','"""
    print repr(line)
    tokens = re.split(",(\S)", line)
    fix = "".join(", ".join(tokens[i:i+2]) for i in range(0, len(tokens), 2))
    print repr(fix)
    swp.write(fix)


@Fix('E261')
def e261(swp, line):
    """Fix at least two spaces before inline comment"""
    print repr(line)
    i = line.index("#")
    fix = line[:i] + " " + line[i:]
    print repr(fix)
    swp.write(fix)


@Fix('E262')
def e262(swp, line):
    """Fix inline comment should start with '# '"""
    print repr(line)
    i = line.index("#") + 1
    fix = line[:i] + " " + line[i:]
    print repr(fix)
    swp.write(fix)


@Fix('E302')
def e302(swp, line):
    """Fix expected 2 lines, found 1."""
    print repr(line)
    fix = "\n" + line
    print repr(fix)
    swp.write(fix)


@Fix('W191')
def w191(swp, line):
    """Fix W191 indentation contains tabs."""
    print repr(line)
    fix = line.replace("\t", " " * 8)
    print repr(fix)
    swp.write(fix)


@Fix('W291')
def w291(swp, line):
    """Fix trailing whitespace."""
    print repr(line)
    fix = line.rstrip() + "\n"
    print repr(fix)
    swp.write(fix)


@Fix('W293')
def w293(swp, line):
    """Fix blank line contains whitespace."""
    print repr(line)
    fix = "\n"
    print repr(fix)
    swp.write(fix)
