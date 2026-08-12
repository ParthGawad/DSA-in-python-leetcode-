class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = [[]]
        
        for num in nums:
            # Add 'num' to every subset created so far
            res += [curr + [num] for curr in res]
            
        return res