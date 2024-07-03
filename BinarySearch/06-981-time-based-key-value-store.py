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
            #fastest approach just a classic with the change of var result in the while loop
            #we are searching for something that is smaller or equal to q

            left, right = 0, len(a) - 1
            ans = ""
            while left <= right:
                mid = (left + right) // 2

                val, tim = a[mid]
                if tim <= q:
                    ans = val
                    left = mid + 1
                else:
                    right = mid - 1
            
            return ans


        def bisect_right(a, q):
            #return the right most target
            #is there is no target return the biggest number that is smaller the target
            if a == []:
                return ""

            left,right = 0,len(a) - 1
            while left < right:
                mid = math.ceil(float(left + right) / 2)
                val, tim = a[mid]

                if tim > q:
                    right = mid - 1
                else:
                    left = mid
            val, tim = a[left]

            if tim <= q:
                return val
            return ""

        a = self.d.get(key, [])
        q = timestamp

        #return classic(a, q)
        return bisect_right(a, q)
