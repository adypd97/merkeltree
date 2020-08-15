#!/usr/bin/env python3

class Node:
    def __init__(self, val):
        self.left = None
        self.right = None
        self.val = val


class Tree:
    def __init__(self):
        self.root = None

    def getRoot(self):
        return self.root

    def add(self, val):
        if self.root is None:
            self.root = Node(val)
        else:
            self._add(val, self.root)


    def _add(self, val, node):
        if val < node.val:
            if node.left is not None:
                self._add(val, node.left)
            else:
                node.left = Node(val)

        else:
            if node.right is not None:
                self._add(val, node.right)
            else:
                node.right = Node(val)

    def find(self, val):
        if self.root is not None:
            return self._find(val, self.root)
        else:
            return None

    def _find(self, val, node):
        if val == node.val:
            return node
        elif (val < node.val and node.light is not None):
            self._find(val, node.light)
        elif (val > node.val and node.right is not None):
            self._find(val, node.right)

    def deleteTree(self):
        self.root = None

    def printTree(self):
        if self.root is not None:
            self._printTree(self.root)

    def _printTree(self, node):
        if node is not None:
            self._printTree(node.left)
            print(str(node.val) + "  ")
            self._printTree(node.right)

tree = Tree()
tree.add(3)
tree.add(4)
tree.add(5)
tree.add(1)
tree.add(9)
tree.printTree()
print("######", tree.find(3).val)
tree.deleteTree()
try:
    print("######", tree.find(3).val)
except:
    print("Tree was deleted")

