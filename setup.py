"""Setup file for the tce."""

##############################################################################
# Python imports.
from pathlib    import Path
from setuptools import setup

##############################################################################
# Import the library itself to pull details out of it.
import tce

##############################################################################
# Work out the location of the README file.
def readme():
    """Return the full path to the README file.
    :returns: The path to the README file.
    :rtype: ~pathlib.Path
    """
    return Path( __file__ ).parent.resolve() / "README.md"

##############################################################################
# Load the long description for the package.
def long_desc():
    """Load the long description of the package from the README.
    :returns: The long description.
    :rtype: str
    """
    with readme().open( "r", encoding="utf-8" ) as rtfm:
        return rtfm.read()

##############################################################################
# Setup.
setup(

    name                          = "tce",
    version                       = tce.__version__,
    description                   = str( tce.__doc__ ),
    long_description              = long_desc(),
    long_description_content_type = "text/markdown",
    url                           = "https://github.com/wmramadan/tce",
    author                        = tce.__author__,
    author_email                  = tce.__email__,
    maintainer                    = tce.__maintainer__,
    maintainer_email              = tce.__email__,
    packages                      = ["tce"],
    data_files                    = ["tce/tce.css"],
    include_package_data          = True,
    zip_safe                      = False,
    install_requires              = [ "textual==0.7.0" ],
    python_requires               = ">=3.9",
    keywords                      = "terminal code editor",
    entry_points                  = {
        "console_scripts": "tce=tce.tce:main"
    },
    license                       = (
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)"
    ),
    classifiers                   = [
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Environment :: Console",
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Topic :: Terminals",
        "Topic :: Utilities",
        "Topic :: Software Development",
        "Typing :: Typed"
    ]

)
