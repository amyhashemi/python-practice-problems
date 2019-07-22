class Solution:
    def longestPalindrome(self, s: str) -> str:
        p1 = 0
        p2 = len(s) - 1

        for i in range(len(s)):
            for j in range(1, len(s)):
            
                p1 = s[i]
                p2 = s[len(s)-j]
                
                print(p1)
                print(p2)

                if p1 == p2:
                    p1 = s[i+1]
                

        return

Solution().longestPalindrome('sadps')