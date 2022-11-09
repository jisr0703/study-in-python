import sys
from typing import List


# 계단 오르기
def climbStair(n: int) -> int:
    def climb(n, i):
        if n == i:
            return 1
        if n < i:
            return 0
        return climb(n, i + 1) + climb(n, i + 2)
    return climb(n, 0)


# 모든 문자열 치환
def find_permutation_idea1(s1):
    if len(s1) == 1:
        return list(s1)

    ans = []
    curr = s1[0]
    s1 = s1[1:]

    words = find_permutation_idea1(s1)
    for sub in words:
        for i in range(len(sub) + 1):
            ans.append(''.join([sub[:i], curr, sub[i:]]))

    return ans


res2 = []


def find_permutation_idea2(chs, s2, e):
    if s2 == e - 1:
        res2.append("".join(chs))
    else:
        for i in range(s2, e):
            chs[s2], chs[i] = chs[i], chs[s2]
            find_permutation_idea2(chs, s2+1, e)
            chs[s2], chs[i] = chs[i], chs[s2]


# 동전 교환
def coinChange(coins: List[int], value: int) -> int:
    def change(v:int):
        if v == 0:
            return 0
        min_coin_cnt = sys.maxsize
        for c in coins:
            if (v-c) >= 0:
                change_cnt = change(v-c)
                if change_cnt < min_coin_cnt:
                    min_coin_cnt = change_cnt
        return min_coin_cnt + 1
    ans = change(value)
    return ans if ans != sys.maxsize+1 else -1


# 배열의 두 부분 집합의 최소 차이 만들기
min_diff = sys.maxsize
total = 0


def subset_diff(index: int, nums: List[int], subsum: int):
    global total, min_diff
    if index == len(nums):
        min_diff = min(min_diff, abs(((total - subsum) - subsum)))
        return
    subset_diff(index + 1, nums, subsum + nums[index])
    subset_diff(index + 1, nums, subsum)


print(f'계단 오르기 결과 : {climbStair(4)}')

s1 = 'abcd'
res1 = find_permutation_idea1(s1)
print(f'모든 문자열 치환1 결과 : {res1}')
s2 = 'abc'
find_permutation_idea2(list(s2), 0, len(s2))
print(f'모든 문자열 치환2 결과 : {res2}')

print(f'동전 교환 결과 : {coinChange([1, 2, 5], 11)}')

nums = [3, 2, 4, 7, 1]
total = sum(nums)
subset_diff(0, nums, 0)
print(f'배열의 두 부분 집합의 최소 차이 만들기 결과 : {min_diff}')
