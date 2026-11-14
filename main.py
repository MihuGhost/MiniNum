import numpy as np
from mininum import Array

arr = Array(
    [10, 20, 30, 11, 21, 31, 40, 50, 60, 41, 51, 61,
     101, 201, 301, 111, 211, 311, 401, 501, 601, 411, 511, 611],
    (2, 3, 2, 2)
)
for i in range(len(arr.data)):
    print(i, arr.data[i])

print(repr(arr))
print(str(arr))
var = arr[1, 1, 1]
print(repr(var))

# [[[[10, 20], [30, 11]]
#      , [[21, 31], [40, 50]]
#      , [[60, 41], [51, 61]]]
#
#
#     , [[[101, 201], [301, 111]]
#      , [[211, 311], [401, 501]]
#      , [[601, 411], [511, 611]]]]
