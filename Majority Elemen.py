# 可以直接维护一个hash table用来count每个数字出现的次数，然后输出数量最多的那一个，但是时间复杂度和空间复杂度都是O(n)
# 更好的方法是Boyer–Moore投票法，即选定一个候选者，没遇到一个与候选者不一样的则候选者的次数”抵消“一次，一样的加一次，这样只需维护两个变量，空间复杂度为O(1)

class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        candidate = None
        count = 0

        for num in nums:
            # 当前没有候选人，选择 num
            if count == 0:
                candidate = num

            # 相同则增加票数，不同则相互抵消
            if num == candidate:
                count += 1
            else:
                count -= 1

        return candidate
