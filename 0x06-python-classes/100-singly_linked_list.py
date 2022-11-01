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
        """if (type(next_node) is not None) and (type(next_node) is not type(self)):
            raise TypeError("next_node must be a Node object")"""
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
        """if (type(value) is not None) and (type(value) is not type(self)):
            raise TypeError("next_node must be a Node object")"""
        self.__next_node = value


class SinglyLinkedList:
    """
    SinglyLinkedList class - defines a singly linked list by:

    Attributes:
        head - the head of the singly linked list
    """

    def __init__(self):
        """instantiation of an object"""
        self.__head = None

    def sorted_insert(self, value):
        """Instance method that inserts a new Node"""
        """node = Node(value)
        if SinglyLinkedList.__count_insert == 1:
            self.__head = node
        return self.__head.data"""
        node = Node(value)
        if self.__head:
            if self.__head.data >= value:
                node.next_node = self.__head
                self.__head = node
            else:
                tmp = self.__head
                prev = self.__head
                while tmp.next_node:
                    tmp = tmp.next_node
                    if (tmp.data < value) and prev.data < value:
                        prev = prev.next_node
                    elif (tmp.data >= value) and prev.data <= value:
                        prev.next_node = node
                        node.next_node = tmp
                        break
                else:
                    prev.next_node = node
        else:
            self.__head = node
        return self.__head
        
    def __str__(self):
        """printable list"""
        node = self.__head
        while node.next_node:
            print(node.data)
            node = node.next_node
        return str(node.data)
