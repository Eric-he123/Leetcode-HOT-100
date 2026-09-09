# 显然由于不知道什么那个是起点，所以需要设置条件判断起点以及是否要保留起点
# 维护一个集合，只有当该集合中的当前元素-1不在集合中才是一个起点，并以此继续寻找+1，维护一个longest记录最长的序列长度

class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        num_set = set(nums)
        longest = 0

        for num in num_set:
            # 只有序列起点才开始向后搜索
            if num - 1 not in num_set:
                current_num = num
                current_length = 1

                while current_num + 1 in num_set:
                    current_num += 1
                    current_length += 1

                longest = max(longest, current_length)

        return longest
