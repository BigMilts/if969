"""
This is a script which will import the packages
"""

from packages.structures.lists.linked_list import LinkedList

if __name__ == "__main__":
    default_list = [1, 2, 3, 5, 6]
    li1 = LinkedList(default_list)
    li2 = LinkedList()
    li2.insert(1)
