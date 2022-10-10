from typing import List
import time


def pascal_pyramid_idea1(num: int) -> List[List[int]]:
    start = time.time()

    pyramid: List[List[int]] = []

    if num <= 0:
        print(f'idea1 실행 시간 : {time.time() - start:.10f}')
        return pyramid

    for i in range(num):
        pyramid.append([])
        for j in range(i + 1):
            pyramid[i].append(0)

    for i in range(len(pyramid)):
        pyramid[i][0] = 1
        if i == 0: continue
        pyramid[i][len(pyramid[i]) - 1] = 1
        for j in range(1, len(pyramid[i]) - 1):
            pyramid[i][j] = pyramid[i - 1][j - 1] + pyramid[i - 1][j]

    print(f'idea1 실행 시간 : {time.time() - start:.10f}')
    return pyramid


def pascal_pyramid_idea2(num: int) -> List[List[int]]:
    start = time.time()
    pyramid = []

    if num <= 0:
        print(f'idea2 실행 시간 : {time.time() - start:.10f}')
        return pyramid

    pyramid.append([1])
    for i in range(1, num):
        prev_len: int = len(pyramid[i-1])
        curr_list: List[int] = []
        for j in range(prev_len + 1):
            num = 1
            if j != 0 and j != prev_len:
                num = pyramid[i-1][j-1] + pyramid[i-1][j]
            curr_list.append(num)
        pyramid.append(curr_list)
    print(f'idea2 실행 시간 : {time.time() - start:.10f}')
    return pyramid


# print(pascal_pyramid_idea1(1000))
# print(pascal_pyramid_idea2(1000))
# print(pascal_pyramid_idea1(100))
# print(pascal_pyramid_idea2(100))
# print(pascal_pyramid_idea1(10))
# print(pascal_pyramid_idea2(10))

pascal_pyramid_idea1(1000)
pascal_pyramid_idea2(1000)
pascal_pyramid_idea1(100)
pascal_pyramid_idea2(100)
pascal_pyramid_idea1(10)
pascal_pyramid_idea2(10)