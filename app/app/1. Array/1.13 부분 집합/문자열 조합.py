from typing import List


class TEST_CASE1:
    STRS: List[str] = [["abc", "def"], ["123", "456", "789"], ["aa", "bb"]]
    RES: List[List[str]] = []
    SUB: List[str] = []
    TEMP_STR: str = ''
    INDEX: int = 0

class TEST_CASE1:
    STRS: List[str] = [["aaa", "bbb", "ccc", "ddd"], ["123", "456", "789", "147", "258", "369"], ["aa", "bb", "cc"]]
    RES: List[List[str]] = []
    SUB: List[str] = []
    TEMP_STR: str = ''
    INDEX: int = 0


def str_recursion(strs: List[List[str]], res: List[str] = [], sub: List[str] = [], temp: str = '', idx: int = 0) -> None:
    sub.append(temp)
    for i in range(idx, len(strs)):
        for j in range(len(strs[i])):
            str_recursion(strs, res, sub, strs[i][j], i + 1)
            if i == len(strs) - 1:
                res.append(''.join(sub[:]))
                sub.pop()
                if j == len(strs[len(strs) - 1]) - 1:
                    sub.pop()
                    return
            if j == len(strs[i]) - 1:
                sub.pop()
                return


str_recursion(TEST_CASE1.STRS, TEST_CASE1.RES, TEST_CASE1.SUB, TEST_CASE1.TEMP_STR, TEST_CASE1.INDEX)
print(f'Test Case 1 ===> {TEST_CASE1.RES}')
