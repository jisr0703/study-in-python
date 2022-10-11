from typing import Dict, List
import time

NUMS1: List[int] = [8, 2, 5, 2, 2, 2]
NUMS2: List[int] = [1]
NUMS3: List[int] = [8, 2, 5, 2, 2, 2, 10, 10, 10, 10, 10, 10, 10]
NUMS4: List[int] = [5, 6, 8, 7, 7, 8, 7, 7, 7, 9, 4, 1, 7, 7, 7, 7, 7]


def value_search_idea1(nums: List[int]) -> int:
    for i in range(len(nums)):
        val = nums[i]
        cnt = 1
        for j in range(i, len(nums)):
            if val == nums[j]:
                cnt += 1

        if cnt > len(nums) // 2:
            return val
    return -1


def value_search_idea2(nums: List[int]) -> int:
    val_dict: Dict[int: int] = {}

    for num in nums:
        if val_dict.get(num) is not None:
            val_dict[num] += 1
        else:
            val_dict[num] = 1

        if val_dict[num] > (len(nums) // 2):
            return num
    return -1


def value_search_idea3(nums: List[int]) -> int:
    return sorted(nums)[len(nums) // 2]


start = time.time()
print(f'value_search_idea1 result : {value_search_idea1(NUMS1)}')
print(f'{time.time() - start:.10f}', end='\n----------\n')

start = time.time()
print(f'value_search_idea2 result : {value_search_idea2(NUMS4)}')
print(f'{time.time() - start:.10f}', end='\n----------\n')

start = time.time()
print(f'value_search_idea3 result : {value_search_idea3(NUMS3)}')
print(f'{time.time() - start:.10f}', end='\n----------\n')
