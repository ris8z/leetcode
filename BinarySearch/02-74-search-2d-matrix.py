ex = 'https://leetcode.com/problems/search-a-2d-matrix/description/'

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        #jsut pretend that the while matrix is just an array of n_row * n_col element
        #and get the element form the index with mat[index // n_col][index % n_col]
        #c style matrix, then is just an easy bisi bs
        def fun1(mat, q):
            n_row, n_col = len(mat), len(mat[0])
            left, right = 0, n_row * n_col - 1

            while left <= right:
                mid = left + (right - left) // 2
                guess = mat[mid // n_col][mid % n_col]

                if guess == q:
                    return True
                
                if guess < q:
                    left = mid + 1
                else:
                    right = mid - 1
            return False
        #return fun1(matrix, target)
        
        

        #we first search for the row that can contains our query
        #than we just run bs on that row that is a valid normal array
        def fun2(mat, q):
            n_row, n_col = len(mat), len(mat[0])

            #first search for the right row
            left, right = 0, n_row - 1
            row = None

            while left <= right:
                mid = (left + right) // 2

                if mat[mid][0] <= q and q <= mat[mid][-1]:
                    row = mid
                    break

                if q > mat[mid][-1]:
                    left = mid + 1
                else:
                    right = mid - 1

            if row == None:
                return False

            #now is just a normal bs on the mat[row]
            a = mat[row]
            left, right = 0, len(a) - 1
            while left <= right:
                mid = (left + right) // 2

                if a[mid] == q:
                    return True

                if q > a[mid]:
                    left = mid + 1
                else:
                    right = mid - 1

            return False
        return fun2(matrix, target)



