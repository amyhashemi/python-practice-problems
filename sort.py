def bubbleSort(arr):
    n = len(arr)

    for i in range(n):
        for j in range(0, n-i-1): #keeping track of elements that are sorted
        #traverse the array from 0 to n-i-1 and swap if the found element is greater
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]


arr = [64, 34, 25, 12, 22, 11, 90]

bubbleSort(arr)

print("Sorted array is:")
for i in range(len(arr)):
    print(arr[i])