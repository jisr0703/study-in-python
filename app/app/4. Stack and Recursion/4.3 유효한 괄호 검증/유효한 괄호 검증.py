TEST_CASE1 = '('
TEST_CASE2 = '}'
TEST_CASE3 = '({<>([])})'
TEST_CASE4 = '(([]))'
TEST_CASE5 = '({<>([)]})'


def isValid(s: str) -> bool:
    stack = []

    pattern = {
        ')': '(',
        '}': '{',
        ']': '[',
        '>': '<',
    }

    for ch in s:
        if ch not in pattern:
            stack.append(ch)
        else:
            pair = stack.pop() if stack else ''

            if pattern[ch] != pair:
                return False

    return len(stack) == 0


print(f'Test Case 1 is {isValid(TEST_CASE1)}')
print(f'Test Case 2 is {isValid(TEST_CASE2)}')
print(f'Test Case 3 is {isValid(TEST_CASE3)}')
print(f'Test Case 4 is {isValid(TEST_CASE4)}')
print(f'Test Case 5 is {isValid(TEST_CASE5)}')
