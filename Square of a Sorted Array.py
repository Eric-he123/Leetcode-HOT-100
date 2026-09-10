# 可以先平方再排序，但这样的话时间复杂度是O(nlogn)，可以用双指针，由于原序列是已经排好序的，所以最大的只可能出现在两头，题目要求输出一个从小到大的序列，
# 那就在执行的时候先从后往前排result

class Solution:
    def sortedSquares(self, nums: list[int]) -> list[int]:
        n = len(nums)
        result = [0] * n
        pos = n - 1
        left = 0
        right = n - 1

        while left <= right:
            left_square = nums[left] ** 2
            right_square = nums[right] ** 2
            if left_square > right_square:
                result[pos] = left_square
                left += 1
                pos -= 1

            else: 
                result[pos] = right_square
                right -= 1
                pos -= 1
        return result

m = Solution()
print(m.sortedSquares([-7,-3,2,3,11]))
