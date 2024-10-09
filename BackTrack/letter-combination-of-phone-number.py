from typing import List, Dict

#mine O(4 ^ n)
def letterCombinations(digits: str) -> List[str]:
    d: Dict[str, List[str]] = {str(i):[] for i in range(2,10)}

    cnt: int = 2
    for i in range(26):
        if len(d[str(cnt)]) == 3 and cnt != 7 and cnt != 9:
            cnt += 1
        elif len(d[str(cnt)]) == 4:
            cnt += 1

        val: str = chr(ord('a') + i)
        d[str(cnt)].append(val)

    K: int = len(digits)
    result: List[str] = []
    buffer: List[str] = []

    def dfs(i: int) -> None:
        if len(buffer) == K:
            result.append("".join(buffer))
            return

        letters = d[digits[i]]
        for letter in letters:
            buffer.append(letter)
            dfs(i + 1)
            buffer.pop()
    dfs(0)
    return result 

#neet code one some login less verobse
def letterCombinationsNeet(digits: str) -> List[str]:
    res = []
    digitToChar = {
        "2": "abc",
        "3": "def",
        "4": "ghi",
        "5": "jkl",
        "6": "mno",
        "7": "qprs",
        "8": "tuv",
        "9": "wxyz",
    }

    def backtrack(i, curStr):
        if len(curStr) == len(digits):
            res.append(curStr)
            return
        for c in digitToChar[digits[i]]:
            backtrack(i + 1, curStr + c)

    if digits:
        backtrack(0, "")

    return res




digits = "23"
Output = ["ad","ae","af","bd","be","bf","cd","ce","cf"]
print(letterCombinations(digits))
