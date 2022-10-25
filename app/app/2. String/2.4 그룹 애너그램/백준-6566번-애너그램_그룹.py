from typing import List
from collections import defaultdict


def input_data() -> List[str]:
    input_list = []
    while True:
        try:
            word = input()
            input_list.append(word)
        except EOFError:
            break
    return input_list


def anagram(strs: List[str]) -> None:
    hashmap = defaultdict(list)
    for i in strs:
        hashmap[''.join(sorted(i))].append(i)

    res = []
    max_len = -1

    for i in hashmap.keys():
        sorted_hashmap = sorted(hashmap[i])
        max_len = max(max_len, len(sorted_hashmap))
        res.append(sorted_hashmap)
    res.sort(key=lambda x: (max_len - len(x), x[0]))

    for i in range(min(len(res), 5)):
        print(f'Group of size {len(res[i])}: {" ".join(sorted(list(set(res[i]))))} .')


anagram(input_data())
