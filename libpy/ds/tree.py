# Generic Tree
from __future__ import annotations # for metadeclare

"""
A node in a generic tree.

parent: GTNode -- GenericTree node. If this is None, then it means it is the root.
children: list[GTNode] -- List of the Generic Tree node childrens.
hash: int -- Hash of the GTNode (used as ID perhaps).
"""
class GTNode(object):
    def __init__(self, parent: GTNode | None = None):
        self.parent = parent
        self.children = []
        self.hash = hash(self)

    def __repr__(self):
        raise Exception("Error: Not implemented %s. Use repr_gt_node() function." % self.__class__.__name__) 

    """
    Wraps the repr_gt_node() function into the node.

    span: bool -- Represent the children of the node.
    indent_level: int -- Level of indentation for the dump cycle.
    """
    def print(self, span: bool = True, indent_level: int = 0):
        repr_gt_node(self, indent_level, span)



"""
Indicates how the tabs or the space between the nodes should be represented.
"""
TAB_REPR = "    "

"""
Represent a node in the Generic Tree.

node: GTNode -- Generic Tree Node to represent. (It will also represent the children nodes)
indent_level: int -- For representing in a prettier way.
span: bool -- Represent the children of the node.
"""
def repr_gt_node(node: GTNode, indent_level: int = 0, span: bool = True):
    # Subindent
    next_indent_level = indent_level + 1

    print("%(tab)s Node %(hash)s [\n%(tabi)s Parent %(phash)s\n%(tabi)s Children [" %
        {
            "tab": TAB_REPR*indent_level,
            "hash": str(node.hash),
            "phash": str(node.parent.hash) if node.parent is not None else "None",
            "tabi": TAB_REPR*(next_indent_level)
        })

    if span:
        for child in node.children:
            repr_gt_node(child, next_indent_level+1, span)
    else:
        # At least print identifiers
        for child in node.children:
            print("%(tab)s Node %(hash)s" % 
                {
                    "tab": (TAB_REPR*(next_indent_level+2)),
                    "hash": str(child.hash)
                }
            )

    print("%s ]" % (TAB_REPR*(next_indent_level)))
    print("%s ]" % (TAB_REPR*(indent_level)))
    
