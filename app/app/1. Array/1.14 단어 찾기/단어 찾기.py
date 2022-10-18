from typing import List


class TEST_CASE1:
    BOARD: List[List[str]] = [
        ["A", "B", "C", "E"],
        ["S", "F", "E", "S"],
        ["A", "D", "E", "E"]
    ]
    WORD: str = 'CEEE'


class TEST_CASE2:
    BOARD: List[List[str]] = [
        ["A", "B", "C", "E"],
        ["S", "F", "E", "S"],
        ["A", "D", "E", "E"]
    ]
    WORD: str = 'FECA'


class TEST_CASE3:
    BOARD: List[List[str]] = [
        ["A", "B", "C", "E"],
        ["S", "F", "E", "S"],
        ["A", "D", "E", "E"]
    ]
    WORD: str = 'DFES'


class TEST_CASE4:
    BOARD: List[List[str]] = [
        ["A", "B", "C", "E"],
        ["S", "F", "E", "S"],
        ["A", "D", "E", "E"]
    ]
    WORD: str = 'ZZZZ'



def word_search(board: List[List[str]], word: str) -> bool:
    direction: List[str] = [[-1, 0], [0, -1], [1, 0], [0, 1]]

    def direction_search(x: int, y: int, str_temp: str) -> bool:
        if (x < 0 or x >= len(board)) or (y < 0 or y >= len(board[0])):
            return False

        if board[x][y] != str_temp[0]:
            return False

        if len(str_temp) <= 1:
            return True

        board[x][y] = '.'

        for a, b in direction:
            if direction_search(x+a, y+b, str_temp[1:]):
                return True

        board[x][y] = str_temp[0]
        return False

    result = False
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == word[0] and direction_search(i, j, word):
                result = True
                break
    return result


print(f'Test Case 1 ===> {word_search(TEST_CASE1.BOARD, TEST_CASE1.WORD)}')
print(f'Test Case 2 ===> {word_search(TEST_CASE2.BOARD, TEST_CASE2.WORD)}')
print(f'Test Case 3 ===> {word_search(TEST_CASE3.BOARD, TEST_CASE3.WORD)}')
print(f'Test Case 4 ===> {word_search(TEST_CASE4.BOARD, TEST_CASE4.WORD)}')
