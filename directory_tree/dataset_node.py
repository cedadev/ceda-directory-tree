"""
This extension of DirectoryNode is different in that when it is searched,
it will not return the closest directory in the tree that matched.
Instead it will return the closest directory in the tree that you actually added explicitly (dataset), not any implicit connecting directories that were added.

For example if you added ``/neodc/arsf/1986/86_09`` with add_child, it will implicitly add:

- ``/neodc/``
- ``/neodc/arsf/``
- ``/neodc/arsf/1986/``

Then the directory that you actually asked to be added, `/neodc/arsf/1986/86_09`, will be added as a "dataset".
When using search, only the closest matching dataset will be returned.

Example:
--------

- ``search(/neodc/arsf/1986/86_09/file)` --> ``/neodc/arsf/1986/86_09/``
- ``search(/neodc/arsf/1986/file)`` --> ``None``
"""

from directory_tree.directory_node import DirectoryNode
from anytree import Node

from typing import List


class DatasetNode(DirectoryNode):
    """
    Subclass of ``directory_tree.directory_node.DirectoryNode`` to provide more
    explicit dataset matching.
    """
    def __init__(self, name=None, parent=None, children=None, **kwargs):
        """
        Creates a new dataset node, uses parent's constructor (directory_tree.DirectoryNode).
        If no name is given it is assumed that this is the root node of the tree and name is an empty string.
        """
        self.dataset = False
        super().__init__(name, parent=parent, children=children, **kwargs)
        
    def add_child(self, child_name: str, **kwargs) -> None:
        """
        Adds a child to the node, will add any missing children needed to add the child.

        :param child_name: Name of dataset to be added to the node. Example: ``/neodc/arsf/1986/86_09``
        :param kwargs: Additional attributes added to the node.

        """

        if not self.valid_node(child_name):
            raise ValueError(f"Invalid argument {child_name}")

        node = self
        
        # Strip leading slash
        if child_name[0] == "/":
            child_name = child_name[1:]
        
        # Strip trailing slash
        if child_name.endswith("/"):
            child_name = child_name[:-1]
            
        for part in child_name.split("/"):
            for child in node.children:
                if part == child.name:
                    node = child
            if part != node.name:
                child = DatasetNode(name=part, parent=node, **kwargs)
                node = child
        node.dataset = True

    def search_all(self, query: str) -> List[Node]:
        """
        Return all dataset nodes in the path

        :param query: Name of child dataset to be searched for under the node. Example: ``/neodc/arsf/1986/86_09``
        :return: List of matching dataset nodes
        """

        if not self.valid_node(query):
            raise ValueError(f"Invalid argument {query}")

        node = self
        matches = []
        for part in query.split("/")[1:]:
            for child in node.children:
                if part == child.name:
                    node = child
                    if node.dataset:
                        matches.append(node)

            if part != node.name:
                return matches
        return matches

    def search(self, query: str) -> Node:
        """
        Search for a node using the tree nature of node's children.
        Returns the found node or the closest directory explicitly added when children were added.

        :param query: Name of child dataset to be searched for under the node. Example: ``/neodc/arsf/1986/86_09``
        :returns: node
        """

        if not self.valid_node(query):
            raise ValueError(f"Invalid argument {query}")

        node = self
        match = None
        for part in query.split("/")[1:]:
            for child in node.children:
                if part == child.name:
                    node = child
                    if node.dataset:
                        match = node

                    # Once you have a match, break the loop
                    break
            if part != node.name:
                return match
        return match
