from typing import Any


class Node:
    def __init__(self, val: int = 0, next: Any = None):
        self.val = val
        self.next = next


# class LinkedList:
#     def __init__(self):
#         self.head = None
#
#     def traverse(self):
#         temp = self.head
#
#         while temp:
#             print(temp.val, end=' ')
#             temp = temp.next
#         print

def hasCycle_idea1(head: Node) -> bool:
    if head is None: return False
    out_cnt = 0
    outer = head
    while outer.next:
        out_cnt += 1
        inner = head
        inner_cnt = 0
        for i in range(out_cnt):
            if inner == outer:
                inner_cnt += 1
            if inner_cnt == 2:
                return True
            inner = inner.next
        outer = outer.next
    return False


def hasCycle_idea2(head: Node) -> bool:
    outer = head
    node_cnt = 0

    while outer is not None and outer.next is not None:
        outer = outer.next
        node_cnt += 1
        visit = node_cnt
        inner = head
        matched = 0
        while visit > 0:
            if outer != inner:
                inner = inner.next
            if outer == inner:
                matched += 1
            if matched == 2:
                return True
            visit -= 1

    return False


def hasCycle_idea3(head: Node) -> bool:
    if head is None:
        return False

    curr = head
    node_set = set()
    while curr is not None:
        if curr in node_set:
            return True
        node_set.add(curr)
        curr = curr.next
    return False


def hasCycle_idea4(head: Node) -> bool:
    slow = head
    fast = head

    while fast is not None and fast.next is not None:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            return True
    return False


node1 = Node(1)
node2 = Node(2)
node3 = Node(3)
node4 = Node(4)
node5 = Node(5)

node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5
node5.next = node1

node6 = Node(6)
node7 = Node(7)
node8 = Node(8)
node9 = Node(9)

node6.next = node7
node7.next = node8
node8.next = node9

node10 = Node(10)
node11 = Node(11)
node12 = Node(12)
node13 = Node(13)
node14 = Node(14)

node10.next = node11
node11.next = node12
node12.next = node13
node13.next = node14
node14.next = node12

node15 = Node(15)

print('IDEA 1')
print(hasCycle_idea1(node1))
print(hasCycle_idea1(node6))
print(hasCycle_idea1(node10))
print(hasCycle_idea1(node15))
print('------------------------')
print('IDEA 2')
print(hasCycle_idea2(node1))
print(hasCycle_idea2(node6))
print(hasCycle_idea2(node10))
print(hasCycle_idea2(node15))
print('------------------------')
print('IDEA 3')
print(hasCycle_idea3(node1))
print(hasCycle_idea3(node6))
print(hasCycle_idea3(node10))
print(hasCycle_idea3(node15))
print('------------------------')
print('IDEA 4')
print(hasCycle_idea4(node1))
print(hasCycle_idea4(node6))
print(hasCycle_idea4(node10))
print(hasCycle_idea4(node15))
print('------------------------')
