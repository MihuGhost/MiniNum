import heapq
import itertools
from mininum import Array


def flatten(data):
    result = []

    for item in data:
        if isinstance(item, list):
            result.extend(flatten(item))
        else:
            result.append(item)

    return result


def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i

    return -1


def binary_search(arr, target):
    if not is_sorted(arr):
        raise ValueError("Array must be sorted")

    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2

        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    return -1


def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    result = []
    i, j = 0, 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[:j])

    return result


def quick_sort(arr):
    if len(arr) <= 1:
        return arr

    pivot_index = len(arr) // 2

    left, pivot, right = partition(arr, pivot_index)

    left_result = quick_sort(left)
    right_result = quick_sort(right)
    return left_result + [pivot] + right_result


def bubble_sort(marr):
   arr = flatten(marr)
   for i in range(len(arr)):
        for j in range(len(arr) - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

   return Array(arr, marr.shape)


def quick_select(arr, k):
    if len(arr) == 1:
        return arr[0]

    pivot_index = len(arr) // 2

    left, pivot, right = partition(arr, pivot_index)

    if k < len(left):
        return quick_select(left, k)
    elif k == len(right):
        return pivot
    else:
        return quick_select(right, k - len(left) - 1)


def unique_set(arr):
    hashset = set()
    for x in arr:
        if x in hashset:
            print("Duplicate:", x)
        else:
            hashset.add(x)


def top_k(arr, k):
    if k < 0 or k > len(arr):
        raise ValueError("Invalid k")

    if k == 0:
        return []

    heap = arr[:k]
    heapq.heapify(heap)

    for value in arr[k:]:
        if value > heap[0]:
            heapq.heapreplace(heap, value)

    return heap


# for binary search
def is_sorted(arr):
    for i in range(len(arr) - 1):
        if arr[i] > arr[i + 1]:
            return False
    return True


def partition(arr, pivot_index):
    pivot = arr[pivot_index]
    left = []
    right = []
    for i, x in enumerate(arr):
        if i == pivot_index:
            continue
        if x <= pivot:
            left.append(x)
        else:
            right.append(x)

    return left, pivot, right
