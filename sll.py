# Name: Homero Vazquez
# OSU Email: vazqueho@oregonstate.edu
# Course: CS261 - Data Structures
# Assignment: 3
# Due Date: 2/10/2026
# Description:


from SLNode import *



class SLLException(Exception):
    """
    Custom exception class to be used by Singly Linked List
    DO NOT CHANGE THIS CLASS IN ANY WAY
    """
    pass


class LinkedList:
    def __init__(self, start_list=None) -> None:
        """
        Initialize new linked list
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        self._head = SLNode(None)

        # populate SLL with initial values (if provided)
        # before using this feature, implement insert_back() method
        if start_list is not None:
            for value in start_list:
                self.insert_back(value)

    def __str__(self) -> str:
        """
        Return content of singly linked list in human-readable form
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        out = 'SLL ['
        node = self._head.next
        while node:
            out += str(node.value)
            if node.next:
                out += ' -> '
            node = node.next
        out += ']'
        return out

    def length(self) -> int:
        """
        Return the length of the linked list
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        length = 0
        node = self._head.next
        while node:
            length += 1
            node = node.next
        return length

    def is_empty(self) -> bool:
        """
        Return True is list is empty, False otherwise
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        return not self._head.next

    # ------------------------------------------------------------------ #

    def insert_front(self, value: object) -> None:
        """
        Insert a new node at the front of the linked list
        """

        #save the reference and then reassign
        new_node = SLNode(value)
        new_node.next = self._head.next
        self._head.next = new_node


    def insert_back(self, value: object) -> None:
        """
        insert a new node at the back of the linked list
        """
        new_node = SLNode(value)

        if self._head is None:
            return new_node

        cur = self._head

        while cur.next:
            cur = cur.next

        cur.next = new_node

    def insert_at_index(self, index: int, value: object) -> None:
        """
        insert a new node at the specified index in the linked list
        """
        cur = self._head

        if index < 0 or index > self.length():
            raise SLLException('Index out of range')

        for i in range(index):
            cur = cur.next
        new_node = SLNode(value)
        new_node.next = cur.next
        cur.next = new_node

    def remove_at_index(self, index: int) -> None:
        """
        Remove the specified node at the specified index
        """
        cur = self._head

        if index < 0 or index > self.length():
            raise SLLException('Index out of range')

        for i in range(index):
            cur = cur.next

        cur.next = cur.next.next


    def remove(self, value: object) -> bool:
        """
        removes the first value in a node that matches the given value
        """
        cur = self._head

        for i in range(self.length()):
            if cur.next.value == value:
                cur.next = cur.next.next
                return True
            cur = cur.next
        return False

    def count(self, value: object) -> int:
        """
        count the number of occurrences of value in a node
        """
        counter = 0
        cur = self._head

        #iterate through values and count the occurrences
        while cur.next:
            cur = cur.next
            if cur.value == value:
                counter += 1
        return counter

    def find(self, value: object) -> bool:
        """
        returns true if value exists in the linked list.
        returns false if not.
        """
        cur = self._head

        if self._head is None:
            return False

        #iterate through valees and validate
        while cur.next:
            if cur.next.value == value:
                return True
            cur = cur.next


    def slice(self, start_index: int, size: int) -> "LinkedList":
        """
        returns a new linked list that is a slice of the original linked list.
        the start index is the start of the slice and the size is the size of the slice.
        """
        if start_index < 0 or size < 0:
            raise SLLException('Index out of range')

        if start_index + size > self.length() or start_index >= self.length():
            raise SLLException('Index out of range')

        cur = self._head

        #move to start index
        for i in range(start_index):
            cur = cur.next


        new_list = LinkedList()


        if size == 0:
            return new_list

        #copy first node
        new_list._head = SLNode(cur.value)
        tail = new_list._head

        #copy the slice you want
        for i in range(size):
            cur = cur.next
            tail.next = SLNode(cur.value)
            tail = tail.next
        return new_list

# ------------------- BASIC TESTING -----------------------------------------


if __name__ == "__main__":

    print("\n# insert_front example 1")
    test_cases = ["A", "B", "C"]
    lst = LinkedList()
    for case in test_cases:
        lst.insert_front(case)
        print(lst)

    print("\n# insert_back example 1")
    test_cases = ["C", "B", "A"]
    lst = LinkedList()
    for case in test_cases:
        lst.insert_back(case)
        print(lst)

    print("\n# insert_at_index example 1")
    lst = LinkedList()
    test_cases = [(0, "A"), (0, "B"), (1, "C"), (3, "D"), (-1, "E"), (5, "F")]
    for index, value in test_cases:
        print("Inserted", value, "at index", index, ": ", end="")
        try:
            lst.insert_at_index(index, value)
            print(lst)
        except Exception as e:
            print(type(e))

    print("\n# remove_at_index example 1")
    lst = LinkedList([1, 2, 3, 4, 5, 6])
    print(f"Initial LinkedList : {lst}")
    for index in [0, 2, 0, 2, 2, -2]:
        print("Removed at index", index, ": ", end="")
        try:
            lst.remove_at_index(index)
            print(lst)
        except Exception as e:
            print(type(e))

    print("\n# remove example 1")
    lst = LinkedList([1, 2, 3, 1, 2, 3, 1, 2, 3])
    print(f"Initial LinkedList, Length: {lst.length()}\n  {lst}")
    for value in [7, 3, 3, 3, 3]:
        print(f"remove({value}): {lst.remove(value)}, Length: {lst.length()}"
              f"\n {lst}")

    print("\n# remove example 2")
    lst = LinkedList([1, 2, 3, 1, 2, 3, 1, 2, 3])
    print(f"Initial LinkedList, Length: {lst.length()}\n  {lst}")
    for value in [1, 2, 3, 1, 2, 3, 3, 2, 1]:
        print(f"remove({value}): {lst.remove(value)}, Length: {lst.length()}"
              f"\n {lst}")

    print("\n# count example 1")
    lst = LinkedList([1, 2, 3, 1, 2, 2])
    print(lst, lst.count(1), lst.count(2), lst.count(3), lst.count(4))

    print("\n# find example 1")
    lst = LinkedList(["Waldo", "Clark Kent", "Homer", "Santa Claus"])
    print(lst)
    print(lst.find("Waldo"))
    print(lst.find("Superman"))
    print(lst.find("Santa Claus"))

    print("\n# slice example 1")
    lst = LinkedList([1, 2, 3, 4, 5, 6, 7, 8, 9])
    ll_slice = lst.slice(1, 3)
    print("Source:", lst)
    print("Start: 1 Size: 3 :", ll_slice)
    ll_slice.remove_at_index(0)
    print("Removed at index 0 :", ll_slice)

    print("\n# slice example 2")
    lst = LinkedList([10, 11, 12, 13, 14, 15, 16])
    print("Source:", lst)
    slices = [(0, 7), (-1, 7), (0, 8), (2, 3), (5, 0), (5, 3), (6, 1)]
    for index, size in slices:
        print("Start:", index, "Size:", size, end="")
        try:
            print(" :", lst.slice(index, size))
        except:
            print(" : exception occurred.")
