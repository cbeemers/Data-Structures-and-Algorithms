########################################
# PROJECT 1 - Linked List
# Author: Christopher Beeman
# Solution: Linked List class creates a
# list of sequential values, with many
# methods to alter and view the list
# PID: A53041935
########################################


class Node:
    # DO NOT MODIFY THIS CLASS #
    __slots__ = 'value', 'next_node'

    def __init__(self, value, next_node=None):
        """
        DO NOT EDIT
        Initialize a node
        :param value: value of the node
        :param next_node: pointer to the next node, default is None
        """
        self.value = value  # element at the node
        self.next_node = next_node  # reference to next node

    def __eq__(self, other):
        """
        DO NOT EDIT
        Determine if two nodes are equal (same value)
        :param other: node to compare to
        :return: True if nodes are equal, False otherwise
        """
        if other is None:
            return False
        if self.value == other.value:
            return True
        return False

    def __repr__(self):
        """
        DO NOT EDIT
        String representation of a node
        :return: string of value
        """
        return str(self.value)

    __str__ = __repr__
../

class LinkedList:
    def __init__(self):
        """
        DO NOT EDIT
        Create/initialize an empty linked list
        """
        self.head = None   # Node
        self.tail = None   # Node
        self.size = 0      # Integer

    def __eq__(self, other):
        """
        DO NOT EDIT
        Defines "==" (equality) for two linked lists
        :param other: Linked list to compare to
        :return: True if equal, False otherwise
        """
        if self.size != other.size:
            return False
        if self.head != other.head or self.tail != other.tail:
            return False

        # Traverse through linked list and make sure all nodes are equal
        temp_self = self.head
        temp_other = other.head
        while temp_self is not None:
            if temp_self == temp_other:
                temp_self = temp_self.next_node
                temp_other = temp_other.next_node
            else:
                return False
        # Make sure other is not longer than self
        if temp_self is None and temp_other is None:
            return True
        return False

    def __repr__(self):
        """
        DO NOT EDIT
        String representation of a linked list
        :return: string of list of values
        """
        temp_node = self.head
        values = []
        if temp_node is None:
            return None
        while temp_node is not None:
            values.append(temp_node.value)
            temp_node = temp_node.next_node
        return str(values)

    __str__ = __repr__

    ###### students modify the below functions #####

    # ------------------------Accessor Functions---------------------------

    def length(self):
        """
        :return: number of nodes in the linked list
        """
        return self.size

    def is_empty(self):
        """
        :return: True or false depending on the linked list being empty
        """
        return self.size == 0

    def front_value(self):
        """
        :return: the head value of the linked list
        """
        if self.head is not None:
            return self.head.value
        else:
            return None
        #returns none if the list is empty

    def back_value(self):
        """
        :return: the tail value of the linked list
        """
        if self.tail is not None:
            return self.tail.value
        else:
            return None
        #returns none if the list is empty

    def count(self, val):
        """
        counts total occurrences of a value in the list
        :param val: a value to search for and count
        :return: the number of occurrences of val in the list
        """
        count = 0
        temp = self.head
        while temp is not None:
            if temp.value == val:
                count += 1
                temp = temp.next_node
                #if the value is found update the count and node in question
                #else, just update node
            else:
                temp = temp.next_node
        return count


    def find(self, val):
        """
        searches for a value in the linked list
        :param val: a value to look for in the list
        :return: True or false depending on whether or not the value was found
        """
        temp = self.head
        while temp is not None:
            if temp.value == val:
                return True
            #returns true if the value is found
            else:
                temp = temp.next_node
            #keeps updating node in question

        return False

    # ------------------------Mutator Functions---------------------------

    def push_front(self, val):
        """
        adds a node with value val to the front of the linked list
        :param val: a value to be added as the head
        :return: None type
        """
        added = Node(val)
        if self.head is None:
            self.head = added
            self.tail = added
            #checks for empty list
        else:
            added.next_node = self.head
            self.head = added
            #updates head to be new value node passed
        self.size += 1
        return

    def push_back(self, val):
        """
        adds a node with value val to the end of the linked list
        :param val: a value to be added as the tail
        :return: None type
        """
        added = Node(val)
        if self.head is None:
            self.head = added
            self.tail = added
            #tests empty list case
        else:
            self.tail.next_node = added
            self.tail = added
            #updates tail
        self.size += 1
        return

    def pop_front(self):
        """
        removes the front value from the linked list and updates the head
        :return: the value of the node being removed
        """
        temp = self.head
        #keeps track of the original head node
        if self.head is not None:
            val = self.head.value
            #assigns the value of the node being removed for return
            if self.head.next_node is not None:
                self.head = temp.next_node
                temp.next_node = None
                #checks for single element in the list
            else:
                self.head = None
                self.tail = None
                #accounts for empty list after popping
            self.size -= 1
            return val
        else:
            return None

    def pop_back(self):
        """
        removes the back value from the linked list and updates the tail
        :return: the value of the node being removed
        """
        temp = self.head
        if self.head is not None:
            val = self.tail.value
            #assigns value of the tail to return
            if self.head.next_node is None:
                self.head = None
                self.tail = None
                self.size -= 1
                #makes the list empty if the node being removed is the only one
                return val
            while temp.next_node is not None:
                temp2 = temp
                temp = temp.next_node
                #cycles through the nodes with temp at the end of the iteration being the node before tail
            temp2.next_node = None
            self.tail = temp2
            self.size -= 1
            #update tail and size then return
            return val
        else:
            return None

def partition(linked_list, x):
    """
    separates linked list based on the value being passed
    :param linked_list: a linked list to split
    :param x: split based off this value
    :return: linked list with values less than x first then the values greater than or equal
    """
    llist = LinkedList()
    llist2 = LinkedList()
    #initialize linked lists to be used
    for i in range(0, linked_list.length()):
        val = linked_list.front_value()
        linked_list.pop_front()
        #removes each value for linked list since it cant be indexed
        if val >= x:
            llist.push_back(val)
            #pushes back if the value is greater than or equal to the val passed
        else:
            llist2.push_front(val)
    for i in range(0, llist2.length()):
        val2 = llist2.front_value()
        llist2.pop_front()
        llist.push_front(val2)
        #reversed the order of the second linked list created so the values less than x are in their original order
    return llist
