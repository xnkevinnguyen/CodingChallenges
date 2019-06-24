from typing import List


class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        myList = []
        for email in emails:
            emailArr = email.split("@")
            endLocal = emailArr[0].split("+")[0].replace(".", "")
            endEmail = endLocal+"@"+emailArr[1]
            myList.append(endEmail)

        uniqueEmailList = list(dict.fromkeys(myList))
        return len(uniqueEmailList)

    def numUniqueEmails2(self, emails: List[str]) -> int:
        uniqueEmail = set()
        for email in emails:
            local, domain = email.split("@")
            endLocal = local.split("+")[0].replace(".", "")
            endEmail = endLocal+"@"+domain
            uniqueEmail.add(endEmail)

        return len(uniqueEmail)


sampleList = ["test.email+alex@leetcode.com",
              "test.e.mail+bob.cathy@leetcode.com", "testemail+david@lee.tcode.com"]

sampleList2 = ["test.email+alex@leetcode.com", "test.email.leet+alex@code.com"]

s = Solution
numOfUniqueEmail = s.numUniqueEmails2(s, sampleList)
print(numOfUniqueEmail)
numOfUniqueEmail = s.numUniqueEmails2(s, sampleList2)
print(numOfUniqueEmail)
