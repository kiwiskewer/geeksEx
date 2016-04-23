



class SortSearchSolutions:
    def bubbleSort(self, A):
        for i in range(len(A)):
            swapped = False
            for j in range(len(A)-i-1):
                if A[j] > A[j+1]:
                    A[j], A[j+1]  = A[j+1], A[j]
                    swapped = True
            if not swapped:
                break
    def selectSort(self, A):
        for i in range(len(A)):
            idx = i
            for j in range(i+1, len(A)):
                if A[idx] > A[j]:
                    idx = j
            A[i],A[idx] = A[idx], A[i]
    def binarySearch(self,A,n):
        if not A:
            return False
        SA = sorted(A)
        h = len(A)//2
        if SA[h] == n:
            return True
        elif SA[h] > n:
            return self.binarySearch(SA[0:h-1],n)
        elif SA[h] < n:
            return self.binarySearch(SA[h+1:],n)

    def insertSort(self,A):
        for i in range(len(A)-1):
            j = i+1
            while j>0 and A[j]<A[j-1]:
                A[j],A[j-1] = A[j-1],A[j]
                j -= 1

    def mergeSort(self,A,s,e):
        if e-s == 0:
            return [A[s]]

        left = self.mergeSort(A,s,(s+e)//2)
        right = self.mergeSort(A,(s+e)//2+1,e)
        s_arr = self.merge(left, right)
        return s_arr

    def merge(self,left,right):
        arr = []
        while left and right:
            if left[0] < right[0]:
                arr.append(left.pop(0))
            else:
                arr.append(right.pop(0))
        while left:
            arr.append(left.pop(0))
        while right:
            arr.append(right.pop(0))
        return arr


algSort = SortSearchSolutions()

A=[2,7,9,3,98,1]
algSort.bubbleSort(A)
print("bubbleSort:",A)


A=[2,7,9,3,98,1]
algSort.selectSort(A)
print("selectSort:", A)

A=[2,7,9,3,98,1]
algSort.insertSort(A)
print("insertSort:", A)

A=[2,7,9,3,98,1]
B = algSort.mergeSort(A,0,len(A)-1)
print("mergeSort:", B)


print(algSort.binarySearch(A,98))