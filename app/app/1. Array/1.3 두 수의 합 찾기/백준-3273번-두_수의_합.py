import sys
from typing import List

# N: int = int(input())
# NUMS: List[int] = sorted(list(map(int, sys.stdin.readline().split())))
# X: int = int(input())
N = 9
NUMS = sorted([5, 12, 7, 10, 9, 1, 2, 3, 11])
X = 13


def two_sum(n, nums, x):
    l, r = 0, n - 1
    cnt: int = 0
    while l < r:
        sum = nums[l] + nums[r]
        if x == sum:
            cnt += 1
            l += 1
            r -= 1
        elif x > sum:
            l += 1
        else:
            r -= 1
    return cnt


print(two_sum(N, NUMS, X))
