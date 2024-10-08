from typing import List

#O(len(start) * len(dna1)) time
#O(len(dna1)) space

def max_days(dna1:str, dna2: str, start:List[int], end:List[int]) -> int:
    #How many days we can modifica dna1
    #while dna2 is still a subsequence of dna1
    if not dna2:
        return 0

    def subsequence(a: str, b: str, marked:List[bool]) -> bool:
        idx:int = 0
        for i,char in enumerate(b):
            if marked[i]:
                continue

            if a[idx] == char:
                idx += 1

            if idx == len(a) - 1:
                return True

        return False
    
    marked = [False] * len(dna1)
    days = 0

    for s,e in zip(start, end):
        for j in range(s, e+1):
            marked[j] = True
        if not subsequence(dna2, dna1, marked):
            break
        days += 1

    return days

dna1 = "abcdefghabc"
dna2 = "abc"
start = [0,0,1,2,9]
end   = [1,2,3,4,10]
print(max_days(dna1, dna2, start, end))
