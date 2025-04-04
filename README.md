
[![Test](https://github.com/cedadev/ceda-directory-tree/actions/workflows/test.yml/badge.svg)](https://github.com/cedadev/ceda-directory-tree/actions/workflows/test.yml)
![Static Badge](https://img.shields.io/badge/cci%20tagger%20workflow-8AD6F6)
[![PyPI version](https://badge.fury.io/py/ceda-directory-tree.svg)](https://pypi.python.org/pypi/ceda-directory-tree/)

# CEDA directory-tree
Data structure for storing and searching directory trees.

This repo provides a efficient process for matching paths against known directories.

[Library Documentation](https://cedadev.github.io/directory-tree/)

## Installation

Older versions:
`pip install ceda-directory-tree`


## Building and editing the docs

The documentation is written and built using the Sphinx workflow.

1. Install the docs requirements `pip install ceda-directory-tree[docs]
`
2. Edit the .rst files in the docsrc directory
3. Build the docs `make html`

This will build the docs and place in the `docsrc/build/html` directory. It will also
copy the html to the `/doc` directory for serving with github pages.
