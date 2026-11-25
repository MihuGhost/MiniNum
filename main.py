import numpy as np
from mininum import Array


# arr = Array(
#     [10, 20, 30, 11, 21, 31, 40, 50, 60, 41, 51, 61,
#      101, 201, 301, 111, 211, 311, 401, 501, 601, 411, 511, 611],
#     (2, 3, 2, 2)
# )
# for i in range(len(arr.data)):
#     print(i, arr.data[i])
#
# print(repr(arr))
# print(str(arr))
# var = arr[1, 1, 1]
# print(repr(var))
#
# # [[[[10, 20], [30, 11]]
# #      , [[21, 31], [40, 50]]
# #      , [[60, 41], [51, 61]]]
# #
# #
# #     , [[[101, 201], [301, 111]]
# #      , [[211, 311], [401, 501]]
# #      , [[601, 411], [511, 611]]]]
#
# b = Array(
#     [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12],
#     (2, 3, 2, 1)
# )
# for i in range(len(b.data)):
#     print(i, b.data[i])
#
# print(repr(b))
# print(str(b))
#
# c = Array(
#     [1, 2, 3, 4, 5, 6, 7, 8],
#     (2, 1, 2, 2)
# )
# for i in range(len(c.data)):
#     print(i, c.data[i])
#
# print(repr(c))
# print(str(c))

# def merge_sort(arr):
#     # Base case
#     if len(arr) <= 1:
#         return arr
#
#     # Divide
#     mid = len(arr) // 2
#
#     left = merge_sort(arr[:mid])
#     right = merge_sort(arr[mid:])
#
#     # merge
#     result = []
#     i = 0
#     j = 0
#     while i < len(left) and j < len(right):
#         if left[i] <= right[j]:
#             result.append(left[i])
#             i += 1
#         else:
#             result.append(right[j])
#             j += 1
#
#     result.extend(left[i:])
#     result.extend(right[j:])
#
#     return result


# def main(arr):
#     if len(arr) <= 1:
#         return arr
#
#     mid = len(arr) // 2
#     left = main(arr[:mid])
#     right = main(arr[mid:])
#
#     result = []
#     i, j = 0, 0
#     while i < len(left) and j < len(right):
#         if left[i] <= right[j]:
#             result.append(left[i])
#             i += 1
#         else:
#             result.append(right[j])
#             j += 1
#
#     result.extend(left[i:])
#     result.extend(right[j:])
#
#     return result
#

# print(main([1, 38, 12, 27, 43, 9, 31, 18]))

#
# def partition(arr, pivot_index):
#     pivot = arr[pivot_index]
#     left = []
#     right = []
#     for i, x in enumerate(arr):
#         if i == pivot_index:
#             continue
#         if x <= pivot:
#             left.append(x)
#         else:
#             right.append(x)
#
#     return left, pivot, right


# def quick_sort(arr):
#     if len(arr) <= 1:
#         return arr
#
#     pivot_index = len(arr) // 2
#
#     # partition
#     pivot = arr[pivot_index]
#     left = []
#     right = []
#     for i, x in enumerate(arr):
#         if i == pivot_index:
#             continue
#         if x <= pivot:
#             left.append(x)
#         else:
#             right.append(x)
#
#     left_result = quick_sort(left)
#     right_result = quick_sort(right)
#     return left_result + [pivot] + right_result
#
#
# print(quick_sort([1, 38, 121, 27, 43, 9, 31, 18]))

#
# def bubble_sort(arr):
#     n = len(arr)
#
#     for i in range(n):
#         for j in range(n - i - 1):
#             if arr[j] > arr[j + 1]:
#                 arr[j], arr[j + 1] = arr[j + 1], arr[j]
#
#     return arr

# print(bubble_sort([1, 38, 121, 27, 43, 9, 31, 18]))



# def quick_sort(arr):
#     if len(arr) <= 1:
#         return arr
#
#     pivot_index = len(arr) // 2
#
#     # partition
#     left, pivot, right = partition(arr, pivot_index)
#
#     left_result = quick_sort(left)
#     right_result = quick_sort(right)
#     return left_result + [pivot] + right_result

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

    return left, pivot,right

def quick_select(arr, k):
    if len(arr) == 1:
        return arr[0]

    pivot_index = len(arr) // 2

    left, pivot, right = partition(arr, pivot_index)

    if k < len(left):
        return quick_select(left,k)
    elif k == len(right):
        return pivot
    else:
        return quick_select(right, k- len(left) - 1)

print(quick_select([1, 38, 121, 27, 43, 9, 31, 18],3))