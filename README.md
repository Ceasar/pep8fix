Basic info
==========

pep8fix is a tool to automatically correct a bunch of errors raised when using the pep8 style-checker tool.

Requirements
============

pep8fix requires pep8 to be used.

Usage
=====

To use pep8fix, you'll need to first install pep8. Once installed, you can view each of the errors in a file via `pep8 myfile.py`. To fix them, simply pipe the output of pep8 into pep8fix as follows: `pep8 myfile.py | python pep8fix.py`.

pep8fix will then fix each of the errors and report the changes by printing the before and after lines it modifies. You can check them to ensure nothing catastrophic has happened. While pep8fix is intended not to break anything, it may be wise to make backups before running the script.

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

Note that pep8fix may not catch all of the errors on a single run. The script will only fix the errors that is sees from `pep8`. It's useful to run pep8 again to ensure no new style mistakes were uncovered.

Contributors
============

* Ceasar Bautista cbautista2010@gmail.com
