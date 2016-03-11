



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
    def mergeSort(self,A):
algSort = SortSearchSolutions()

A=[2,7,9,3,98,1]
algSort.bubbleSort(A)
print("bubbleSort:",A)


A=[2,7,9,3,98,1]
algSort.selectSort(A)
print("selectSort:", A)

A=[2,7,9,3,98,1]
algSort.insertSort(A)
print("selectSort:", A)


print(algSort.binarySearch(A,98))