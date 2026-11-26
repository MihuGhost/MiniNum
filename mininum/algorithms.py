from mininum import Array
import heapq


def sort(arr, algorithm="merge"):
    if not isinstance(arr, Array):
        raise TypeError("Input must be an Array object")

    if algorithm == "merge":
        sorted_data = merge_sort(arr.data)

    elif algorithm == "quick":
        sorted_data = quick_sort(arr.data)

    elif algorithm == "bubble":
        sorted_data = bubble_sort(arr.data)

    else:
        raise ValueError(f"Unknown sorting algorithm: {algorithm}")

    return Array(sorted_data, arr.shape)


# def argsort(arr):
#     hash_table = {}
#
#     # Build the hashtable
#     for i in range(len(arr)):
#         value = arr[i]
#
#         if value not in hash_table:
#             hash_table[value] = []
#
#         hash_table[value].append(i)
#
#     # Sort values and collect their original indices
#     0indices = []
#     for value in sort(list(hash_table.keys())):
#         indices.extend(hash_table[value])
#
#     return indices


def argsort(arr):
    if not isinstance(arr, Array):
        raise TypeError("Input must be an Array object")

    hash_table = {}

    # Step 1: Build the hash table
    for i in range(arr.size):
        value = arr.data[i]

        if value not in hash_table:
            hash_table[value] = []

        hash_table[value].append(i)

    # Step 2: Extract unique values
    unique_values = list(hash_table.keys())

    # Step 3: Convert unique values into an Array
    values_array = Array(unique_values, (len(unique_values),))

    # Step 4: Sort unique values
    sorted_values = sort(values_array)

    # Step 5: Collect original indices
    indices = []

    for value in sorted_values.data:
        indices.extend(hash_table[value])

    # Step 6: Return an Array
    return Array(indices, arr.shape)


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
    result.extend(right[j:])

    return result


def quick_sort(arr):
    if len(arr) <= 1:
        return arr

    pivot_index = len(arr) // 2

    left, pivot, right = partition_list(arr, pivot_index)

    left_result = quick_sort(left)
    right_result = quick_sort(right)
    return left_result + [pivot] + right_result


def bubble_sort(arr):
    for i in range(len(arr)):
        for j in range(len(arr) - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

    return arr


def quick_select(arr, k):
    if len(arr) == 1:
        return arr[0]

    pivot_index = len(arr) // 2

    left, pivot, right = partition_list(arr, pivot_index)

    if k < len(left):
        return quick_select(left, k)
    elif k == len(left):
        return pivot
    else:
        return quick_select(right, k - len(left) - 1)


def unique_set(arr):
    hashset = set()
    for x in arr:
        if x in hashset:
            print("Duplicate:", x)
            return False
        else:
            hashset.add(x)
    return len(hashset) == len(arr)


def top_k(arr, k):
    if not isinstance(arr, Array):
        raise TypeError("Input must be an Array object")
    return top_k_list(arr.data, k)


def top_k_list(arr, k):
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


def partition_list(arr, pivot_index):
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


def partition(arr, pivot_index):
    if not isinstance(arr, Array):
        raise TypeError("Input must be an Array object")

    # Convert multidimensional index to flat index
    if isinstance(pivot_index, int):
        if len(arr.shape) != 1:
            raise ValueError("Multidimensional arrays require a tuple index")
        flat_index = pivot_index
    else:
        flat_index = flatten_index(pivot_index, arr.shape)

    # Use the existing partition algorithm
    left, pivot, right = partition_list(arr.data, flat_index)

    return (
        Array(left, (len(left),)),
        pivot,
        Array(right, (len(right),))
    )


def flatten_index(index, shape):
    if len(index) != len(shape):
        raise ValueError("Index dimension does not match array dimension")

    flat_index = 0

    for i, dim in zip(index, shape):
        if i < 0 or i >= dim:
            raise IndexError("Array index out of range")

        flat_index = flat_index * dim + i

    return flat_index
