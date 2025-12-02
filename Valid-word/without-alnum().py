class Solution(object):
    def isValid(self, word):
        if len(word) < 3:
            return False
        vowels = ['a','e','i','o','u','A','E','I','O','U']
        digits = ['0','1','2','3','4','5','6','7','8','9']
        letters = list("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ")
        v = 0    
        c = 0    
        d = 0    
        for i in word:
            if (i not in vowels) and (i not in digits) and (i not in letters):
                d += 1
            # return    
            if (i in letters) and (i not in vowels):
                c += 1    
            if i in vowels:
                v += 1
        if v > 0 and c > 0 and d == 0:
            return True
        return False
