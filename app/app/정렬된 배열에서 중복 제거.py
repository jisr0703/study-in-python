from typing import List

CASE1: List[int] = []
CASE2: List[int] = [1, 2, 3, 4]
CASE3: List[int] = [0, 0, 1, 1, 1, 2]


def remove_duplicates(nums: List[int]) -> int:
    if len(nums) == 0:
        return 0

    cnt: int = 1
    val: int = nums[0]

    for i in range(1, len(nums)):
        if val != nums[i]:
            val = nums[i]
            nums[cnt] = val
            cnt += 1

    return cnt


print(remove_duplicates(CASE1))
print(remove_duplicates(CASE2))
print(remove_duplicates(CASE3))
