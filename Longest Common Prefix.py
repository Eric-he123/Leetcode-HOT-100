# 横向对比，先比较第一、二个词，在比较当前的common prefix和第三个词。。。
class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        i = 1
        common = strs[0]

        while i < len(strs):
            id_c = 0
            id_s = 0
            current = ""

            while id_c < len(common) and id_s < len(strs[i]) and common[id_c] == strs[i][id_s]:
                current += common[id_c]
                id_c += 1
                id_s += 1
            i += 1 

            common = current
        
        return common

# 纵向对比，先比较所有词的第一个字符，在比较所有词的第二个字符。。。，相当于以第一个单词作为标准一个一个去比，既然是common prefix那第一个词也应该包含该cp
# 需要注意的是，在这种情况下，如果只有一个词需要 特殊考虑
class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        for i in range(len(strs[0])):
            current_char = strs[0][i]
            
            for word in strs[1:]:
                if i >= len(word) or word[i] != current_char:
                    return strs[0][:i]
            
        return strs[0]
