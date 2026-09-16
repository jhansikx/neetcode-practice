class Solution:
    def hasDuplicate(self, nums: list[int]) -> bool:
        uniqueset = set()
        for n in nums:
            if n in uniqueset:
                return True
            uniqueset.add(n)
        return False