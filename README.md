##### Phase 0

 

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

