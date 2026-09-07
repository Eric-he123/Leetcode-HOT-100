# 双指针，分别从头尾向中间进行查找，考察的对象是当前柱子能容纳的水的深度，是“逐个柱子”考察
# 当前柱子能接水的深度只取决于该柱子左边最高和右边最高的较小者，min(left_max, right_max)
# 这个方法的迷惑点：例如是left移动了，即上一步处理了left_max，保证了现在处理的柱子的左边的最高是left_max了，但是右边不知道还有没有更高的
# 实则这个担心是多余的，分情况讨论：若现在的right_max已经是包括还没处理的右边的最大的了，那min(left_max, right_max)没有问题
# 若现在的right_max只是以查找的最大，而不是右边整体的最大，那min(left_max, right_max)也只会返回left_max，为什么？
# 因为上一步说了是处理的left_max，那么说明left_max<right_max
# 所以不会出现后续还有更高的right_max而使当前柱子的深度判断错误的情况

class Solution:
    def trap(self, height: list[int]) -> int:
            left = 0
            right = len(height)-1
            left_max = 0
            right_max = 0

            total = 0

            while left <= right:
                left_max = max(height[left], left_max)
                right_max = max(height[right], right_max)

                if left_max <= right_max:
                     total += left_max - height[left]
                     left += 1
                else:
                     total += right_max - height[right]
                     right -= 1
                     
            return total
