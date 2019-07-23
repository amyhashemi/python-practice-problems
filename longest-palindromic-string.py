class Solution:
    def longestPalindrome(self, s: str) -> str:

        i = 0
        j = 0
        length = len(s)
        largest = 0
        palindices = []
        longestPalindrome = ''
        checkarray = [[0 for item in range(0, length)] for num in range(0, length)]
        
        for num in range(0, length):
            checkarray[num][num] = 1

        
        for i in range(0, length-1):
            j+=1
            if s[i] == s[j]:
                checkarray[i][j] = checkarray[i+1][j-1]
            else:
                checkarray[i][j] = max(checkarray[i][j-1], checkarray[i+1][j])
        
        for i in checkarray:
            for j in checkarray:
                if checkarray[i][j] >= largest:
                    palindices[0] = checkarray[i]
                    palindices[1] = checkarray[j]

        for item in range(palindices[0], palindices[1]):
            longestPalindrome + s[item]

        print(longestPalindrome)

        return

Solution().longestPalindrome('sadps')