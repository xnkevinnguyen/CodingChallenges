import time


class Solution:

    def isValid(self, s: str) -> bool:
        parenDict = {"{": "}", "(": ")", "[": "]"}
        stack = []
        for n in s:
            if stack.__len__() == 0:
                if parenDict.get(n, 0) == 0:
                    return False
                else:
                    stack.append(n)
            else:
                topElem = stack.pop()
                if parenDict[topElem] != n:
                    stack.append(topElem)
                    if parenDict.get(n, 0) != 0:
                        stack.append(n)
                    else:
                        return False

        if stack.__len__() == 0:
            return True
        return False

    def isValid2(self, s: str) -> bool:
        parenDict = {"{": "}", "(": ")", "[": "]"}
        stack = []
        for n in s:
            if stack:
                topElem = stack.pop()
                if parenDict[topElem] != n:
                    stack.append(topElem)
                    if parenDict.get(n, 0) != 0:
                        stack.append(n)
                    else:
                        return False
            else:
                if n in parenDict:
                    stack.append(n)
                else:
                    return False

        return not stack


s = Solution
examples = ["((", "", "(", "()", "()[]{}", "(]", "([)]", "{[]}"]

start = time.time()
for ex in examples:
    s.isValid(s, ex)
end = time.time()

print(end - start)

start = time.time()
for ex in examples:
    s.isValid2(s, ex)
end = time.time()

print(end - start)
