from typing import List

TEST_CASE1: List[List[int]] = [[1, 3, 5, 7], [2, 4, 8]]
TEST_CASE2: List[List[int]] = [[10], [2, 3]]
TEST_CASE3: List[List[int]] = [[2, 8, 10], [5]]


def merge_arr_idea1(nums1: List[int], nums2: List[int]) -> None:
    for i, v1 in enumerate(nums1):
        if v1 > nums2[0]:
            nums1[i] = nums2[0]
            nums2[0] = v1

            for j, v2 in enumerate(nums2[1:], start=1):
                if v1 <= v2:
                    nums2[j-1] = v1
                    break

                nums2[j-1] = nums2[j]

    print(f'merge_arr_idea1 nums1 ===> {nums1}')
    print(f'merge_arr_idea1 nums2 ===> {nums2}')


def merge_arr_idea2(nums1: List[int], nums2: List[int]) -> None:
    for i, v1 in enumerate(nums1):
        if v1 > nums2[0]:
            nums1[i] = nums2[0]
            nums2[0] = v1
        nums2[:] = sorted(nums2)

    print(f'merge_arr_idea2 nums1 ===> {nums1}')
    print(f'merge_arr_idea2 nums2 ===> {nums2}')


print(f'Before TEST_CASE3 ===> {TEST_CASE3}')
merge_arr_idea1(TEST_CASE3[0], TEST_CASE3[1])
print(f'After TEST_CASE3 ===> {TEST_CASE3}')
print('*-------------------------------------*')
print(f'Before TEST_CASE1 ===> {TEST_CASE1}')
merge_arr_idea2(TEST_CASE1[0], TEST_CASE1[1])
print(f'After TEST_CASE1 ===> {TEST_CASE1}')
print('*-------------------------------------*')
