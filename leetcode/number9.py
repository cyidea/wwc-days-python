class Solution:
    """  https://leetcode.com/problems/palindrome-number/ """
    def isPalindrome(self, x: int) -> bool:
        
        # getting digits from right to left and put them together again.
        # but if it is a negative number it will be definitely False
        if x < 0:
            return False
        
        if x < 10:
            return True
        
        len_of_int = len(str(x))

        val = 0
        pow = 0
        for i in str(x):
            newval = int(i) * 10**pow
            val += newval
            pow += 1

        # print(val)
        if val == x:
            return True
        
        return False
    
solution = Solution()
y = solution.isPalindrome(12345)