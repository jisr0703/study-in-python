from typing import List


NUMS1 = [3, 1, 0, 4]
NUMS2 = [3, 1, 0, 4]
NUMS3 = [3, 1, 0, 4]
NUMS4 = [3, 1, 0, 4]
NUMS5 = [3, 1, 0, 4]


def missing_num1(nums: List[int]) -> int:
    nums.sort()

    for i in range(len(nums) + 1):
        if i != nums[i]:
            return i

    return -1


def missing_num_idea2(nums: List[int]) -> int:
    nums_set = set(nums)

    for i in range(len(nums) + 1):
        if i not in nums_set:
            return i

    return -1


def missing_num_idea3(nums: List[int]) -> int:
    max_num = len(nums)

    for i in range(len(nums)):
        max_num ^= (i ^ nums[i])

    return max_num


def missing_nums_idea4(nums: List[int]) -> int:
    expected_sum = 0
    nums_sum = 0

    for i in range(len(nums) + 1):
        expected_sum += i

    for _, num in enumerate(nums):
        nums_sum += num

    return expected_sum - nums_sum


def missing_num_idea5(nums: List[int]) -> int:
    return int((len(nums) * len(nums) + 1) / 2) - sum(nums)


print(f'idea1 num ===> {missing_num1(NUMS1)}')
print(f'idea2 num ===> {missing_num1(NUMS2)}')
print(f'idea3 num ===> {missing_num1(NUMS3)}')
print(f'idea4 num ===> {missing_num1(NUMS4)}')
print(f'idea5 num ===> {missing_num1(NUMS5)}')
