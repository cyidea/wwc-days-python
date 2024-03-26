class Solution:
    
    """
    https://leetcode.com/problems/integer-to-roman/description/
    """
    def intToRoman(self, num: int) -> str:
        mstr = ''

        val = num/1000
        intval = int(val)
        if intval >= 1:
            mstr += "M"*intval
        remaining = num % 1000

        intval = int(remaining/900)
        if intval >= 1:
            mstr += 'CM'*intval
        remaining = remaining % 900

        intval = int(remaining/500)
        if intval >= 1:
            mstr += 'D'*intval
        remaining = remaining % 500

        intval = int(remaining/400)
        if intval >= 1:
            mstr += 'CD'*intval
        remaining = remaining % 400

        # get the rest of them figured out:
        intval = int(remaining/100)
        if intval >= 1:
            mstr += 'C'*intval
        remaining = remaining % 100

        intval = int(remaining/90)
        if intval >= 1:
            mstr += 'XC'*intval
        remaining = remaining % 90

        intval = int(remaining/50)
        if intval >= 1:
            mstr += 'L'*intval
        remaining = remaining % 50

        intval = int(remaining/40)
        if intval >= 1:
            mstr += 'XL'*intval
        remaining = remaining % 40

        intval = int(remaining/10)
        if intval >= 1:
            mstr += 'X'*intval
        remaining = remaining % 10

        intval = int(remaining/9)
        if intval >= 1:
            mstr += 'IX'*intval
        remaining = remaining % 9

        intval = int(remaining/5)
        if intval >= 1:
            mstr += 'V'*intval
        remaining = remaining % 5

        intval = int(remaining/4)
        if intval >= 1:
            mstr += 'IV'*intval
        remaining = remaining % 4

        if remaining > 0:
            mstr += 'I' * remaining           
        
        return mstr

s = Solution()
ret = s.intToRoman(1994)
print(f'{ret}') 