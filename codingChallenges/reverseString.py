from typing import List


class Solution:
    def reverseString4(self, s: List[str]) -> None:
        for i in range(0, int(len(s)/2)):
            s[i], s[int(len(s)-1-i)] = s[int(len(s)-1-i)], s[i]

    def reverseString3(self, s: List[str]) -> None:
        l, r = 0, len(s)-1
        while l < r:
            s[l], s[r] = s[r], s[l]
            l += 1
            r -= 1

    def reverseString2(self, s: List[str]) -> None:

        def helper(start, end, list):
            if start >= end:
                return

            list[start], list[end] = list[end], list[start]

            return helper(start+1, end-1, list)

        helper(0, len(s)-1, s)

    def reverseString(self, s: List[str]) -> None:
        s.reverse()


s = Solution

arr = ["h", "e", "l", "l", "o"]
s.reverseString(s, arr)

print(arr)
