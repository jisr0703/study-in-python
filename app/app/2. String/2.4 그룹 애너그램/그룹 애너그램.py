from typing import List, DefaultDict, Tuple
from collections import defaultdict

TEST_CASE1 = ['eat', 'repaid', 'paired', 'tea', 'bat']
TEST_CASE2 = ['ab', 'cd', 'ef']
TEST_CASE3 = ['abc', 'bca', 'cba']


def anagram_idea1(strs: List[str]) -> List[List[str]]:
    res = []
    check = []
    for i in range(len(strs)):
        temp_list = [strs[i]]
        if i in check:
            continue
        for j in range(i+1, len(strs)):
            if ''.join(sorted(strs[i])) == ''.join(sorted(strs[j])):
                temp_list.append(strs[j])
                check.append(j)
        res.append(temp_list)
    return res


def anagram_idea2(strs: List[str]) -> List[List[str]]:
    hash_list: DefaultDict[str, List[str]] = defaultdict(list)
    for i in strs:
        hash_list[''.join(sorted(i))].append(i)
    return list(hash_list.values())


def anagram_idea3(strs: List[str]) -> List[List[str]]:
    hash_list: DefaultDict[Tuple, List[str]] = defaultdict(list)
    for i in strs:
        count = [0] * 26
        for j in i:
            count[ord(j)-ord('a')] += 1
        hash_list[tuple(count)].append(i)
    return list(hash_list.values())


print(anagram_idea1(TEST_CASE1))
print(anagram_idea2(TEST_CASE2))
print(anagram_idea3(TEST_CASE3))
