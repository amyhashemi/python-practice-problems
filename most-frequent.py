arr = [1, 3, 1, 3, 2, 3]

class mostFrequent:
    '''
    Finds and returns the most frequent item occurring in an array
    '''

    def Solve(self, arr):
        max_item = None
        max_count = -1
        count = {}

        for item in arr:
            if item not in count:
                count[item] = 1
            else:
                count[item]+=1
            if count[item] > max_count:
                max_count = count[item]
                max_item = item

        return max_item
        

item = mostFrequent().Solve(arr)

print(item)