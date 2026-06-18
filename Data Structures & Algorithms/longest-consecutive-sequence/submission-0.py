class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        conset = set(nums)
        longest = 0
        for i in nums:
            if i - 1 not in conset:
                p = 1
                q = i
                while q + 1 in conset:
                    p += 1
                    q += 1
                if p > longest:
                    longest = p
        return longest