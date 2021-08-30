"""
Good morning! Here's your coding interview problem for today.

This problem was asked by Google.

Given the root to a binary tree, 
implement serialize(root),
 which serializes the tree into a string, 
 and deserialize(s), 
 which deserializes the string back into the tree.

For example, given the following Node class

class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

The following test should pass:

node = Node('root', Node('left', Node('left.left')), Node('right'))
assert deserialize(serialize(node)).left.left.val == 'left.left'

"""

class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def deserialize(serialized: dict)-> Node:
    node = Node(serialized['val'])
    for key, value in serialized.items():
        if isinstance(value, dict):
            node.__dict__[key] = deserialize(value)
        else:
            node.__dict__[key] = value
    return node


def serialize(node: Node) -> dict:
    def loop_dict(dic: dict, acc: dict):
        for key, value in dic.items():
            if isinstance(value, Node):
                acc[key] = loop_dict(value.__dict__, {})
            else:
                acc[key] = value
        return acc
    return loop_dict(node.__dict__, {})

node = Node('root', Node('left', Node('left.left')), Node('right'))
assert deserialize(serialize(node)).left.left.val == 'left.left'

