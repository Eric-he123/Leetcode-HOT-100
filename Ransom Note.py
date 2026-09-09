# 维护一个字典，首先统计magazine即有什么字母，每个字母又有多少个，组成一个字典，然后遍历查找的字符串ransomNote，如果ransomNote的字母在字典中有出现则个数减一，否则返回False

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        if len(ransomNote) > len(magazine):
            return False

        counter = {}

        # 统计 magazine 中每个字符的数量
        for letter in magazine:
            counter[letter] = counter.get(letter, 0) + 1

        # 使用 magazine 中的字符
        for letter in ransomNote:
            if letter not in counter or counter[letter] == 0:
                return False

            counter[letter] -= 1

        return True
