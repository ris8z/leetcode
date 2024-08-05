


def fun(s: str, k: int) -> int:
    cnt = [0] * 26 #0 -> A, 1 -> B etc ... 
    
    left, right = 0, 0
    ans = 0

    while right < len(s):
        while right < len(s):
            cnt[ord(s[right]) - ord('A')] += 1
            if not (right - left + 1 - max(cnt)) <= k:
                break
            print(right - left + 1, s[left: right+1], cnt)
            ans = max(ans, right - left + 1)
            right += 1

        cnt[ord(s[left]) - ord('A')] -= 1
        left += 1
        right += 1
    
    return ans
def fun2(s:str, k:int) -> int:
    cnt = [0] * 26

    left, right = 0, 0
    ans = 0
    while right < len(s):
        cnt[ord(s[right]) - ord('A')] += 1
        
        if right - left + 1 - max(cnt) <= k:
            print(right - left + 1, s[left: right+1], cnt)
            ans = max(ans, right - left + 1)
        else:
            cnt[ord(s[left]) - ord('A')] -= 1
            left += 1
        
        right += 1
    return ans

#fun("ABAB", 2)
#fun2("ABAB", 2)
fun("AABABBA", 1)
fun2("AABABBA", 1)
