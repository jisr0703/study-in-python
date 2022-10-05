from typing import List, Dict

NUMS: List[int] = [2, 7, 8, 11]
TARGET: int = 13


def two_sum_idea1(nums: List[int], target: int) -> List[int]:
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if target is nums[i] + nums[j]:
                return [i, j]
    return [-1, -1]


def two_sum_idea2(nums: List[int], target: int) -> List[int]:
    hashtable_dict: Dict[int, int] = {}

    for i in range(len(nums)):
        value: int = target - nums[i]
        if hashtable_dict.get(value) is not None and hashtable_dict[value] != i:
            return sorted([i, hashtable_dict[value]])
        hashtable_dict[nums[i]] = i

    return [-1, -1]


print(two_sum_idea1(NUMS, TARGET))
print(two_sum_idea2(NUMS, TARGET))