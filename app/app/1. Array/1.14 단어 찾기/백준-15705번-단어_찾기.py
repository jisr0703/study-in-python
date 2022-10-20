from typing import List, Optional


# def find_word(word, n, m, board):
def find_word() -> int:
    word, n, m, board = input_word_and_board()

    direction = [[-1, 0], [-1, 1], [0, 1], [1, 1], [1, 0], [1, -1], [0, -1], [-1, -1]]

    def find_next_alphabet(x: int, y: int, subword: str, fix: Optional[List[int]] = None):

        if (x < 0 or x >= len(board)) or (y < 0 or y >= len(board)):
            return False

        if board[x][y] != subword[0]:
            return False

        if len(subword) == 1:
            return True

        if fix is None:
            for a, b in direction:
                if find_next_alphabet(x+a, y+b, subword[1:], [a, b]):
                    return True
        else:
            if find_next_alphabet(x+fix[0], y+fix[1], subword[1:], fix):
                return True

        return False

    for i in range(n):
        for j in range(m):
            if board[i][j] == word[0]:
                if find_next_alphabet(i, j, word):
                    return 1

    return 0


def input_word_and_board():
    s = input()
    n, m = map(int,input().split(' '))
    b: List[List[str]] = []
    for i in range(n):
        b.append(list(input()))

    return s, n, m, b


print(find_word())

# class TEST_CASE1:
#     s = 'ABCD'
#     n = 5
#     m = 5
#     board = [
#         ['A','C','D','B','E'],
#         ['A','B','C','E','D'],
#         ['A','C','C','E','E'],
#         ['A','C','H','D','F'],
#         ['A','C','B','C','E']
#     ]
#
#
# class TEST_CASE2:
#     s = 'STR'
#     n = 6
#     m = 6
#     board = [
#         ['S', 'T', 'A', 'R', 'T', 'S'],
#         ['S', 'T', 'R', 'S', 'T', 'R'],
#         ['R', 'R', 'T', 'S', 'R', 'E'],
#         ['S', 'R', 'S', 'T', 'R', 'R'],
#         ['S', 'T', 'R', 'T', 'S', 'R'],
#         ['S', 'T', 'S', 'T', 'S', 'S']
#     ]
#
#
# class TEST_CASE3:
#     s = 'AFAFK'
#     n = 2
#     m = 2
#     board = [
#         ['A', 'B'],
#         ['C', 'D']
#      ]
#
#
# class TEST_CASE4:
#     s = 'AAAB'
#     n = 4
#     m = 4
#     board = [
#         ['A', 'A', 'A', 'A'],
#         ['A', 'B', 'B', 'A'],
#         ['A', 'B', 'B', 'A'],
#         ['A', 'A', 'A', 'A']
#     ]
#
#
# print(find_word(TEST_CASE1.s,TEST_CASE1.n,TEST_CASE1.m,TEST_CASE1.board))
# print(find_word(TEST_CASE2.s,TEST_CASE2.n,TEST_CASE2.m,TEST_CASE2.board))
# print(find_word(TEST_CASE3.s,TEST_CASE3.n,TEST_CASE3.m,TEST_CASE3.board))
# print(find_word(TEST_CASE4.s,TEST_CASE4.n,TEST_CASE4.m,TEST_CASE4.board))
