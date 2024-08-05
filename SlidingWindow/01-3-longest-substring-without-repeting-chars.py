def fun(s: str) -> int:
    d = set()
    left = 0
    ans = 0

    for right, value in enumerate(s):
        while value in d:
            d.remove(s[left])
            left += 1
        print(right - left, s[left : right + 1])
        ans = max(right - left + 1, ans)
        d.add(value)
    return ans


fun("abcabcbb")
