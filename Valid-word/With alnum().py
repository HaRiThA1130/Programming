class Solution(object):
    def isValid(self, word):
        """
        :type word: str
        :rtype: bool
        """
        if len(word)<3:
            return False
        if word.isalnum() == False:
            return False
        vowels=['a','e','i','o','u','A','E','I','O','U']
        digits=['0','1','2','3','4','5','6','7','8','9']
        # vowels=False
        # consonants=False
        v = 0
        c = 0
        for i in word:
            if i in vowels:
                v = v + 1
            if i not in digits and i not in vowels:
                c = c + 1

        print(v)
        print(c)
        if v >= 1 and c >= 1:
            return True
        else:
            return False
