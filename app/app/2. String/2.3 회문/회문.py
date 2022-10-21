TEST_CASE1_S = 'Abb, cbb a'     #abbcbba
TEST_CASE2_S = ',  , --'        #
TEST_CASE3_S = 'Abbc, cdd a'    #abbccdda

def isPalindrome_idea1(s: str) -> bool:
    i = 0
    j = len(s) - 1

    s = s.lower()

    while i < j:
        while i < j:
            if s[i].isalnum():
                break
            i += 1
        while i < j:
            if s[j].isalnum():
                break
            j -= 1

        if s[i] != s[j]:
            return False

        i += 1
        j -= 1
    return True

def isPalindrome_idea2(s: str) -> bool:
    s = "".join(list(filter(str.isalnum, s))).lower()
    return s == s[::-1]


print(f'idea1 - Test Case 1 ===> {isPalindrome_idea1(TEST_CASE1_S)}')
print(f'idea1 - Test Case 2 ===> {isPalindrome_idea1(TEST_CASE2_S)}')
print(f'idea1 - Test Case 3 ===> {isPalindrome_idea1(TEST_CASE3_S)}')
print('-------------------------------')
print(f'idea2 - Test Case 1 ===> {isPalindrome_idea2(TEST_CASE1_S)}')
print(f'idea2 - Test Case 2 ===> {isPalindrome_idea2(TEST_CASE2_S)}')
print(f'idea2 - Test Case 3 ===> {isPalindrome_idea2(TEST_CASE3_S)}')
