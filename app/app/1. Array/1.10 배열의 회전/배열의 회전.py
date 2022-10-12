from typing import List


NUMS1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
K1 = 2
NUMS2 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
K2 = 3
NUMS3 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
K3 = 4
NUMS4 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
K4 = 5
NUMS5 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
K5 = 6


def rotate_idea1(nums: List[int], k: int) -> None:
    temp = [0] * len(nums)
    temp[k:] = nums[:len(nums) - k]
    temp[:k] = nums[len(nums) - k:]
    nums[:] = temp


rotate_idea1(NUMS1, K1)
print(f'idea1 ===> {NUMS1}')


def rotate_idea2(nums: List[int], k: int) -> None:
    for i in range(k):
        prev = nums[len(nums) - 1]
        for j in range(len(nums)):
            temp = nums[j]
            nums[j] = prev
            prev = temp


rotate_idea2(NUMS2, K2)
print(f'idea2 ===> {NUMS2}')


def rotate_idea3(nums: List[int], k: int) -> None:
    temp = [0] * len(nums)
    for i in range(len(nums)):
        temp[(i+k) % len(nums)] = nums[i]
    nums[:] = temp


rotate_idea3(NUMS3, K3)
print(f'idea3 ===> {NUMS3}')


def rotate_idea4(nums: List[int], k: int) -> None:
    k = k % len(nums)
    nums[:] = nums[::-1]
    nums[:k] = nums[:k][::-1]
    nums[k:] = nums[k:][::-1]


rotate_idea4(NUMS4, K4)
print(f'idea4 ===> {NUMS4}')


def rotate_idea5(nums: List[int], k: int) -> None:
    cnt = 0
    for i in range(len(nums)):
        if cnt >= len(nums):
            break

        curr_idx = i
        prev_elem = nums[i]

        while True:
            next_idx = (curr_idx + k) % len(nums)
            temp = nums[next_idx]
            nums[next_idx] = prev_elem
            prev_elem = temp
            curr_idx = next_idx
            cnt += 1

            if i == curr_idx:
                break


rotate_idea1(NUMS5, K5)
print(f'idea5 ===> {NUMS5}')
