"""
A implementation of a linked_list, with yours methods and atributes
"""

from packages.structures.node import Node


class LinkedList:
    """
    A LinkedList Class
    """
    def __init__(self, iterable=None):
        """
        :param iterable: whatever iterable object here,
            will be followed and inserted in the linkedList
        """
        self._head = self._crt_node = None
        self._size = 0
        if iterable is not None:
            for element in iterable:
                self.insert(element)

    def __str__(self) -> str:
        """
        :return: the object representation
        """
        output = "( )"
        if self._head is not None:
            counter = 1
            output = "( "
            for node in self:
                if counter == 0:
                    output += str(node) + " ->"
                elif counter < self._size:
                    output += " " + str(node) + " ->"
                else:
                    output += " " + str(node) + " )"
                counter += 1
        return output

    def __iter__(self):
        """
        :return: just return the instance object
        """
        self._crt_node = self._head
        return self

    def __next__(self):
        """
        This method is overwritten in order to
        to set up the object iteration, on each iteration
        it returns the current node
        :return:
        """
        if self._crt_node is None:
            raise StopIteration
        current = self._crt_node
        self._crt_node = self._crt_node.get_next()
        return current

    def __len__(self):
        """
        :return: it returns the list length
        """
        return self._size

    def __repr__(self):
        output = "LinkedList()"
        if self._head is not None and self._size > 1:
            counter = 1
            output = output[:10]
            for node in self:
                if counter == 0:
                    output += f"([{node}, "
                elif counter < self._size:
                    output += f"{node}, "
                else:
                    output += f"{node}])"
                counter += 1
        elif self._size == 1:
            output = f"LinkedList([{str(self._head)}])"
        return output

    def __getitem__(self, item):
        current = self._head
        if item > self._size - 1:
            raise IndexError
        for i in range(item):
            current = current.get_next()
        return current

    def __setitem__(self, key, value):
        current = self.__getitem__(key)
        current.set_value(value)
        return self

    def __delitem__(self, key):
        if key > self._size - 1:
            raise IndexError
        current = self._head
        if self._size > 1:
            if key == 0:
                self._head = current.get_next()
            else:
                current = self._head
                for index in range(key):
                    aux = current
                    current = current.get_next()
                if key < self._size:
                    aux.set_next(current.get_next())
                elif key == self._size - 1:
                    aux.set_next(None)
        else:
            self._head = None
        del current
        self._size -= 1

    def index_of(self, value):
        """
        :param value: a value which is or not is in the list
        :return: the index of the value
        """
        index = counter = 0
        is_inlist = False
        if self._size > 1:
            for node in self:
                counter += 1
                if node.get_value() == value:
                    index = counter - 1
                    is_inlist = not is_inlist
            if not is_inlist:
                raise ValueError
        return index

    def insert(self, value):
        """
        :param value: a new value to be inserted in the list
        """
        new_node = Node(value)
        if self._head is not None:
            for node in self:
                if node.get_next() is None:
                    node.set_next(new_node)
        else:
            self._head = new_node
        self._size += 1

    def insert_on_order(self):
        pass

    def sort(self):
        pass

    def pop(self, key):
        """
        :param key: the index
        :return:
        """
        return self.__delitem__(key)
