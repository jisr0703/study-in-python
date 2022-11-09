class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

    def __repr__(self):
        return str(self.data)


class BinarySearchTree:
    def __init__(self):
        self.__root = None

    def insert(self, data, method='iterative'):
        if method in 'recursion':
            self.__root = self._insert_rec(self.__root, data)
        else:
            self._insert_iter(data)

    def _insert_rec(self, node, data):
        if not node:
            node = Node(data)
        else:
            if node.data > data:
                node.left = self._insert_rec(node.left, data)
            else:
                node.right = self._insert_rec(node.right, data)

        return node

    def _insert_iter(self, data):
        # root is None
        if not self.__root:
            self.__root = Node(data)
            return
        # create new node
        new_node = Node(data)

        curr = self.__root
        parent = None

        while curr is not None:
            parent = curr
            if curr.data > data:
                curr = curr.left
            else:
                curr = curr.right

        if parent.data > data:
            parent.left = new_node
        else:
            parent.right = new_node

    def inorder_traverse(self):
        result = []
        self._inorder_rec(self.__root, result)
        return result

    def _inorder_rec(self, node, result):
        if not node:
            return

        self._inorder_rec(node.left, result)
        result.append(node.data)
        self._inorder_rec(node.right, result)

    def inorder_iter(self):
        result = []
        stack = []
        node = self.__root

        while node or stack:
            while node:
                stack.append(node)
                node = node.left
            if stack:
                node = stack.pop()
                result.append(node)
                node = node.right
        return result

    def find(self, data):
        return self._find_data(self.__root, data)

    def _find_data(self, node, data):
        if node is None:
            return False
        elif node.data == data:
            return True
        elif node.data > data:
            return self._find_data(node.left, data)
        else:
            return self._find_data(node.right, data)

    def find_min_node(self, node):
        while node.left:
            node = node.left
        return node

    def delete(self, data):
        self._delete_data(self.__root, data)

    def _delete_data(self, node, data):
        parent = None
        curr = node

        # data에 해당하는 노드 찾기, parent 추적
        while curr and curr.data != data:
            parent = curr

            if curr.data > data:
                curr = curr.left
            else:
                curr = curr.right

        # data를 못 찾는 경우
        if curr is None:
            return node

        # 자식 노드가 없는 노드의 삭제
        if curr.left is None and curr.right is None:
            if curr != node:
                if parent.left == curr:
                    parent.left = None
                else:
                    parent.right = None
            else:
                node = None

        # 오른쪽 왼쪽에 모든 자식이 있는 경우
        elif curr.left and curr.right:
            # 지우려는 노드의 오른쪽 하위 트리에서 가장 작은 노드 찾기
            min_node = self.find_min_node(curr.right)
            min_data = min_node.data

            # 오른쪽 하위 트리에서 가장 작은 노드는
            # 항상 잎새(reaf) 노드이므로 그냥 삭제 진행
            self._delete_data(node, min_data)
            curr.data = min_data

        # 오른쪽 혹은 왼쪽 노드가 하나만 있는 경우
        else:
            if curr.left:
                child = curr.left
            else:
                child = curr.right

            if curr != node:
                if curr == parent.left:
                    parent.left = child
                else:
                    parent.right = child
            else:
                node = child
        return node


bst = BinarySearchTree()
bst.insert(20)
bst.insert(25)
bst.insert(14)
bst.insert(30)
bst.insert(23)
bst.insert(18)
bst.insert(11)
bst.insert(21)
bst.insert(15)
print(bst.inorder_traverse())
print(f'find 25: {bst.find(25)}')
print(f'find 0: {bst.find(0)}')
# bst.delete(25)
# bst.delete(18)
bst.delete(21)
print(bst.inorder_traverse())

