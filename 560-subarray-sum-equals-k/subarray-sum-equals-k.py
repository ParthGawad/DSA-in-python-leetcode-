from typing import List

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        # 'res' stores the total count of continuous subarrays whose sum equals k.
        # 'currSum' tracks the running cumulative sum of elements as we iterate.
        res, currSum = 0, 0
        
        # 'prefixSum' is a hash map (dictionary) storing the frequencies of cumulative sums:
        # { cumulative_sum: count_of_times_seen }
        # Base case initialization:
        # A prefix sum of 0 has occurred once before reading any elements (an empty prefix).
        # This handles the case where a subarray starting from index 0 itself sums to k
        # (i.e., currSum - k == 0).
        prefixSum = {0 : 1}

        # Iterate through every number in the input array
        for n in nums: 
            # Add current element to the running prefix sum
            currSum += n
            
            # If (currSum - previous_prefix_sum) == k, then the subarray between
            # that previous point and the current index sums exactly to k.
            # Rearranging the formula gives: previous_prefix_sum = currSum - k.
            # 'diff' is the prefix sum we need to find in our history.
            diff = currSum - k

            # If 'diff' exists in prefixSum, it means there are prefixSum[diff] subarrays
            # ending at the current index whose elements sum to k.
            # Add that count to our total result. If not found, add 0.
            res += prefixSum.get(diff, 0)
            
            # Record/update the frequency of the current prefix sum in the hash map
            # so that future iterations can check against it.
            prefixSum[currSum] = 1 + prefixSum.get(currSum, 0)
        
        # Return the total count of valid subarrays found
        return res