class Solution:
    def select(self, arr, i):
        i = 0
        for k in range(1, len(arr)):
            if arr[k] < arr[i]:
                i = k
        return i

    def selectionSort(self, arr, n):
        for j in range(0, n):
            minIndex = j
            for i in range(j, n):
                if arr[i] < arr[minIndex]:
                    minIndex = i
            arr[j], arr[minIndex] = arr[minIndex], arr[j]
        return arr
