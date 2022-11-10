from typing import Any


class Node:
    def __init__(self, val: Any):
        self.val = val
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def push_back(self, val: Any):
        new_node = Node(val)

        if self.head is None:
            self.head = new_node
            return

        last = self.head
        while last.next:
            last = last.next

        last.next = new_node

    def push(self, val: Any):
        new_node = Node(val)

        if self.head is None:
            self.head = new_node
            return

        temp = self.head
        self.head = new_node
        new_node.next = temp

    def remove(self, val: Any):
        curr = self.head
        prev = None

        if curr is not None:
            if curr.val == val:
                self.head = curr.next
                curr = None
                return

        while curr is not None:
            if curr.val == val:
                break
            prev = curr
            curr = curr.next

        if curr is None:
            return

        prev.next = curr.next

        curr = None

    def remove_node(self, node: Node):
        if node is None:
            return

        if node.next is None:
            node = None
            return

        next_node = node.next
        node.val = next_node.val
        node.next = next_node.next

        next_node = None

    def traverse(self):
        temp = self.head

        while temp:
            print(temp.val, end=' ')
            temp = temp.next
        print()


linked_list = LinkedList()
linked_list.push_back(11)
linked_list.push_back(12)
linked_list.push_back(13)

linked_list.push(10)

linked_list.remove(12)

linked_list.traverse()


linked_list2 = LinkedList()
node1 = Node(25)
node2 = Node(150)
node3 = Node(3345)
node4 = Node(5464)
node5 = Node(39785)

node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5

linked_list2.head = node1

linked_list2.remove_node(node3)

linked_list2.traverse()
