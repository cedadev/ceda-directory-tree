.. directory-tree documentation master file, created by
   sphinx-quickstart on Fri Mar 19 11:27:07 2021.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to directory-tree's documentation!
==========================================

This package can be used to optimise directory and dataset lookup tables.

Speed comparison against a recursive lookup approach, shortening the path by
one each time and re-testing:

.. program-output:: directory-tree-speed-test

`Speed test code <https://github.com/cedadev/directory-tree/tree/master/directory_tree/examples/speed_test.py>`_

Installation
============

Install the library::

   pip install git+https://github.com/cedadev/directory-tree


Basic Usage
===========

.. code-block:: python

   directory_tree = DatasetNode()

    # Build the tree
    for path in path_list:
        directory_tree.add_child(path)

    # Search for path
   directory_tree.search_name(TEST_PATH)


.. toctree::
   :hidden:

   self


.. toctree::
   :maxdepth: 2
   :caption: API:

   api/node



Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
