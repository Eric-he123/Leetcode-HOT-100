# 数字转字符：f"{num}str"
# 采用双指针，表面上是两个循环但实际上每个数都只检查了一遍，时间复杂度为O(n)

class Solution:
    def summaryRanges(self, nums: list[int]) -> list[str]:
        i = 0
        seq = []

        while i < len(nums):
            start = nums[i]
            j = i

            while j < len(nums) - 1 and nums[j + 1] == nums[j] + 1:
                j += 1

            end = nums[j]

            if start == end:
                seq.append(str(start))
            else:
                seq.append(f"{start}->{end}")

            i = j + 1

        return seq
