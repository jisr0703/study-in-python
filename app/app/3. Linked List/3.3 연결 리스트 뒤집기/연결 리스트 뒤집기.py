from typing import Any


class Node:
    def __init__(self, val: int = 0, next: Any = None):
        self.val = val
        self.next = next


class ListNode:
    def __init__(self):
        self.head = None

    def headSet(self, node: Node):
        self.head = node

    def traverse(self):
        temp = self.head

        while temp:
            print(temp.val, end=' ')
            temp = temp.next
        print()


def reverseList_idea1(head: Node, linked: ListNode) -> Node:
    prev = None
    curr = head

    while curr is not None:
        next_temp = curr.next
        curr.next = prev
        prev = curr
        curr = next_temp

    linked.headSet(prev)
    return prev


def reverseList_idea2(head: Node, linked: ListNode) -> Node:
    if head is None:
        return None

    stack = []
    curr = head
    while curr.next is not None:
        stack.append(curr)
        curr = curr.next

    temp_head = curr

    while stack:
        curr.next = stack.pop()
        curr = curr.next
    curr.next = None

    linked.headSet(temp_head)
    return temp_head


def reverseList_idea3(head: Node, linked: ListNode = None) -> Node:
    if head is None or head.next is None:
        return head

    reverse_list = reverseList_idea3(head.next)
    head.next.next = head
    head.next = None

    if linked is not None:
        linked.headSet(reverse_list)

    return reverse_list


print('IDEA 1')
list_node_idea1 = ListNode()

node1 = Node(1)
node2 = Node(2)
node3 = Node(3)
node4 = Node(4)

node1.next = node2
node2.next = node3
node3.next = node4

list_node_idea1.headSet(node1)
print(f'based linked : ', end='')
list_node_idea1.traverse()

reverseList_idea1(node1, list_node_idea1)
print(f'reverse linked : ', end='')
list_node_idea1.traverse()
print('------------------------')
print('IDEA 2')
list_node_idea2 = ListNode()

node5 = Node(12)
node6 = Node(323)
node7 = Node(548)
node8 = Node(997)

node5.next = node6
node6.next = node7
node7.next = node8

list_node_idea2.headSet(node5)
print(f'based linked : ', end='')
list_node_idea2.traverse()

reverseList_idea2(node1, list_node_idea2)
print(f'reverse linked : ', end='')
list_node_idea2.traverse()
print('------------------------')
print('IDEA 3')
list_node_idea3 = ListNode()

node9 = Node(10)
node10 = Node(20)
node11 = Node(30)
node12 = Node(40)

node9.next = node10
node10.next = node11
node11.next = node12

list_node_idea3.headSet(node1)
print(f'based linked : ', end='')
list_node_idea3.traverse()

reverseList_idea3(node1, list_node_idea3)
print(f'reverse linked : ', end='')
list_node_idea3.traverse()
print('------------------------')
