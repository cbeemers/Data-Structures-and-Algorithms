'''
PROJECT 7 - Hash Tables
Name:
PID:
'''

class HashNode:
    """
    DO NOT EDIT
    """
    __slots__ = ["key", "value", "deleted"]

    def __init__(self, key, value, deleted=False):
        self.key = key
        self.value = value
        self.deleted = deleted

    def __repr__(self):
        return f"HashNode({self.key}, {self.value})"

    def __eq__(self, other):
        return self.key == other.key and self.value == other.value


class HashTable:
    """
    Hash Table Class
    """
    __slots__ = ['capacity', 'size', 'table', 'collisions', 'prime_index']

    primes = (
        2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83,
        89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179,
        181, 191, 193, 197, 199, 211, 223, 227, 229, 233, 239, 241, 251, 257, 263, 269, 271, 277,
        281, 283, 293, 307, 311, 313, 317, 331, 337, 347, 349, 353, 359, 367, 373, 379, 383, 389,
        397, 401, 409, 419, 421, 431, 433, 439, 443, 449, 457, 461, 463, 467, 479, 487, 491, 499,
        503, 509, 521, 523, 541, 547, 557, 563, 569, 571, 577, 587, 593, 599, 601, 607, 613, 617,
        619, 631, 641, 643, 647, 653, 659, 661, 673, 677, 683, 691, 701, 709, 719, 727, 733, 739,
        743, 751, 757, 761, 769, 773, 787, 797, 809, 811, 821, 823, 827, 829, 839, 853, 857, 859,
        863, 877, 881, 883, 887, 907, 911, 919, 929, 937, 941, 947, 953, 967, 971, 977, 983, 991,
        997)

    def __init__(self, capacity=8):
        """
        DO NOT EDIT
        Initializes hash table
        :param capacity: capacity of the hash table
        """
        self.capacity = capacity
        self.size = 0
        self.table = [None] * capacity

        i = 0
        while HashTable.primes[i] <= self.capacity:
            i += 1
        self.prime_index = i - 1

    def __eq__(self, other):
        """
        DO NOT EDIT
        Equality operator
        :param other: other hash table we are comparing with this one
        :return: bool if equal or not
        """
        if self.capacity != other.capacity or self.size != other.size:
            return False
        for i in range(self.capacity):
            if self.table[i] != other.table[i]:
                return False
        return True

    def __repr__(self):
        """
        DO NOT EDIT
        Represents the table as a string
        :return: string representation of the hash table
        """
        represent = ""
        bin_no = 0
        for item in self.table:
            represent += "[" + str(bin_no) + "]: " + str(item) + '\n'
            bin_no += 1
        return represent

    def __setitem__(self, key, value):
        """
        DO NOT EDIT
        Allows for the use of the set operator to insert into table
        :param key: string key to insert
        :param value: value to insert
        :return: None
        """
        return self.insert(key=key, value=value)

    def __getitem__(self, item):
        """
        DO NOT EDIT
        Allows get operator to retrieve a value from the table
        :param item: string key of item to retrieve from tabkle
        :return: HashNode
        """
        return self.get(item)

    def __contains__(self, item):
        """
        DO NOT EDIT
        Checks whether a given key exists in the table
        :param item: string key of item to retrieve
        :return: Bool
        """
        if self.get(item) is not None:
            return True
        return False

    def _hash_1(self, key):
        """
        ---DO NOT EDIT---
        Converts a string x into a bin number for our hash table
        :param x: key to be hashed
        :return: bin number to insert hash item at in our table, -1 if x is an empty string
        """
        if not key:
            return None
        hashed_value = 0

        for char in key:
            hashed_value = 181 * hashed_value + ord(char)
        return hashed_value % self.capacity

    def _hash_2(self, key):
        """
        ---DO NOT EDIT---
        Converts a string x into a hash
        :param x: key to be hashed
        :return: a hashed value
        """
        if not key:
            return None
        hashed_value = 0

        for char in key:
            hashed_value = 181 * hashed_value + ord(char)

        prime = HashTable.primes[self.prime_index]

        hashed_value = prime - (hashed_value % prime)
        if hashed_value % 2 == 0:
            hashed_value += 1
        return hashed_value

    """ **************** Student Section Below ****************************** """

    def hash(self, key, inserting=False):
        """
        takes a key and finds the index where the node is/should go in the table using double hashing
        :param key: string key to find the index of
        :param inserting: boolean whether or not the key is being inserted
        :return: index of where a node with key is/should be
        """

        index = self._hash_1(key)
        if index is None:
            return
        # if empty string, return

        i = 1
        node = self.table[index]
        while node:
            # keeps looping until table[index] is None or something is returned
            if not node.deleted:
                if node.key == key:
                    return index
                # returns index if the key passed is found in the table
            if inserting:
                if node.deleted:
                    return index
                # returns the index of a deleted node if inserting is true

            index = (self._hash_1(key) + i * self._hash_2(key)) % self.capacity
            i += 1
            node = self.table[index]
            # updates index using double hashing

        return index

    def insert(self, key, value):
        """
        places a node with key and value into the hash table
        :param key: key of the node being inserted
        :param value: value of the new node
        :return: None
        """

        index = self.hash(key, inserting=True)
        if index is None:
            return
        # if key empty string, return

        node = self.table[index]
        if node:
            if node.key == key:
                node.value = value
                return
            # if the key is already in the table, update its value

        self.table[index] = HashNode(key, value)
        self.size += 1
        # inserts the new node at the index found

        if self.size >= self.capacity/2 and self.capacity <= 500:
            self.grow()
            # if the size is greater than the capacity times a load factor of 0.5, grow
            # capacity can never be more than 1000
        return

    def get(self, key):
        """
        finds the node with given key in the hash table
        :param key: key searching for
        :return: None if empty or the key is not in the table, otherwise node of given key
        """

        if self.size == 0:
            return
        # return none if empty table

        index = self.hash(key)
        if index is None:
            return
        # find index of key using hash function and return the node if not None
        return self.table[index]

    def delete(self, key):
        """
        removes a node with given key in the table
        :param key: key to be removed
        :return: None
        """

        index = self.hash(key)
        if index is None:
            return
        # finds index of the passed key, returns none if empty string passed

        node = self.table[index]
        if node:
            if node.key == key:
                node.key = None
                node.value = None
                node.deleted = True
                self.size -= 1
            # if the key found at index is the key passed, update key, value, deleted and size

        return

    def grow(self):
        """
        grows size of table if size is greater than or equal to capacity * load factor of 0.5
        :return: None
        """

        self.capacity *= 2
        hash = HashTable(self.capacity)
        self.prime_index = hash.prime_index
        # updates capacity and creates new hash table
        # updates prime index for double hashing

        index = 0
        while index < (self.capacity/2):
            node = self.table[index]
            if node:
                if not node.deleted:
                    hash.insert(node.key, node.value)
            index += 1
        # goes through each index of the original table and inserts the node in the new table as long as not deleted

        self.table = hash.table
        # update table

        return


def word_frequency(string, lexicon, table):
    """
    splits string, finding a new word in lexicon and updating its frequency value in table
    :param string: a string to be split into multiple words
    :param lexicon: a list of all words that can be placed into the table
    :param table: a hash table to easily update values
    :return: hash table with every word in lexicon as key and its frequency in string as value
    """

    for word in lexicon:
        table.insert(word, 0)
        # initialize table with every word in the lexicon

    c = ''
    # substring of string to potentially be added to table
    i = 0
    # used for indexing string
    temp = ''
    # substring of string that makes sure the longest word possible is added
    retrace = False
    # boolean that decides whether or not there was an error and we have to go back in the string
    wordList = []
    # wordList is a list of all words added to the table in order of when they appeared in string

    while i < len(string):

        c += string[i]
        # c is always a substring of string

        if c in lexicon:
            j = i + 1
            node = table.get(c)
            d = c
            temp = ''
            # initialize place holders for checking if c is the longest it can be

            while j < len(string) and not retrace:
                d += string[j]
                if d in lexicon:
                    temp = d
                j += 1
                # update temp to longer word

            if temp:
                node = table.get(temp)
                i += (len(temp) - len(c))
                table.insert(temp, node.value + 1)
                wordList.append(temp)
                c = ''
                # update wordList, table, i, and c
            else:
                table.insert(c, node.value + 1)
                wordList.append(c)
                c = ''
                # update wordList and c
                retrace = False
                # whenever c is inserted, retrace can be set to false

        i += 1
        if len(c) > 20 or (i == len(string) and c):
            # if a word was inserted when it shouldn't have been
            if temp == wordList[-1]:
                # if the last word added was temp
                i -= (len(c) + len(temp))
                # update i so we can go through the string again where the error occurred
                node = table.get(temp)
                wordList.pop(-1)
                retrace = True
                c = ''
                # update wordList, and c
                # set retrace to true so c will be added
            else:
                # if the last word added was c
                node = table.get(wordList[-1])
                c = wordList.pop(-1)
                i -= len(c)
                # update i so you can go back through the string

            node.value -= 1
            # decrement the frequency of the last added key

    return table

