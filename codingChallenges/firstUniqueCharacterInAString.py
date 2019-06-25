import collections
import string
import time


class Solution:
    def firstUniqChar(self, s: str) -> int:
        if len(s) == 0:
            return -1
        if len(s) == 1:
            return 0

        # count how often char appears
        dict = {}
        for char in s:
            if char in dict:
                dict[char] = dict[char] + 1
            else:
                dict[char] = 1

        # find index of char
        for key, value in dict.items():
            if value == 1:
                for idx, value in enumerate(s):
                    if value == key:
                        return idx

        return -1


class Solution2:
    def firstUniqChar(self, s: str) -> int:
        if len(s) == 0:
            return -1
        if len(s) == 1:
            return 0

        # count how often char appears
        count = collections.Counter(s)

        # find index of char
        index = 0
        for ch in s:
            if count[ch] == 1:
                return index
            index += 1

        return -1


class Solution3:
    def firstUniqChar(self, s: str) -> int:
        if len(s) == 0:
            return -1
        if len(s) == 1:
            return 0

        minIndex = len(s)
        for ch in string.ascii_lowercase:
            l, r = s.find(ch), s.rfind(ch)
            if l != -1 and l == r:
                minIndex = min(l, minIndex)
        return minIndex if minIndex != len(s) else -1


start = time.time()
s = Solution3()
assert(s.firstUniqChar("leetcode") == 0)
assert(s.firstUniqChar("loveleetcode") == 2)
assert(s.firstUniqChar("") == -1)
assert(s.firstUniqChar("aabbwwkeke") == -1)
assert(s.firstUniqChar("a") == 0)
assert(s.firstUniqChar("aaa") == -1)
assert(s.firstUniqChar("dddccdbba") == 8)
assert(s.firstUniqChar("dddccdbbaat") == 10)
end = time.time()
print(end-start)
