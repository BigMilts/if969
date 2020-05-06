"""
A simple sample of node, which it's function is only use pointers to help to build
 some samples data structure
"""


class Node:
    """
     The Node class have two pointers
    """
    def __init__(self, value):
        """
        :param value: this param can be anything such as a list, a dictionary...
        """
        self._value = value
        self._next = None
        self._prev = None

    def get_value(self):
        """
        :return: it returns the node current value
        """
        return self._value

    def set_value(self, value):
        """
        :param value: the value which will be the new value of the node
        """
        self._value = value

    def get_next(self):
        """
        :return: return the other object(in this case the next object)
        """
        return self._next

    def set_next(self, init_next):
        """
        :param init_next: is a reference to other object(in this case the next object)
        """
        self._next = init_next

    def get_prev(self):
        """
        :return: return the previous object
        """
        return self._prev

    def set_prev(self, init_prev):
        """
        :param init_prev: it is a reference to other object(in this case the previous object)
        """
        self._prev = init_prev

    def __str__(self) -> str:
        """
        :return: the representation of the value in a string
        """
        return str(self.get_value())

    def __repr__(self) -> str:
        """
        :return: in this case it will return the __str__ method
        """
        return self.__str__()
