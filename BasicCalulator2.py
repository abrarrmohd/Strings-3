"""
Approach: calculate the vaklues on the go without having to use a stack. Need to take care during / and *
t.c. => O(n)
s.c. =>O(n)
same solution can be solved using a for loop
"""
class Solution:
    def calculate(self, s: str) -> int:
        s = s.strip()
        if not s:
            return 0

        n = len(s)
        self.idx = 0
        self.res = 0

        def skipSpace():
            while self.idx < n and s[self.idx] == " ":
                self.idx += 1
        
        def helper(tail):
            if self.idx == n:
                return

            currNum = 0
            currSign = 1

            skipSpace()
            if self.idx == 0:
                if s[self.idx] == "-":
                    currSign = -1
                    self.idx += 1
            else:
                if s[self.idx] == "+":
                    currSign = 1
                elif s[self.idx] == "-":
                    currSign = -1
                elif s[self.idx] == "/":
                    currSign = -2
                elif s[self.idx] == "*":
                    currSign = 2
                self.idx += 1

            skipSpace()
            while self.idx < n and s[self.idx].isnumeric():
                currNum = currNum * 10 + (ord(s[self.idx]) - ord('0'))
                self.idx += 1
            if currSign == 1:
                self.res += currNum
                helper(currNum)
            elif currSign == -1:
                self.res -= currNum
                helper(-currNum)
            elif currSign == 2:
                og_res = self.res - tail
                self.res = og_res + (tail * currNum)
                helper(tail*currNum)
            else:
                og_res = self.res - tail
                self.res = og_res + int(tail / currNum)
                helper(int(tail/currNum))
        helper(0)
        return self.res
