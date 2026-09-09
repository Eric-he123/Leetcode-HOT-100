# 由于set会自动去重，所以只需考察集合的长度和数列的长度是否一致即可

class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        return len(nums) != len(set(nums))
