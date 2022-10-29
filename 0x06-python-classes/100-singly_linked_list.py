#!/usr/bin/python3
"""
This is the "100-singly_linked_list" module.
This module contains the "Node" class that defines a node of
a singly linked list, and the "SinglyLinkedList" class that
defines a singly linked list.
"""


class Node:
    """
    Node class defines a node of a singly linked list by:

    Attributes:
        data - an integer value
        next_node - None or a Node

    """

    def __init__(self, data, next_node=None):
        """
        instatiation of an object
        """
        if type(data) is not int:
            raise TypeError("data must be an integer")
        self.__data = data
        if (type(next_node) is not None) and (type(next_node) is not type(next_node)):
            raise TypeError("next_node must be a Node object")
        self.__next_node = next_node

    @property
    def data(self):
        """getter for the data"""
        return self.__data

    @data.setter
    def data(self, value):
        """setter for data"""
        if type(value) is not int:
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """getter for nex_node"""
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """setter for next_node"""
        if (type(value) is not None) and (type(value) is not type(next_node)):
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    """
    SinglyLinkedList class - defines a singly linked list by:

    Attributes:
        head - the head of the singly linked list
    """
    def __init__(self):
        """instantiation of an object"""
        pass

    def sorted_insert(self, value):
        """Instance method that inserts a new Node"""
        """if SinglyLinkedList() == 0:"""
        __head = Node(value)
        return __head
    """def __repr__(self):
        ""printable list""
        return str(__head)"""
