'''
PROJECT 5 - AVL Trees
Name:
PID:
'''

import random as r      # To use for testing

class Node:
    # DO NOT MODIFY THIS CLASS #
    __slots__ = 'value', 'parent', 'left', 'right', 'height'

    def __init__(self, value, parent=None, left=None, right=None):
        """
        Initialization of a node
        :param value: value stored at the node
        :param parent: the parent node
        :param left: the left child node
        :param right: the right child node
        """
        self.value = value
        self.parent = parent
        self.left = left
        self.right = right
        self.height = 0

    def __eq__(self, other):
        """
        Determine if the two nodes are equal
        :param other: the node being compared to
        :return: true if the nodes are equal, false otherwise
        """
        if type(self) is not type(other):
            return False
        return self.value == other.value

    def __str__(self):
        """String representation of a node by its value"""
        return str(self.value)

    def __repr__(self):
        """String representation of a node by its value"""
        return str(self.value)

class AVLTree:

    def __init__(self):
        # DO NOT MODIFY THIS FUNCTION #
        """
        Initializes an empty Binary Search Tree
        """
        self.root = None    # The root Node of the tree
        self.size = 0       # The number of Nodes in the tree

    def __eq__(self, other):
        # DO NOT MODIFY THIS FUNCTION #
        """
        Describe equality comparison for BSTs ('==')
        :param other: BST being compared to
        :return: True if equal, False if not equal
        """
        if self.size != other.size:
            return False
        if self.root != other.root:
            return False
        if self.root is None or other.root is None:
            return True  # Both must be None

        if self.root.left is not None and other.root.left is not None:
            r1 = self._compare(self.root.left, other.root.left)
        else:
            r1 = (self.root.left == other.root.left)
        if self.root.right is not None and other.root.right is not None:
            r2 = self._compare(self.root.right, other.root.right)
        else:
            r2 = (self.root.right == other.root.right)

        result = r1 and r2
        return result

    def _compare(self, t1, t2):
        # DO NOT MODIFY THIS FUNCTION #
        """
        Recursively compares two trees, used in __eq__.
        :param t1: root node of first tree
        :param t2: root node of second tree
        :return: True if equal, False if nott
        """
        if t1 is None or t2 is None:
            return t1 == t2
        if t1 != t2:
            return False
        result = self._compare(t1.left, t2.left) and self._compare(t1.right, t2.right)
        return result

    def visual(self):
        """
        Returns a visual representation of the AVL Tree in terms of levels
        :return: None
        """
        root = self.root
        if not root:
            print("Empty tree.")
            return
        bfs_queue = []
        track = {}
        bfs_queue.append((root, 0, root.parent))
        h = self.height(self.root)
        for i in range(h+1):
            track[i] = []
        while bfs_queue:
            node = bfs_queue.pop(0)
            track[node[1]].append(node)
            if node[0].left:
                bfs_queue.append((node[0].left, node[1] + 1, node[0]))
            if node[0].right:
                bfs_queue.append((node[0].right, node[1] + 1, node[0]))
        for i in range(h+1):
            print(f"Level {i}: ", end='')
            for node in track[i]:
                print(tuple([node[0], node[2]]), end=' ')
            print()

    ### Implement/Modify the functions below ###

    def insert(self, node, value):
        """
        inserts a value in the correct avl tree order
        :param node: root of a tree inserting in
        :param value: value to be inserted
        :return: none
        """
        if self.root is None:
            self.root = Node(value)
            self.size += 1
            # creates the tree if there are no values in the tree
            return
        if node.value > value:
            if node.left is None:
                node.left = Node(value, parent=node)
                self.size += 1
                # adds the value if the correct spot is found, increment size
            else:
                self.insert(node.left, value)
        elif node.value < value:
            if node.right is None:
                node.right = Node(value, parent=node)
                self.size += 1
            else:
                self.insert(node.right, value)
                # recursively calls if the insertion spot has not been found yet
        if node:
            node.height = 1 + max(self.height(node.left), self.height(node.right))
            # after recursion, increment height for rebalance to work

        self.rebalance(node)
        # rebalances the tree after a node has been added
        return



    def remove(self, node, value):
        """
        removes a node passed if found
        :param node: root of the tree value is being removed from
        :param value: value to be removed
        :return: new root
        """
        if self.root is None:
            return
        # if the tree is empty, return

        if node.value == value:

            if self.size == 1:
                self.root = None
                self.size -= 1
                # removes root if the root is the value being removed and is the only node
                return

            elif self.height(node) == 0:
                # removes leaf node
                if node.value > node.parent.value:
                    node.parent.right = None
                else:
                    node.parent.left = None
                self.size -= 1
                # return to save value removed
                return

            elif node.left is None or node.right is None:
                # remove a node with one child
                if node.left is None:
                    node.value = node.right.value
                    node.right = None
                elif node.right is None:
                    node.value = node.left.value
                    node.left = None
                    # replace the value and update the child
                self.size -= 1
                if self.root.value == value:
                    self.root = node
                    # update root if needed

            elif node.left is not None and node.right is not None:
                # removes a node with two children
                max_val = self.max(node.left)
                # finds the max of the left child

                node.left = self.remove(node.left, max_val.value)
                # recursively calls remove until one of the previous cases is found, updates left node
                if self.root.value == value:
                    self.root.value = max_val.value
                    self.root.height = 1 + max(self.height(self.root.left), self.height(self.root.right))
                    return
                    # replaces root if needed

        elif node.value < value:
            if node.right is not None:
                self.remove(node.right, value)

        elif node.value > value:
            if node.left is not None:
                self.remove(node.left, value)
            # recursively calls remove until the value is found or the end of the tree is reached

        if node:
            node.height = 1 + max(self.height(node.left), self.height(node.right))
            # update height for rebalance

        self.rebalance(node)
        # rebalances tree if necessary
        return node


    def search(self, node, value):
        """
        looks for a certain value in the tree
        :param node: root of the tree being searched
        :param value: value searching for
        :return: node with value or node where value should be placed
        """
        temp = None
        while node is not None:
            temp = node
            # temp keeps track of previous node in case value is not found
            if node.value == value:
                return temp
            # returns the value if found
            elif node.value < value:
                node = node.right
            elif node.value > value:
                node = node.left
                # updates node until the end is reached
        return temp

    def inorder(self, node):
        """
        returns entire tree in order
        :param node: root of tree being ordered
        :return: generator of values
        """
        if node is None:
            return
        # return if the tree is empty
        else:
            yield from self.inorder(node.left)
            yield node
            yield from self.inorder(node.right)
            # recursively calls from left of the root
            # yields root
            # recursively calls from right of root

    def preorder(self, node):
        """
        returns tree as it is shown
        :param node: root of the tree
        :return: generator of tree values
        """
        if node is None:
            return
        # return if empty tree
        else:
            yield node
            yield from self.preorder(node.left)
            yield from self.preorder(node.right)
            # yields root, then left subtree, then right subtree

    def postorder(self, node):
        """
        returns smallest to largest then root
        :param node: root of a tree
        :return: generator of tree values
        """
        if node is None:
            return
        # return if tree is empty
        else:
            yield from self.postorder(node.left)
            yield from self.postorder(node.right)
            yield node
            # yields left subtrees, right subtrees, then root

    def depth(self, value):
        """
        finds the depth of the given value in the tree
        :param value: value to find in the tree
        :return: depth of that node
        """
        depth = 0
        node = self.search(self.root, value)
        if node is None:
            return -1
        # if the tree empty return -1
        elif node.value != value:
            return -1
        # if value not found, return -1
        while node.parent is not None:
            depth += 1
            node = node.parent
            # adds to depth moving up starting from the found node
        return depth


    def height(self, node):
        """
        returns the height of a node
        :param node: a node from the tree
        :return: the height of that node
        """
        if node is None:
            return -1
        # returns -1 if the node is none, otherwise returns the nodes height
        return node.height


    def min(self, node):
        """
        finds the minimum node of the tree
        :param node: root of the tree
        :return: minimum node
        """
        if node is None:
            return
        # if empty return
        if node.left is not None:
            min_val = self.min(node.left)
            # recursively calls through for each nodes left value until the last one is found
        else:
            min_val = node
            # updates the min for return
        return min_val


    def max(self, node):
        """
        returns node with max value of the tree
        :param node: root of a subtree
        :return: node with the max value
        """
        if node is None:
            return
        # return if empty
        if node.right is not None:
            max_val = self.max(node.right)
            # recursively calls until the right most node is found
        else:
            max_val = node
            # updates max val when last node found for return
        return max_val


    def get_size(self):
        """
        returns number of nodes in the tree
        :return: size of the tree
        """
        return self.size


    def get_balance(self, node):
        """
        gets the balance factor of a node
        :param node: a node of the tree
        :return: balance factor of the node
        """
        if node is None:
            return 0
        # return if none
        return self.height(node.left) - self.height(node.right)


    def left_rotate(self, root):
        """
        left rotates tree if needed
        :param root: root being rotated
        :return: new root of the subtree
        """

        if root.parent is not None:
            new_root = root.right
            new_root.parent = root.parent

            if new_root.right is not None:
                # left-left rotate case
                if new_root.left is not None:
                    new_root.left.parent = root
                    root.right = new_root.left
                else:
                    root.right = None
                # updates old roots left node
                root.parent = new_root
                if new_root.parent.value > new_root.value:
                    new_root.parent.left = new_root
                else:
                    new_root.parent.right = new_root
                    # places new root on correct side of its new parent
                new_root.left = root

            else:
                # left-right rotate case
                root.right = new_root.left
                root.parent.left = new_root
                root.parent = new_root
                if new_root.parent.value > new_root.value:
                    new_root.parent.left = new_root
                else:
                    new_root.parent.right = new_root
                new_root.left = root

        else:
            # self.root rotate case
            new_root = root.right
            new_root.parent = None
            root.parent = new_root

            if new_root.left is not None:
                new_root.left.parent = root
                root.right = new_root.left
                # case where size is 5
            elif new_root.right is not None:
                root.right = new_root.left
                # case where size is 3

            new_root.left = root
            self.root = new_root

        root.height = 1 + max(self.height(root.left), self.height(root.right))
        new_root.height = 1 + max(self.height(new_root.left), self.height(new_root.right))
        # updates heights of the node rotated and the new root
        return new_root


    def right_rotate(self, root):
        """
        rotates the tree right
        :param root: node being rotated
        :return: new root of the subtree
        """
        if root.parent is not None:
            new_root = root.left
            new_root.parent = root.parent
            # new root will be the left child of the node passed

            if new_root.left is not None:
                # right-right rotate case
                if new_root.right is not None:
                    new_root.right.parent = root
                    root.left = new_root.right
                else:
                    root.left = None
                    # updates left of the root
                root.parent = new_root
                if new_root.value > new_root.parent.value:
                    new_root.parent.right = new_root
                else:
                    new_root.parent.left = new_root
                    # makes sure new root is placed in the correct side of its new parent
                new_root.right = root

            else:
                # right-left case
                if new_root.right is not None:
                    new_root.right.parent = root
                root.left = new_root.right
                root.parent.right = new_root
                root.parent = new_root
                new_root.right = root
                # updates all necessary node attributes

        else:
            new_root = root.left
            new_root.parent = None
            root.parent = new_root
            # root shift case
            if new_root.right is not None:
                new_root.right.parent = root
                root.left = new_root.right
                # case where size is 5
            elif new_root.left is not None:
                root.left = new_root.right
                # case where size is 3
            new_root.right = root
            self.root = new_root
            # updates root

        root.height = 1 + max(self.height(root.left), self.height(root.right))
        new_root = 1 + max(self.height(new_root.left), self.height(new_root.right))
        # updates heights of the nodes that were rotated
        return new_root


    def rebalance(self, node):
        """
        rebalances the tree so the avl format is still in place
        :param node: root of the subtree that needs to be balanced
        :return: new root of the subtree
        """
        balance = self.get_balance(node)
        # gets the balance factor of the node passed
        if balance == 2:
            # balance of two means a right rotate is needed
            if self.get_balance(node.left) == -1:
                # checks if the node needs to be balanced twice
                self.left_rotate(node.left)
            return self.right_rotate(node)
        elif balance == -2:
            # balance of -2 means left rotate
            if self.get_balance(node.right) == 1:
                # checks if node needs to be balanced twice
                self.right_rotate(node.right)
            return self.left_rotate(node)

        return node

def repair_tree(tree):
    """
    fixes a tree where 2 nodes are swapped
    :param tree: tree being fixed
    :return: none
    """
    order = list(tree.inorder(tree.root))
    # gets the order of the tree
    size = tree.get_size()
    j = None
    s = None
    s2 = None
    # values being swapped
    # j is index before the index i
    if size == 1:
        return
    # no repair needed
    elif size == 2:
        if tree.root.left is None:
            if tree.root.right.value < tree.root.value:
                temp = tree.root.value
                tree.root.value = tree.root.right.value
                tree.root.right.value = temp
        else:
            if tree.root.left.value > tree.root.value:
                temp = tree.root.value
                tree.root.value = tree.root.left.value
                tree.root.left.value = temp
        # repairs a tree with 2 nodes depending on where the swap occured, left or right
        return
    for i in range(size):

        if i < size-1:
            if order[i].value > order[i+1].value and not s:
                s = order[i]
                # first node that needs to be swapped
            elif j is not None:
                if order[i].value < order[j].value:
                    s2 = order[i]
                    # second node that needs to be swapped
        else:
            if order[i].value < order[j].value:
                s2 = order[i]
                # checks if the last node needs to be swapped
        j = i
    if s is not None and s2 is not None:
        # if s and s2 are none, a swap was not needed
        temp = s.value
        s.value = s2.value
        s2.value = temp
        # actual value swap

    return

a = AVLTree()

insert_list = [50, 3, 15, 20, 18, 63, 75, 100, 148, 47, 68, 9, 71, 33]
print()
remove_list = [68, 75, 20, 63]

for i in insert_list:
    a.insert(a.root, i)
a.visual()
print()
a.remove(a.root, 68)
a.remove(a.root, 75)
a.remove(a.root, 20)
a.remove(a.root, 63)
a.visual()
