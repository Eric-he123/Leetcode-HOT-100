# 双指针，分别从两个字符串的首位开始查找，本题较为简单，时间复杂度为O(n+m)

class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        in_s = 0
        in_t = 0
        while in_s < len(s) and in_t < len(t):
            if s[in_s] == t[in_t]:
                in_s += 1
                in_t += 1
            else:
                in_t += 1
        
        if in_s == len(s):
            return "ture"
        else:
            return "false"
