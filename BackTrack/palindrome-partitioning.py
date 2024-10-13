from typing import List

def partition(s: str) -> List[List[str]]:

    result: List[List[str]] = []
    buffer: List[str] = []
    
    def isPali(s, start, end):
        while start < end:
            if s[start] != s[end]:
                return False
            start, end = start + 1, end - 1
        return True

    def dfs(start):
        if start >= len(s):
            result.append(buffer.copy())
            return
        
        for end in range(start, len(s)):
            if isPali(s, start, end):
                word = s[start:end+1]
                print(word)
                buffer.append(word)
                dfs(end+1)
                buffer.pop()

    dfs(0)
    return result 




s = "aab"
    
print(partition(s))
