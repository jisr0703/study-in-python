from typing import List


# idea1
def search_insert_idea1(nums: List[int], target: int):
    i = 0

    while i < len(nums):
        if target <= nums[i]:
            break
        i += 1
    return i


def search_insert_idea2(nums: List[int], target: int):
    left, right = 0, len(nums)-1
    while left <= right:
        i = (left + right) // 2
        if target == nums[i]:
            return i
        elif target > nums[i]:
            left = i + 1
        else:
            right = i - 1
    return left


NUMS = [1, 3, 5, 7]
TARGET1 = 0
TARGET2 = 100
TARGET3 = 6

print(search_insert_idea1(NUMS, TARGET3))
print(search_insert_idea2(NUMS, TARGET3))
