class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        x = start^goal   
        c = 0              
        while x > 0:
            c += (x & 1) 
            x //= 2       
        return c

EXPLANATION::
First I just checked how different both numbers are using XOR.
Then you know it basically shows all the places where the bits don’t match.
After that I just counted how many 1s came in that result.
Those 1s are exactly the flips we need simple as that
