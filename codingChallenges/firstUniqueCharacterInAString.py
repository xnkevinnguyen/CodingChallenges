class Solution:
    def firstUniqChar(self, s: str) -> int:
        dict = {}
        index = 0
        for char in s:
            if char in dict:
                dict[char] = -1
            else:
                dict[char] = index
                index = index + 1

        minIndex = 99999999
        for key, value in dict.items():
            if value < minIndex:
                minIndex = value
            print(key)
            print(value)


s = Solution()
s.firstUniqChar("leetcode")
