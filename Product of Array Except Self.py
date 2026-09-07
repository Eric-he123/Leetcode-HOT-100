# 除了自己以外其他的数字的乘积其实就是自己左边的数的乘积乘上自己右边的数的乘积，所以只需正着走一遍把左边的乘积队列得出，再倒着走一遍把右边的乘积队列得出
# 需要注意的是若数组只有一个数，则返回自己

class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        n = len(nums)
        output = [1] * n

        left_product = 1

        for i in range(n):
            output[i] = left_product
            left_product *= nums[i]

        right_product = 1

        for i in range(n - 1, -1, -1):
            output[i] *= right_product
            right_product *= nums[i]

        return output
