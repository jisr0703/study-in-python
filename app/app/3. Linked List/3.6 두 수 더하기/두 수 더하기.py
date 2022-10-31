from typing import Any, List


class Node:
    def __init__(self, val: int, next: Any = None):
        self.val = val
        self.next = next


class LinkedList:
    def __init__(self, head: Any = None):
        self.head = head

    def traverse(self) -> None:
        temp = self.head
        print(f'this link is :', end=' ')
        while temp is not None:
            if temp.next is None:
                print(f'{temp.val}')
                return
            print(f'{temp.val} ', end='-> ')
            temp = temp.next


def addTwoNums_idea1(h1: Node, h2: Node) -> LinkedList:
    def stackStorage(head: Node) -> List:
        temp_list = []
        while head is not None:
            temp_list.append(head)
            head = head.next
        return temp_list

    stack1 = stackStorage(h1)
    stack2 = stackStorage(h2)
    temp_head = None
    carry = 0
    while stack1 or stack2:
        num1 = stack1.pop().val if stack1 else 0
        num2 = stack2.pop().val if stack2 else 0
        sumVal = num1 + num2 + carry
        carry, num = divmod(sumVal, 10)

        node = Node(num)
        if temp_head is None:
            temp_head = node
        else:
            temp = temp_head
            temp_head = node
            node.next = temp

    if carry != 0:
        node = Node(carry)
        temp = temp_head
        temp_head = node
        node.next = temp

    inked_list = LinkedList(temp_head)
    return inked_list


def addTwoNums_idea2(h1: Node, h2: Node) -> LinkedList:
    def listReverse(head: Node) -> None:
        prev = None
        curr = head

        while curr is not None:
            temp_next = curr.next
            curr.next = prev
            prev = curr
            curr = temp_next
        return prev

    r_h1 = listReverse(h1)
    r_h2 = listReverse(h2)

    temp_head = None
    carry = 0
    while r_h1 is not None or r_h2 is not None:
        num1 = 0
        num2 = 0

        if r_h1 is not None:
            num1 = r_h1.val
            r_h1 = r_h1.next
        if r_h2 is not None:
            num2 = r_h2.val
            r_h2 = r_h2.next

        sumVal = num1 + num2 + carry
        carry, num = divmod(sumVal, 10)

        node = Node(num)
        if temp_head is None:
            temp_head = node
        else:
            temp = temp_head
            temp_head = node
            node.next = temp

    if carry != 0:
        node = Node(carry)
        temp = temp_head
        temp_head = node
        node.next = temp

    linked_list = LinkedList(temp_head)
    return linked_list


def addTwoNums_idea3(h1: Node, h2: Node) -> Node:
    def intToString(head: Node) -> str:
        list_temp = []
        while head is not None:
            list_temp.append(str(head.val))
            head = head.next
        return ''.join(list_temp)

    total_res = str(int(intToString(h1)) + int(intToString(h2)))
    head_node = None
    prev_node = None
    for i in range(len(total_res)):
        node = Node(int(total_res[i]))
        if i == 0:
            head_node = node
        if prev_node is not None:
            prev_node.next = node
        prev_node = node

    linked_list = LinkedList(head_node)
    return linked_list


node1 = Node(7)
node2 = Node(2)
node3 = Node(5)
node4 = Node(4)
node1.next = node2
node2.next = node3
node3.next = node4

node5 = Node(2)
node6 = Node(8)
node7 = Node(3)
node8 = Node(3)
node5.next = node6
node6.next = node7
node7.next = node8

nodeA = Node(1)
nodeB = Node(3)
nodeC = Node(2)
nodeA.next = nodeB
nodeB.next = nodeC

nodeD = Node(6)
nodeE = Node(7)
nodeD.next = nodeE

print(f'idea1 - Test Case 1')
idea1_linked_list = addTwoNums_idea1(node1, node5)
idea1_linked_list.traverse()
print(f'idea1 - Test Case 2')
idea1_linked_list = addTwoNums_idea1(nodeA, nodeD)
idea1_linked_list.traverse()
print('--------')
print(f'idea2 - Test Case 1')
idea2_linked_list = addTwoNums_idea2(node1, node5)
idea2_linked_list.traverse()
print(f'idea2 - Test Case 2')
idea2_linked_list = addTwoNums_idea2(nodeA, nodeD)
idea2_linked_list.traverse()
print('--------')
print(f'idea3 - Test Case 1')
idea3_linked_list = addTwoNums_idea3(node4, node8)
idea3_linked_list.traverse()
print(f'idea3 - Test Case 2')
idea3_linked_list = addTwoNums_idea3(nodeC, nodeE)
idea3_linked_list.traverse()





