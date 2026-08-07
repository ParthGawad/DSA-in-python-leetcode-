# Solved using Top down approach of Dynamic Programming
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        sum_nums = sum(nums)
        length = len(nums)


        if sum_nums % 2 : return False
        target = sum_nums // 2

        dp = set()
        dp.add(0)
         
        for i in range(length) :
           if nums[i] > target : return False
            
           tempdp = dp.copy()
           for t in dp :
               if (t + nums[i]) == target : return True
               if (t + nums[i]) < target : 
                   tempdp.add(nums[i] + t)
           dp = tempdp
        return False
 # memory complexity : O(n*sums(n))
