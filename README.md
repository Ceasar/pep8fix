Basic info
==========

pep8fix is a tool to automatically correct a bunch of errors raised when using the pep8 style-checker tool.

Requirements
============

pep8fix requires pep8 to work.

You can download pep8 from pypi here: http://pypi.python.org/pypi/pep8

Usage
=====

To use pep8fix, you'll need to first install pep8. Once installed, you can use pep8 to view the style errors in a file via `pep8 *.py`. To fix them, simply pipe the output of pep8 into pep8fix: `pep8 *.py | python pep8fix.py`.

pep8fix will then fix each of the errors and report the changes by printing  each line it's changed before and after modification. You can inspect the changes to ensure nothing catastrophic has happened.


    19:26:05 ~/Desktop/pep8fix$ pep8 cis192turnin.py 
    cis192turnin.py:8:3: E111 indentation is not a multiple of four
    cis192turnin.py:10:1: W293 blank line contains whitespace
    cis192turnin.py:40:80: E501 line too long (110 characters)
    cis192turnin.py:57:16: E261 at least two spaces before inline comment
    19:26:09 ~/Desktop/pep8fix$ pep8 cis192turnin.py | python pep8fix.py 
    cis192turnin.py:8:3: E111 indentation is not a multiple of four
    cis192turnin.py:10:1: W293 blank line contains whitespace
    '  \n'
    '\n'
    cis192turnin.py:40:80: E501 line too long (110 characters)
    cis192turnin.py:57:16: E261 at least two spaces before inline comment
    '    raw_input() # pause\n'
    '    raw_input()  # pause\n'
    19:27:30 ~/Desktop/pep8fix$ pep8 cis192turnin.py 
    cis192turnin.py:8:3: E111 indentation is not a multiple of four
    cis192turnin.py:40:80: E501 line too long (110 characters)

Note that pep8fix may not catch all of the errors on a single run. The script will only fix the errors that is sees from running pep8. It's usually useful to run pep8 again to ensure no new style mistakes were uncovered.

Lastly, it's worth nothing that while many style changes can be automated, not all can. Some errors will always require a human to make correct them.

Warning
-------

While pep8fix is intended to only improve style, as a general note of caution, it may be wise to make backups (or commits) before running the script.

Contributors
============

* Ceasar Bautista cbautista2010@gmail.com
