from typing import List


class TEST_CASE1:
    NUMS: List[int] = [1, 2, 3, 4, 5]
    RES: List[List[int]] = []
    SUB: List[int] = []
    INDEX: int = 0


class TEST_CASE2:
    NUMS: List[int] = [1, 2, 3]
    RES: List[List[int]] = []
    SUB: List[int] = []
    INDEX: int = 0


def subsets_recursion(nums: List[int], res: List[List[int]], sub: List[int], idx: int) -> None:
    if len(sub) > len(nums):
        return

    res.append(sub[:])

    for i in range(idx, len(nums)):
        sub.append(nums[i])
        subsets_recursion(nums, res, sub, i+1)
        sub.pop()


subsets_recursion(TEST_CASE1.NUMS, TEST_CASE1.RES, TEST_CASE1.SUB, TEST_CASE1.INDEX)
subsets_recursion(TEST_CASE2.NUMS, TEST_CASE2.RES, TEST_CASE2.SUB, TEST_CASE2.INDEX)

print(f'Test Case 1 ===> {TEST_CASE1.RES}')
print(f'Test Case 2 ===> {TEST_CASE2.RES}')
