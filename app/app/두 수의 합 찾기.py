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

NUM: int = 9
NUM_LIST: List[int] = [5, 12, 7, 10, 9, 1, 2, 3, 11, 6]
RESULT: int = 17


def two_sum_baekjoon3273(num: int, num_list: List[int], result: int) -> int:
    list_to_dict: Dict[int, int] = {val: idx for idx, val in enumerate(num_list)}
    check_num: int = 0
    for key, val in enumerate(list_to_dict):
        search_val: int = result - key
        if list_to_dict.get(search_val) is not None and list_to_dict[search_val] != key:
            check_num += 1
    return check_num


print(two_sum_baekjoon3273(NUM, NUM_LIST, RESULT))
