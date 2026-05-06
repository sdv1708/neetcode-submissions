class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        
        def merge(L, R, arr): 
            M = (L + R) // 2 
            leftArr = arr[L:M+1]
            rightArr = arr[M+1:R+1]

            i, j, k = L, 0, 0 # (arr, leftArr, rightArr) are the indices being tracked

            while j < len(leftArr) and k < len(rightArr): 
                if leftArr[j] <= rightArr[k]: 
                    arr[i] = leftArr[j]
                    j += 1 
                else: 
                    arr[i] = rightArr[k]
                    k += 1 
                i += 1 

            # for any remaining elements extend the arr 
            while j < len(leftArr): 
                arr[i] = leftArr[j]
                j += 1 
                i += 1 

            while k < len(rightArr): 
                arr[i] = rightArr[k]
                k += 1 
                i += 1 

        def mergeSort(arr, l, r):
            if l >= r: 
                return 
            m = (l + r) // 2 # halving the array 
            #recursive call as we divide the array into constituent elements 
            mergeSort(arr, l, m) # start to middle 
            mergeSort(arr, m+1, r) # mid + 1 to end 
            merge(l, r, arr)

        mergeSort(nums, 0, len(nums) - 1)
        return nums




        