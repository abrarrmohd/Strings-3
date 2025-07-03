"""
Approach: looking at the pattern we can calulate in groups of three and do it for all the triplets present
in the num given
t.c. => O(1) since max of 4 triplest = O(12)
s.c. => O(1)
"""
class Solution:
    def numberToWords(self, num: int) -> str:
        groups = ["", "Thousand", "Million","Billion"]
        below_ten = ["", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine"]
        below_twenty = ["Ten", "Eleven", "Twelve", "Thirteen", "Fourteen", "Fifteen", "Sixteen", "Seventeen", "Eighteen", "Nineteen"]
        below_hundred = ["Twenty", "Thirty", "Forty", "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"]
        hundred = "Hundred"
        zero = "Zero"
        def helper( num):
            if num == 0:
                return ""

            if 1 <= num <= 9:
                return below_ten[num]

            if num < 20:
                return below_twenty[num%10]

            if num < 100:
                return below_hundred[(num//10) - 2] + " " + helper(num%10).strip()

            if num >= 100:
                return helper(num//100) + " " + hundred + " " + helper(num%100).strip()
            return ""
        
        factor = 1000
        groupNum = 0
        res = ""
        if num == 0:
            return zero
        while num:
            ret = helper(num % 1000).strip()
            if groupNum > 0 and ret != "":
                res =  ret + " " + groups[groupNum] + " " + res.strip()
            else:
                res = ret + res.strip()
    
            num = ((num//1000))
            groupNum += 1

        return res.strip()
    
        

    