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
                self.add(element)

    def __str__(self) -> str:
        """
        :return: the object representation
        """
        output = "( )"
        if self._head is not None:
            counter = 0
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
        if self._head is not None:
            counter = 0
            output = output[:10]
            for node in self:
                if counter == 0:
                    output += f"([{node}, "
                elif counter < self._size:
                    output += f"{node}, "
                else:
                    output += f"{node}])"
                counter += 1
        return output

    def __getitem__(self, item):
        pass

    def add(self, value):
        """
        :param value: a new value to be inserted in the list
        """
        new_node = Node(value)
        if self._head is not None:
            for node in self:
                if node.get_next() is None:
                    node.set_next(new_node)
                    self._size += 1
        else:
            self._head = new_node
