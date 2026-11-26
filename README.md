##### Phase 0

 **array** Representation, construction, shape, strides, indexing, slicing

**operations** Element-wise arithmetic, comparisons, broadcasting

**algorithms** Searching, sorting, selection, hashing-based operations

**statistics** Aggregations, median, variance, histogram data

**linalg** Vectors, matrices, transpose, dot products, multiplication

**io** CSV loading/saving and data cleaning

**plot** Line, scatter, bar, histogram, optional heat map

**tests** Unit, property, integration, regression, and performance tests

**examples** End-to-end applications using real datasets



##### Phase 1

- construction 
- nested-input flattening
- shape, size, ndim validation, also why tuple
- flatten
- reshape
- copying
- readable string conversion
- exceptions(define specific error type)

##### Phase 2

access is O(1) whne dim is fixed

copying slice & view-based slice

- positive & negative indexing operations 
- bounds checks
- basic slicing
- row/ column extraction

##### Phase 3

- element-wisse operations
- broadcasting 
  - Think of each dimension independently:

$$
result_i =
\begin{cases}
A_i & A_i=B_i\\
A_i & B_i=1\\
B_i & A_i=1\\
\text{Error} & \text{otherwise}
\end{cases}
$$

todo: time-complexity

optimization: eq & nq, "Even though both arrays have identical data and shapes, Python considers them unequal."



##### Phase 4

Operations:

sum

min

max

mean

median [optimize sort al]

variance

standard_deviation

argmin

argmax

count

unique



##### Pase 5

- linear search
- binary search
- merge sort

$$
O(n \log n)
$$



- bubble sort  

$$
O(n^2)
$$

- quicksort

$$
O(n \log n)
$$



- quickselect
- duplicate detection
- top-k selection



