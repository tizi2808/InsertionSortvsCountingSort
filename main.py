import sys
import matplotlib.pyplot as plt
import numpy as np
import time
import random

inf = sys.maxsize

def CountingSort(arr):
    max_val = max(arr)
    counts = [0] * (max_val + 1)
    sorted = [0] * len(arr)
    for i in range(0, len(arr)):
        counts[arr[i]] += 1
    for i in range(1, max_val+1):
        counts[i] = counts[i] + counts[i-1]
    for j in range(len(arr)-1, 0, -1):
        sorted[counts[arr[j]]-1] = arr[j]
        counts[arr[j]] -= 1
    
    

def InsertionSort(A):
    for j in range(2,len(A)):
        key = A[j]
        i = j - 1
        while i > 0 and A[i] > key:
            A[i + 1] = A[i]
            i = i - 1
        A[i + 1] = key


def plotSortGraph(algType, insertType, arrayDim, plot=True):
    x, y = [], []
    for i in range(1, arrayDim, 5):
        x.append(i)
        A = np.arange(i) if insertType == 0 else random.sample(range(i), i)
        if algType == 0:
            start = time.perf_counter()
            InsertionSort(A)
            end = time.perf_counter()
        else:
            start = time.perf_counter()
            CountingSort(A)
            end = time.perf_counter()
        z = y[-1] if (len(y) != 0) else 0
        y.append((end - start) / i + z)
    if plot:
        plt.plot(x, y)
        title = 'Insertion-Sort' if algType == 0 else 'Counting-Sort'
        title += ' on Ordered List ' if insertType == 0 else ' on Randomized List '
        title += str(arrayDim)
        plt.title(title)
        plt.show()
    else:
        return x, y


if __name__ == '__main__':
    x1, y1 = plotSortGraph(0, 1, 500, False)
    x2, y2 = plotSortGraph(1, 1, 500, False)
    plt.plot(x1, y1, label='InsertionSort')
    plt.plot(x2, y2, label='CountingSort')
    plt.legend()
    plt.show()