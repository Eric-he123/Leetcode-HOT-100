# 首先就是要进行排序，这样可以不用考虑每个元素的0号位置的顺序了，每次比较，都只需比较上一序列的结尾和后一序列的起始的大小，需要注意的是，在合并的时候，新序列的结尾不一定
# 是后一序列的结尾，而应该是前一序列的结尾和后一序列结尾的较大者
class Solution:
    def merge(self, intervals: list[list[int]]) -> list[list[int]]:
        intervals.sort(key = lambda x: x[0])
        seq = [intervals[0]]
        for i in range(1, len(intervals)):
            if seq[-1][1] >= intervals[i][0]:
                seq[-1][1] = max(seq[-1][1], intervals[i][1])
            else:
                seq.append(intervals[i])
        return seq
    
m = Solution()
print(m.merge([[4,7],[1,4]]))
