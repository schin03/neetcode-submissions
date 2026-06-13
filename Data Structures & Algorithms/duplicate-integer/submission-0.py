class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        list = {}

        for n in nums:
            if n not in list:
                list[n] = 1
            else:
                return True
        return False
