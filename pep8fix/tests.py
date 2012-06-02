from nose.tools import assert_equal

import fixes


class Pep8FixTester(object):
    def test_cases(self):
        pass

    def oracle(self, given, expected):
        observed = getattr(fixes, self.code.lower())(given, 0)
        assert_equal(observed, expected)


class TestE225(Pep8FixTester):
    code = 'E225'

    def test_cases(self):
        yield self.oracle, "1+2", "1 + 2"
        yield self.oracle, "1 +2", "1 + 2"
        yield self.oracle, "1+ 2", "1 + 2"
        yield self.oracle, "1==2", "1 == 2"


class TestE231(Pep8FixTester):
    code = 'E231'

    def test_cases(self):
        yield self.oracle, '[1,2]', '[1, 2]'
        yield self.oracle, '[1,2,3]', '[1, 2, 3]'
        yield self.oracle, '[1,2]  # [1,2]', '[1, 2]  # [1,2]'


class TestE261(Pep8FixTester):
    code = 'E261'

    def test_cases(self):
        yield self.oracle, "1 + 2# s", "1 + 2  # s"
        yield self.oracle, "1 + 2 # s", "1 + 2  # s"
        yield self.oracle, "'s #s' # s", "'s #s'  # s"
        yield self.oracle, "1 + 2# s#s", "1 + 2  # s#s#"


class TestE262(Pep8FixTester):
    code = 'E262'

    def test_cases(self):
        yield self.oracle, "1 + 2  #s", "1 + 2  # s"
        yield self.oracle, "'#s'  #s", "'#s'  # s"
        yield self.oracle, "1 + 2  #s#", "1 + 2  # s#"


class TestE302(Pep8FixTester):
    code = 'E302'

    def test_cases(self):
        yield self.oracle, "\n", "\n\n"


class TestW191(Pep8FixTester):
    code = 'W191'


class TestW291(Pep8FixTester):
    code = 'W291'

    def test_cases(self):
        yield self.oracle, "a = 1 \n", "a = 1\n"


class TestW293(Pep8FixTester):
    code = 'W293'

    def test_cases(self):
        yield self.oracle, " \n", "\n"
