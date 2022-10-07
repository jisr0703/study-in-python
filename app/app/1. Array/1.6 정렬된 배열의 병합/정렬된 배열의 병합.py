from typing import List

TEST_CASE1: List[List[int]] = [[1, 2, 3], []]
TEST_CASE2: List[List[int]] = [[0, 0, 0], [1, 2, 3]]
TEST_CASE3: List[List[int]] = [[1, 2, 3, 0, 0, 0], [4, 5, 6]]
TEST_CASE4: List[List[int]] = [[4, 5, 6, 0, 0, 0], [1, 2, 3]]


def merge_arr_idea1(nums1: List[int], nums2: List[int]) -> None:
    nums1 += nums2
    nums1[:] = sorted(nums1)
    print(f'merge_arr_idea1.nums1 ===> {nums1}')


print(f'before Test Case 3 ===> {TEST_CASE3}')
merge_arr_idea1(TEST_CASE3[0], TEST_CASE3[1])
print(f'after Test Case 3 ===> {TEST_CASE3}', end="\n\n")


def merge_arr_idea2(nums1: List[int], nums2: List[int]) -> None:
    i, j = len(nums1) - 1, len(nums2) - 1
    for idx in range(j+1):
        nums1.append(0)
    k = len(nums1) - 1

    while i >= 0 and j >= 0:
        if nums1[i] <= nums2[j]:
            nums1[k] = nums2[j]
            j -= 1
        else:
            nums1[k] = nums1[i]
            j -= 1
        k -= 1

    while j > 0:
        nums1[k] = nums2[j]
        k -= 1
        j -= 1

    print(f'merge_arr_idea2.nums1 ===> {nums1}')


print(f'before Test Case 2 ===> {TEST_CASE2}')
merge_arr_idea2(TEST_CASE2[0], TEST_CASE2[1])
print(f'after Test Case 2 ===> {TEST_CASE2}')
