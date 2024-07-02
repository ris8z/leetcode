ex = 'https://leetcode.com/problems/time-based-key-value-store/description/'


class TimeMap:

    def __init__(self):
        self.d = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.d:
            self.d[key] = []
        self.d[key].append((value, timestamp))
    
    def get(self, key: str, timestamp: int) -> str:
        #two differen approches, to get the right timestamp or the one just smaller
        def classic(a, q):

        def bisect_right(a, q):





