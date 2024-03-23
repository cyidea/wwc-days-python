class Solution:
    def __init__(self) -> None:
        self.dic = {} #stores the values
        self.dic['I'] = 1
        self.dic['V'] = 5
        self.dic['X'] =10
        self.dic['L'] = 50
        self.dic['C'] = 100
        self.dic['D'] = 500
        self.dic['M'] = 1000

    """
    https://leetcode.com/problems/roman-to-integer/
    """
    def romanToInt(self, s: str) -> int:
        print(f'{self.dic}')
        for c in s:
            print(c)
        return 0

s = Solution()
ret = s.romanToInt("III")
print(f'{ret}')