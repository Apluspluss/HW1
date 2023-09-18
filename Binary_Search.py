import time
import matplotlib.pyplot as plt

def Recursive_Binary_Search(A, x, low, high):
    if low > high:
        return -1  # Element not found
    
    mid = (low + high) // 2

    if A[mid] == x:
        return mid
    elif A[mid] < x:
        return Recursive_Binary_Search(A, x, mid + 1, high)
    else:
        return Recursive_Binary_Search(A, x, low, mid - 1)
