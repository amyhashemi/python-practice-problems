
class Solution:
    
    def reverse(self, x: int):
        '''
        This function takes in an int and reverses the digits of the integer

        Assume we are dealing with an environment which could only store integers 
        within the 32-bit signed integer range: [−231,  231 − 1]. For the purpose 
        of this problem, assume that your function returns 0 when the reversed integer overflows.
        '''

        if x < -2**31 or x > (2**31) - 1:
            return 0

        else:
            strg = str(x)

            if x >= 0:               
                revst = strg[::-1]
                revst = int(revst)

            else:
                sign = strg[:1]
                temp2 = str(abs(x))[::-1]

                revst = sign + temp2

                revst = int(revst)

            if revst < -2**31 or revst > (2**31) - 1:
                return 0
            else:
                return int(revst)
 

answer = Solution().reverse(1534236469)
print(answer)