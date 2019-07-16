from anytree import Node

class DirectoryNode(Node):
    """
    When using DirectoryNode, first create one without a name to be used as the root.
    Then when adding children or seaching, perform this on the root node of the tree.
    Directories are added implicitly with add_child.
    For example if you added /neodc/arsf/1986/86_09 with add_child, it will implicitly add /neodc/, /neodc/arsf/, /neodc/arsf/1986/, and then /neodc/arsf/1986/86_09 will be added.
    These names are what is returned with directory_path function, the actual nodes names are just the name of the directory and not the full path.
    When using search, the closes directory to the search term will be returned.
    Example:
    search(/neodc/arsf/1986/86_09/file) returns /neodc/arsf/1986/86_09/
    search(/neodc/arsf/1986/file) returns /neodc/arsf/1986/
    search(/neodc/arsf/1986/file/file1/file2/file3) returns /neodc/arsf/1986/
    search(file) returns None
    """
    def __init__(self, name=None, parent=None, children=None, **kwargs):
        """
        Creates a new directory node, uses parent's constructor (anytree.Node).
        If no name is given it is assumed that this is the root node of the tree and name is an empty string.
        """
        if not name:
            name = ""
        super().__init__(name, parent=parent, children=children, **kwargs)
    
    def valid_node(self, value):
        """
        Tests if a value is allowed to go into a directory tree. Nodes have to be non-empty strings.
        Parameters: value (String): Name of node to be tested before adding to the tree.
        Returns: True if node is valid, False if not (Boolean).
        """
        if not isinstance(value, str):
            return False
        if not value:
            return False
        
        return True

    def directory_path(self):
        """
        Get the full path of a directory node in the tree, not just the name of this directory.
        Returns: name (String).
        """
        names = [ancestor.name for ancestor in self.ancestors]
        names.append(self.name)

        return f'{"/".join(names)}/'
        
    def add_child(self, child_name):
        """
        Adds a child to the node, will add any missing children needed to add the child.
        Parameters: child_name (String): Name of directory to be added to the node. Example: '/neodc/arsf/1986/86_09' will add: neodc -> arsf -> 1986 -> 86_09
        """
        if not self.valid_node(child_name):
            raise ValueError(f"Invalid argument {child_name}")

        node = self
        if child_name[0] == "/":
            child_name = child_name[1:]
        for part in child_name.split("/"):
            for child in node.children:
                if part == child.name:
                    node = child
            if part != node.name:
                child = DirectoryNode(name=part, parent=node)
                node = child

    def search(self, query):
        """
        Search for a node using the tree nature of node's children. Returns the found node or as close as it got.
        Parameters: query (String): Name of child directory to be searched for under the node. Example: '/neodc/arsf/1986/86_09'.
        Returns: node (Node).
        """
        if not self.valid_node(query):
            raise ValueError(f"Invalid argument {query}")

        node = self
        for part in query.split("/")[1:]:
            for child in node.children:
                if part == child.name:
                    node = child
            if part != node.name:
                return node
        if node == self:
            return
        return node

    def search_name(self, query):
        """
        Search for a node using the tree nature of node's children. Returns the found node's name or as close as it got.
        Parameters: query (String): Name of child directory to be searched for under the node. Example: '/neodc/arsf/1986/86_09'.
        Returns: name (String).
        """

        if not self.valid_node(query):
            raise ValueError(f"Invalid argument {query}")

        match = self.search(query)

        if match:
            return match.directory_path()
        else:
            return
