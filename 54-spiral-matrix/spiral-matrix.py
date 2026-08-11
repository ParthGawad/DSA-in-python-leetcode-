class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        res = [] # result array
        
        # left & top pointer points at the 0th index i.e at the starting of the matrix
        left,top = 0,0 

        # right pointer points at the rightmost side of the matrix at index 2th (length = 3) i.e. at the end of the 1st sub-array in the matrix
        right = len(matrix[0]) 
        # bottom pointer points at the bottom side of the matrix i.e. at the final index of the last sub-array in the matrix
        bottom = len(matrix) 

        # This loop runs until pointers don't overlap onto each other 
        while left < right and top < bottom : 

            # gets every i element in the top row
            for i in range(left,right) :
                res.append(matrix[top][i])
            top += 1

            # gets every i element in the rightmost row
            for i in range(top,bottom) :
                res.append(matrix[i][right-1])
            right -= 1

            # checks if pointers are overlapped or not
            if not (left < right and top < bottom) : break

            # gets every i element in the bottommost row
            for i in range(right-1, left-1, -1) :
                res.append(matrix[bottom-1][i])
            bottom -= 1

            # gets every i element in the leftmost row
            for i in range(bottom-1,top-1, -1) :
                res.append(matrix[i][left])
            left += 1

        return res
# O(n*m) : time complexity & O(1) : space complexity