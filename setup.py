from distutils.core import setup

import pep8fix


setup(
    name="pep8fix",
    version=pep8fix.__version__,
    description="pep8 style enforcer",
    author="Ceasar Bautista",
    author_email="cbautista2010@gmail.com",
    url="http://www.github.com/Ceasar/pep8fix",
    scripts=["pep8fix/pep8fix"],
    packages=["pep8fix"]
)
