from array import array
from heapq import heappop, heappush

# ========== Bubble Sort ==========
def swap(A, i, j):
    A[i], A[j] = A[j], A[i]

def bubblesort(A):
    swapped = True
      
    for i in range(len(A) - 1):
        if not swapped:
            return
        swapped = False
          
        for j in range(len(A) - 1 - i):
            if A[j] > A[j + 1]:
                swap(A, j, j + 1)
                swapped = True
            
            yield A

# ========== Merge Sort ==========

def mergesort(A, start, end):
    if end <= start:
        return
    
    mid = start + ((end - start + 1) // 2) - 1

    yield from mergesort(A, start, mid)
    yield from mergesort(A, mid + 1, end)
    yield from merge(A, start, mid, end)

def merge(A, start, mid, end):
    merged = []
    leftIdx = start
    rigthIdx = mid + 1

    while leftIdx <= mid and rigthIdx <= end:
        if A[leftIdx] < A[rigthIdx]:
            merged.append(A[leftIdx])
            leftIdx += 1
        else:
            merged.append(A[rigthIdx])
            rigthIdx += 1

    while leftIdx <= mid:
        merged.append(A[leftIdx])
        leftIdx += 1

    while rigthIdx <= end:
        merged.append(A[rigthIdx])
        rigthIdx += 1
    
    for i in range(len(merged)):
        A[start + i] = merged[i]
        yield A

# ========== Quick Sort ==========

def quicksort(a, l, r):
    if l >= r:
        return
    x = a[l]
    j = l
    for i in range(l + 1, r + 1):
        if a[i] <= x:
            j += 1
            a[j], a[i] = a[i], a[j]
        yield a
    a[l], a[j]= a[j], a[l]
    yield a

    yield from quicksort(a, l, j-1)
    yield from quicksort(a, j + 1, r)

# ========== Insertion Sort ==========

def insertionsort(a):
    for j in range(1, len(a)):
        key = a[j]
        i = j-1
          
        while(i >= 0 and a[i] > key):
            a[i+1] = a[i]
            i -= 1
            yield a
        a[i+1] = key
          
        yield a

# ========== Heap Sort ==========

def heapsort(a):
    heap = []
    for element in a:
        heappush(heap, element)

    sort = []

    while heap:
        sort.append(heappop(heap))
        yield sort

# ========== Selection Sort ==========

def selectionsort(a):
    for i in range(len(a)):
        min_index = i

        for j in range(i + 1, len(a)):
            if a[j] < a[min_index]:
                min_index = j
        a[i], a[min_index] = a[min_index], a[i]
        yield a
