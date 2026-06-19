class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        size = len(nums)
        prefix = [1] * size 
        suffix = [1] * size
        res = [1] * size


        for n in range(1, size):
            prefix[n] = prefix[n-1] * nums[n-1]
        

        for n in range(size -2, -1, -1):
            suffix[n] = suffix[n+1] * nums[n+1]
        

        for n in range(size):
            res[n] = prefix[n] * suffix[n]
        
        return res