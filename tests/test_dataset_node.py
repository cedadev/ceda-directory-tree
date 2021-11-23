# encoding: utf-8
"""

"""
__author__ = 'Richard Smith'
__date__ = '23 Nov 2021'
__copyright__ = 'Copyright 2018 United Kingdom Research and Innovation'
__license__ = 'BSD - see LICENSE file in top-level package directory'
__contact__ = 'richard.d.smith@stfc.ac.uk'

import pytest

from directory_tree import DatasetNode

@pytest.fixture
def tree():
    return DatasetNode()


def test_add_child(tree):

    dataset_path = '/badc/faam/a/b/c/'
    tree.add_child(dataset_path)

    node = tree.search('/badc/faam/a/b/c/d/e')

    assert node.dataset
    assert node.directory_path() == dataset_path


def test_extra_args(tree):
    dataset_path = '/badc/faam/a/b/c/'
    tree.add_child(dataset_path, description_file='file1')

    node = tree.search('/badc/faam/a/b/c/d/e')

    assert node.dataset
    assert node.directory_path() == dataset_path
    assert node.description_file == 'file1'

def test_search_all(tree):

    path1 = '/badc/faam/a/'
    path2 = '/badc/faam/a/b/c/'

    tree.add_child(path1)
    tree.add_child(path2)

    nodes = tree.search_all('/badc/faam/a/b/c/d/e/')

    assert len(nodes) == 2
    assert nodes[0].directory_path() == path1
    assert nodes[1].directory_path() == path2


def test_out_of_order_add_child(tree):

    path1 = '/badc/faam/a/'
    path2 = '/badc/faam/a/b/c/'

    tree.add_child(path2, description_file='file2')
    tree.add_child(path1, description_file='file1')

    nodes = tree.search_all('/badc/faam/a/b/c/d/e/')

    assert nodes[0].description_file == 'file1'
    assert nodes[1].description_file == 'file2'


