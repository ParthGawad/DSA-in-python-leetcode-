class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = [] 
        subset = []
        nums_len = len(nums)

        # backtracking function
        def dfs(i) :
            # base case
            if i >= nums_len :  
                # copying all the values in the subset to the result
                result.append(subset.copy())
                return 
            
            # including values into the subsets that we want to include & perform dfs from on
            subset.append(nums[i])
            dfs(i+1)

            # excluding values from the subsets by popping it that we don't want to include & perform dfs from on
            subset.pop()
            dfs(i+1)

        # start of the backtracking dfs
        dfs(0)
        return result             