class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        for i, n in enumerate(nums):
            diff = target-n
            if diff in nums[i+1:]:
                j = nums.index(diff, i+1)
                return [i, j]
        
        return []
        
        
        