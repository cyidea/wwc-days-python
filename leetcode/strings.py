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
        
        r = 0
        rest_string = s
        while rest_string:
            print(rest_string)
            c = rest_string[0]
            the_next = False
            if len(rest_string) > 1:
                the_next = rest_string[1]
            if c == 'I':
                if the_next:
                    if the_next == 'I':
                        r += 1
                    elif the_next == 'V':
                        r += 4
                        rest_string = rest_string[2:]
                        continue
                    elif the_next == 'X':
                        r += 9
                        rest_string = rest_string[2:]
                        continue
                else:
                    r += 1
            elif c == 'X':
                if the_next:
                    
                    if the_next == 'L':
                        r += 40
                        rest_string = rest_string[2:]
                        continue
                    elif the_next == 'C':
                        r += 90
                        rest_string = rest_string[2:]
                        continue
            elif c== 'C':
                if the_next:
                    
                    if the_next == 'D':
                        r += 400
                        rest_string = rest_string[2:]
                        continue
                    elif the_next == 'M':
                        r += 900
                        rest_string = rest_string[2:]
                        continue
            # special cases ended here
            elif c == 'V':
                r += 5
            elif c == 'L':
                r += 50
            elif c == 'D':
                r += 500
            elif c == 'M':
                r += 1000
            rest_string = rest_string[1:]

        return r

s = Solution()
ret = s.romanToInt("MCMXCIV")
print(f'{ret}')