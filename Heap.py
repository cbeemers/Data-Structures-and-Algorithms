'''
PROJECT 6 - Heaps
Name: Christopher Beeman
PID: A53041935
'''

class Node:
    """
    Class definition shouldn't be modified in anyway
    """
    __slots__ = ('_key', '_val')

    def __init__(self, key, val):
        self._key = key
        self._val = val

    def __lt__(self, other):
        return self._key < other._key or (self._key == other._key and self._val < other._val)

    def __gt__(self, other):
        return self._key > other._key or (self._key == other._key and self._val > other._val)

    def __eq__(self, other):
        return self._key == other._key and self._val == other._val

    def __str__(self):
        return '(k: {0} v: {1})'.format(self._key, self._val)

    __repr__ = __str__

    @property
    def val(self):
        """
        :return: underlying value of node
        """
        return self._val


class Heap:
    """
    Class definition is partially completed.
    Method signatures and provided methods may not be edited in any way.
    """
    __slots__ = ('_size', '_capacity', '_data')

    def __init__(self, capacity):
        self._size = 0
        self._capacity = capacity + 1  # additional element space for push
        self._data = [None for _ in range(self._capacity)]

    def __str__(self):
        return ', '.join(str(el) for el in self._data if el is not None)

    __repr__ = __str__

    def __len__(self):  # allows for use of len(my_heap_object)
        return self._size

#    DO NOT MODIFY ANYTHING ABOVE THIS LINE
#    Start of Student Modifications

    def _percolate_up(self):
        '''
        takes the last node and moves up until it is placed correctly
        :return: None
        '''
        percolate = self._data[self._size - 1]
        # last element being moved
        temp = self._size - 1
        parent_id = (self._size - 2) // 2
        # the parent of the element
        while parent_id >= 0:
            if percolate < self._data[parent_id]:
                parent = self._data[parent_id]
                self._data[parent_id] = percolate
                self._data[temp] = parent
                # swaps the values if the lower element is less than its parent
            temp = parent_id
            parent_id = (parent_id - 1) // 2
            # update parent and tracker indexes
        return

    def _percolate_down(self):
        '''
        moves an element down from the root until it is in the correct spot
        :return: None
        '''
        percolate = self._data[0]
        temp = 0
        # keep track of the element and the original index
        while temp < self._size:
            child = 2*temp + 1
            # finds the children of the element
            if (child + 1) < self._capacity:
                # checks if the children are in the range of the fixed size
                if self._data[child] is not None and self._data[child+1] is not None:
                    # checks if both children are not None
                    if percolate > self._data[child] and percolate > self._data[child+1]:
                        if self._data[child] > self._data[child+1]:
                            node = self._data[child+1]
                            self._data[child+1] = percolate
                            self._data[temp] = node
                            temp = child+1
                        else:
                            node = self._data[child]
                            self._data[child] = percolate
                            self._data[temp] = node
                            temp = child
                        # swaps with the min child if greater than both

                    elif percolate > self._data[child]:
                        node = self._data[child]
                        self._data[child] = percolate
                        self._data[temp] = node
                        temp = child

                    elif percolate > self._data[child+1]:
                        node = self._data[child+1]
                        self._data[child+1] = percolate
                        self._data[temp] = node
                        temp = child + 1
                    # swaps with the child it is greater than if not greater than both
                    else:
                        break
                        # breaks if it is found to be in the correct spot
                elif self._data[child] is not None:
                    node = self._data[child]
                    self._data[child] = percolate
                    self._data[temp] = node
                    temp = child
                elif self._data[child+1] is not None:
                    node = self._data[child+1]
                    self._data[child+1] = percolate
                    self._data[temp] = node
                    temp = child + 1
                # case where the element only has one child
                # swaps if greater
                else:
                    break
                    # breaks if the element is a leaf
            else:
                break
                # breaks if the end of the heap is reached
        return

    def _min_child(self, i):
        '''
        finds the min child of a node at a given index
        :param i: index of the node
        :return: min node
        '''
        child = 2*i + 1
        if child + 1 < self._capacity:
            if self._data[child] is None and self._data[child + 1] is None:
                return -1
            # if index is a leaf, return -1
            elif self._data[child] is not None and self._data[child + 1] is not None:
                if self._data[child] > self._data[child + 1]:
                    return child+1
                else:
                    return child
                # if element has 2 children, compare and return the smaller node
            elif self._data[child] is None:
                return child+1
            elif self._data[child + 1] is None:
                return child
            # if only one child, return that child
        else:
            return -1

    def push(self, key, val):
        '''
        adds a node to the heap
        :param key: key for the node
        :param val: value of the node
        :return: None
        '''
        node = Node(key, val)
        if self._capacity == 1:
            return
        if self._size == 0:
            self._data[0] = node
            self._size += 1
            return
        # adds the first element to the heap
        self._data[self._size] = node
        self._size += 1
        self._percolate_up()
        # updates _data and _size then percolates the new element that was added to the bottom up
        if self._data[self._capacity-1] is not None:
            self.pop()
            # pops if the size is equal to the capacity
        return

    def pop(self):
        '''
        removes the top element of the heap
        :return: the value of the top element
        '''
        if self._size == 0:
            return
        temp = self._data[0].val
        self._data[0] = self._data[self._size - 1]
        self._percolate_down()
        # replaces the root node with the last node and percolates down to its correct place
        if self._size == self._capacity:
            self._data[self._capacity-1] = None
            # ensures the size is not equal to the fixed capacity
        else:
            self._data[self._size-1] = None
            # removes the last element that was swapped with the top
        self._size -= 1
        # update size
        return temp


    @property  # do not remove
    def empty(self):
        '''
        checks if the heap is empty
        :return: boolean
        '''
        return self._size == 0

    @property  # do not remove
    def top(self):
        '''
        returns top node value
        :return: top node value
        '''
        if self._size == 0:
            return
        return self._data[0].val

    @property  # do not remove
    def levels(self):
        '''
        creates a list of lists containing nodes on the same levels
        :return: list of lists with nodes
        '''
        if self._size == 0:
            return []
        return_list = []
        level = 1
        levels = []
        for i in range(self._size):
            if self._data[i]:
                levels.append(self._data[i])
                # checks that the node is not None
            if i < level-1:
                # if the index is still a child of one of the elements continue
                if i == self._size - 1:
                    return_list.append(levels)
                    # if the end of the heap is reached before its last possible child is found, append
                continue

            return_list.append(levels)
            # append after all children of a node are checked
            level = 2 * level + 1
            # update level to be the child of the current index
            levels = []
            # resets the levels list

        return return_list


def most_x_common(vals, X):
    '''
    finds the most common string values in a list
    :param vals: a list of strings
    :param X: the number of elements to return
    :return: set of the values most found in the list
    '''
    heap = Heap(X)
    d = dict()
    l = ''
    for i in vals:
        if i not in d:
            d[i] = 1
        else:
            d[i] += 1
            # create the dictionary with string as key and count as value
        if len(heap) == 0:
            heap.push(d[i], i)
            # initialize the heap
        elif len(heap) < X:
            if i == heap.top:
                heap.pop()
                # updates a node if another instance is found with a greater count
            heap.push(d[i], i)
        else:
            heap.push(d[i], i)

    for i in range(len(heap)):
        l = heap.pop() + l
        # creates a string of the values for return
    return set(l)


# heap = Heap(8)
# heap.push(10, 10)
# heap.push(1, 10)
# heap.push(12, 13)
# heap.push(0,9)
# heap.push(10,9)
# heap.push(10,3)
# heap.push(3,4)
# heap.push(2,3)
# heap.push(13,7)
# print(heap._data)

heap = Heap(10)
heap.push(5, 'c')
heap.push(4, 'y')
heap.push(3, 'n')
heap.push(2, 'd')
heap.push(5, 'y')
heap.push(6, 'r')
heap.push(7, 'r')
heap.push(8, 'u')
#print(heap.levels)
#print(heap._min_child(0))
#print(heap._data)

result = most_x_common(['a', 'a', 'a', 'b', 'b', 'b', 'c'], 3)
print(result)

# d = most_x_common(['a','a','a','b','c','d','c'], 2)
# print(d)
# for i in d:
#     print(d, d[i])
# heap = Heap(2)
# heap.push(5, 'c')
# heap.push(4, 'y')
# heap.push(3, 'n')
# print(heap._min_child(0))
# print(heap._data)
