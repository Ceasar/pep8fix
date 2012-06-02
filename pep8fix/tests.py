import tokenize

from nose.tools import assert_equal
import pep8

import fixes


# hack to generate tokens
# TODO: See if there is a better way to do this
def iden(x):
    yield x


class Pep8FixTester(object):
    oracle = None  # pep8 checker

    def tokenize(self, line):
        return tokenize.generate_tokens(iden(line).next)

    def ask(self, line, *args):
        oracle = getattr(pep8, self.oracle)

        location, msg = oracle(line, *args)
        try:
            _, cursor = location
        except TypeError:
            cursor = location
        code, _ = msg.split(None, 1)
        fixed = getattr(fixes, code.lower())(line, cursor)
        assert_equal(oracle(fixed, *args), None)


class TestMissingWhitespaceAroundOperator(Pep8FixTester):
    oracle = 'missing_whitespace_around_operator'

    def test_e225(self):
        for op in pep8.OPERATORS:
            line = "1%s2" % op
            yield self.ask, line, self.tokenize(line)
            line = "1 %s2" % op
            yield self.ask, line, self.tokenize(line)
            line = "1%s 2" % op
            yield self.ask, line, self.tokenize(line)
        lines = [
                'i=i+1',
                'submitted +=1',
                'x = x*2 - 1',
                'hypot2 = x*x + y*y',
                'c = alpha -4',
                'z = x **y'
                ]
        for line in lines:
            yield self.ask, line, self.tokenize(line)


class TestMissingWhitespace(Pep8FixTester):
    oracle = 'missing_whitespace'

    def test_e231(self):
        yield self.ask, "['a','b']"
        yield self.ask, "foo(bar,baz)"


class TestWhiteSpaceBeforeInlineComment(Pep8FixTester):
    oracle = 'whitespace_before_inline_comment'

    def test_e261(self):
        lines = ["x = x + 1 # Increment x"]
        for line in lines:
            yield self.ask, line, self.tokenize(line)

    def test_262(self):
        lines = ["x = x + 1  #Increment x", "x = x + 1  #  Increment x"]
        for line in lines:
            yield self.ask, line, self.tokenize(line)


class TestBlankLines(Pep8FixTester):
    oracle = 'blank_lines'

    def test_e302(self):
        yield self.ask, "\n"


class TestTabsObsolete(Pep8FixTester):
    oracle = 'tabs_obsolete'


class TestTrailingWhitespace(Pep8FixTester):
    oracle = 'trailing_whitespace'

    def test_w291(self):
        yield self.ask, "a = 1 \n"

    def test_w293(self):
        yield self.ask, " \n"
