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

    def create_bst(self, nodes_list):
        nodes = [None if item is None else Node(item)
                 for item in nodes_list]

        # root node
        self.__root = nodes[0]

        for index in range(1, len(nodes)):
            node = nodes[index]

            if node is not None:
                parent_index = (index - 1) // 2
                parent = nodes[parent_index]
                if parent is None:
                    raise ValueError(
                        f'Missing parent node at index {parent_index},'
                        f' Node({node.data})')
                if index % 2 == True:
                    parent.left = node
                else:
                    parent.right = node

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

        # data??? ???????????? ?????? ??????, parent ??????
        while curr and curr.data != data:
            parent = curr

            if curr.data > data:
                curr = curr.left
            else:
                curr = curr.right

        # data??? ??? ?????? ??????
        if curr is None:
            return node

        # ?????? ????????? ?????? ????????? ??????
        if curr.left is None and curr.right is None:
            if curr != node:
                if parent.left == curr:
                    parent.left = None
                else:
                    parent.right = None
            else:
                node = None

        # ????????? ????????? ?????? ????????? ?????? ??????
        elif curr.left and curr.right:
            # ???????????? ????????? ????????? ?????? ???????????? ?????? ?????? ?????? ??????
            min_node = self.find_min_node(curr.right)
            min_data = min_node.data

            # ????????? ?????? ???????????? ?????? ?????? ?????????
            # ?????? ??????(reaf) ??????????????? ?????? ?????? ??????
            self._delete_data(node, min_data)
            curr.data = min_data

        # ????????? ?????? ?????? ????????? ????????? ?????? ??????
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

    def depth_first_search(self):
        res_iter = self.dfs_iter()
        print(f'dfs iter : {res_iter}')

    def dfs_iter(self):
        if not self.__root:
            return[]

        stack = []
        result = []

        stack.append(self.__root)

        while len(stack) != 0:
            node = stack.pop()

            result.append(node.data)

            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)
        return result

    def depth_first_search_rec(self):
        res_rec = []
        self.dfs_rec(self.__root, res_rec)
        print(f'dfs rec : {res_rec}')

    def dfs_rec(self, node, result):
        if not node:
            return

        result.append(node.data)
        if node.left:
            self.dfs_rec(node.left, result)
        if node.right:
            self.dfs_rec(node.right, result)


print('=====================================')
bst_1 = BinarySearchTree()
bst_1.insert(20)
bst_1.insert(25)
bst_1.insert(14)
bst_1.insert(30)
bst_1.insert(23)
bst_1.insert(18)
bst_1.insert(11)
bst_1.insert(21)
bst_1.insert(15)
print(bst_1.inorder_traverse())
print(f'find 25: {bst_1.find(25)}')
print(f'find 0: {bst_1.find(0)}')
# bst.delete(25)
# bst.delete(18)
bst_1.delete(21)
print(bst_1.inorder_traverse())
print('=====================================')
# 20 25 14 30 23 18 11 21 15
bst_2 = BinarySearchTree()
datas = list(map(int, input().split(' ')))
for num in datas:
    bst_2.insert(num)
print(bst_2.inorder_traverse())
print('=====================================')
# 14 42 35 33 31 19 27 10 N N N N 26 N N
bst_3 = BinarySearchTree()
input_datas = []
for i in input().split(' '):
    if i == 'N':
        input_datas.append(None)
    else:
        input_datas.append(int(i))
bst_3.create_bst(input_datas)
print(bst_3.inorder_traverse())
print('=====================================')
# 20 14 25 11 18 23 30 N N 15 N 21 N N N
bst_4 = BinarySearchTree()
input_datas = []
for i in input().split(' '):
    if i == 'N':
        input_datas.append(None)
    else:
        input_datas.append(int(i))
bst_4.create_bst(input_datas)
bst_4.depth_first_search()
print('=====================================')
# 20 14 25 11 18 23 30 N N 15 N 21 N N N
bst_5 = BinarySearchTree()
input_datas = []
for i in input().split(' '):
    if i == 'N':
        input_datas.append(None)
    else:
        input_datas.append(int(i))
bst_5.create_bst(input_datas)
bst_5.depth_first_search_rec()
