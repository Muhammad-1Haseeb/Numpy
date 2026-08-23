# # import numpy as np


# # # ============================================================
# # # 1. NumPy Array vs Python List
# # # ============================================================

# # # Python list
# # numbers_list = [10, 20, 30, 40]

# # # * 3 repeats the list three times
# # print(numbers_list * 3)


# # # NumPy array
# # numbers = np.array([10, 20, 30, 40])

# # # * 3 multiplies every element by 3
# # print(numbers * 3)


# # # ============================================================
# # # 2. ndarray
# # # ============================================================

# # # np.array() creates a NumPy ndarray
# # print(type(numbers))


# # # ============================================================
# # # 3. 1D Array
# # # ============================================================

# # numbers_1d = np.array([10, 20, 30, 40])

# # # ndim tells us how many dimensions the array has
# # print(numbers_1d.ndim)  # 1


# # # ============================================================
# # # 4. 2D Array
# # # ============================================================

# # numbers_2d = np.array([
# #     [10, 20, 30, 40],
# #     [50, 60, 70, 80]
# # ])

# # print(numbers_2d)
# # print(numbers_2d.ndim)  # 2


# # # ============================================================
# # # 5. Adding More Rows Does NOT Create More Dimensions
# # # ============================================================

# # numbers_2d = np.array([
# #     [10, 20, 30, 40],
# #     [50, 60, 70, 80],
# #     [90, 100, 110, 120]
# # ])

# # # Still 2D because we still have rows containing values
# # print(numbers_2d.ndim)  # 2


# # # ============================================================
# # # 6. 3D Array
# # # ============================================================

# # # Here we add another level of nesting
# # numbers_3d = np.array([
# #     [
# #         [1, 2, 3],
# #         [4, 5, 6]
# #     ],
# #     [
# #         [7, 8, 9],
# #         [10, 11, 12]
# #     ]
# # ])

# # print(numbers_3d)
# # print(numbers_3d.ndim)  # 3


# # # ============================================================
# # # 7. Shape
# # # ============================================================

# # numbers = np.array([
# #     [1, 2],
# #     [3, 4],
# #     [5, 6],
# #     [7, 8]
# # ])

# # # shape tells us the size of each dimension
# # # (4, 2) = 4 rows and 2 columns
# # print(numbers.shape) # this will print (4, 2)

# # # shape returns a tuple
# # print(type(numbers.shape))


# # # ============================================================
# # # 8. 2D Indexing
# # # ============================================================

# # # Format:
# # # numbers[row, column]

# # print(numbers[2, 0])  # 5
# # print(numbers[0, 1])  # 2
# # print(numbers[3, 0])  # 7


# # # ============================================================
# # # 9. Negative Indexing
# # # ============================================================

# # # Negative indexes count from the end

# # print(numbers[-1, -1])  # 8
# # print(numbers[-3, -2])  # 3


# # # ============================================================
# # # 10. Slicing Rows
# # # ============================================================

# # # start is included, stop is excluded
# # # 1:3 means rows 1 and 2

# # print(numbers[1:3])

# # # Output:
# # # [[3 4]
# # #  [5 6]]


# # # ============================================================
# # # 11. Slicing Rows + Selecting a Column
# # # ============================================================

# # # Rows 1 and 2 + column 0
# # print(numbers[1:3, 0])

# # # Output:
# # # [3 5]


# # # ============================================================
# # # 12. Slicing Rows + Selecting Another Column
# # # ============================================================

# # # Rows 1 and 2 + column 1
# # print(numbers[1:3, 1])

# # # Output:
# # # [4 6]


# # # ============================================================
# # # 13. Slicing Rows + All Columns
# # # ============================================================

# # # 1:3  -> rows 1 and 2
# # # :    -> all columns

# # print(numbers[1:3, :])

# # # Output:
# # # [[3 4]
# # #  [5 6]]


# import numpy as np


# # ============================================================
# # NUMPY BRICK #2 — dtype
# # ============================================================


# # ============================================================
# # 1. Checking dtype of an Integer Array
# # ============================================================

# numbers = np.array([10, 20, 30, 40])

# # dtype tells us the data type of the array
# print(numbers.dtype)

# # Output:
# # int64


# # ============================================================
# # 2. Checking dtype of a Float Array
# # ============================================================

# numbers = np.array([10.5, 20.5, 30.5])

# print(numbers.dtype)

# # Output:
# # float64


# # ============================================================
# # 3. Mixed Integers + Floats
# # ============================================================

# # NumPy needs a compatible/common dtype
# # so the integers are converted to floats

# mixed = np.array([1, 2, 3.5])

# print(mixed)
# print(mixed.dtype)

# # Output:
# # [1.  2.  3.5]
# # float64


# # ============================================================
# # 4. Explicitly Choosing a dtype
# # ============================================================

# # We can tell NumPy which dtype we want

# numbers = np.array([10, 20, 30, 40], dtype=np.float32)

# print(numbers)
# print(numbers.dtype)

# # Output:
# # [10. 20. 30. 40.]
# # float32


# # ============================================================
# # 5. Converting Floats to Integers
# # ============================================================

# # dtype=int tells NumPy to convert the values to integers

# numbers = np.array([1, 2, 3.5], dtype=int)

# print(numbers)
# print(numbers.dtype)

# # Output:
# # [1 2 3]
# # int64

# # Notice:
# # 3.5 became 3.
# # This is truncation, NOT rounding.


# # ============================================================
# # 6. More Truncation Examples
# # ============================================================

# numbers = np.array([1.9, 2.9, 3.9], dtype=int)

# print(numbers)

# # Output:
# # [1 2 3]

# # Decimal parts are removed:
# # 1.9 -> 1
# # 2.9 -> 2
# # 3.9 -> 3


# # ============================================================
# # 7. float32 vs float64
# # ============================================================

# # float64 = 64 bits = 8 bytes per number
# # float32 = 32 bits = 4 bytes per number

# numbers_64 = np.array([10, 20, 30, 40], dtype=np.float64)
# numbers_32 = np.array([10, 20, 30, 40], dtype=np.float32)

# print(numbers_64.dtype)
# print(numbers_32.dtype)

# # Output:
# # float64
# # float32


# # ============================================================
# # 8. Checking the Number of Bytes Used by Each Element
# # ============================================================

# # itemsize tells us how many bytes each element uses

# print(numbers_64.itemsize)
# print(numbers_32.itemsize)

# # Output:
# # 8
# # 4

# # Why?
# # 64 bits / 8 = 8 bytes
# # 32 bits / 8 = 4 bytes


# # ============================================================
# # 9. Why dtype Matters in AI / ML
# # ============================================================

# # AI/ML often works with very large numerical arrays.
# # Using a smaller dtype can reduce memory usage.

# # float64 -> 8 bytes per number
# # float32 -> 4 bytes per number

# # Less memory per number can matter when working
# # with millions or billions of numerical values.


# import numpy as np
# 
# numbers = np.zeros(5, dtype=int)
# 
# print(numbers)

# import numpy as np

# numbers = np.zeros(3, dtype=int)

# print(numbers)
# print(numbers.shape)

# import numpy as np

# numbers = np.ones(4)
# print(numbers)


import numpy as np


# ============================================================
# NUMPY BRICK #3 — ARRAY CREATION
# ============================================================


# ============================================================
# 1. np.zeros()
# ============================================================

# Creates an array filled with zeros.
# 5 means we want 5 elements.
# Default dtype is float64.

numbers = np.zeros(5)

print(numbers)
print(numbers.dtype)

# Output:
# [0. 0. 0. 0. 0.]
# float64


# ============================================================
# 2. np.zeros() with an Explicit dtype
# ============================================================

# We can explicitly tell NumPy which dtype we want.

numbers = np.zeros(5, dtype=int)

print(numbers)
print(numbers.dtype)

# Output:
# [0 0 0 0 0]
# int64


# ============================================================
# 3. np.zeros() with a Shape
# ============================================================

# (3, 4) means:
# 3 rows
# 4 columns

numbers = np.zeros((3, 4))

print(numbers)
print(numbers.shape)
print(numbers.dtype)

# Output:
# [[0. 0. 0. 0.]
#  [0. 0. 0. 0.]
#  [0. 0. 0. 0.]]
#
# (3, 4)
# float64


# ============================================================
# 4. np.zeros() — 1D Array
# ============================================================

# A single number means the number of elements.
# 3 elements -> shape (3,)

numbers = np.zeros(3, dtype=int)

print(numbers)
print(numbers.shape)

# Output:
# [0 0 0]
# (3,)


# ============================================================
# 5. np.ones()
# ============================================================

# Creates an array filled with ones.
# Like zeros(), the default dtype is float64.

numbers = np.ones(5)

print(numbers)
print(numbers.dtype)

# Output:
# [1. 1. 1. 1. 1.]
# float64


# ============================================================
# 6. np.ones() with Shape and dtype
# ============================================================

# (2, 3) means:
# 2 rows
# 3 columns
#
# dtype=np.float32 means we explicitly want float32.

numbers = np.ones((2, 3), dtype=np.float32)

print(numbers)
print(numbers.shape)
print(numbers.dtype)

# Output:
# [[1. 1. 1.]
#  [1. 1. 1.]]
#
# (2, 3)
# float32


# ============================================================
# 7. np.arange()
# ============================================================

# arange() creates a sequence of numbers.
#
# arange(stop)
# starts from 0
# stop is excluded

numbers = np.arange(5)

print(numbers)

# Output:
# [0 1 2 3 4]


# ============================================================
# 8. np.arange() with Start and Stop
# ============================================================

# Start = 2
# Stop = 8 (excluded)

numbers = np.arange(2, 8)

print(numbers)

# Output:
# [2 3 4 5 6 7]


# ============================================================
# 9. np.arange() with Start, Stop and Step
# ============================================================

# Start = 1
# Stop = 10 (excluded)
# Step = 3

numbers = np.arange(1, 10, 3)

print(numbers)

# Output:
# [1 4 7]


# ============================================================
# 10. np.arange() with a Negative Step
# ============================================================

# Start = 10
# Stop = 0 (excluded)
# Step = -2

numbers = np.arange(10, 0, -2)

print(numbers)

# Output:
# [10  8  6  4  2]


# ============================================================
# 11. np.linspace()
# ============================================================

# linspace() creates equally spaced numbers.
#
# Start = 0
# Stop = 10
# Number of points = 5
#
# Unlike arange(), the stop value is included by default.

numbers = np.linspace(0, 10, 5)

print(numbers)
print(numbers.dtype)

# Output:
# [ 0.   2.5  5.   7.5 10. ]
# float64


# ============================================================
# 12. np.linspace() — Another Example
# ============================================================

# 5 equally spaced numbers between 0 and 20.

numbers = np.linspace(0, 20, 5)

print(numbers)

# Output:
# [ 0.  5. 10. 15. 20.]


# ============================================================
# 13. np.random.rand()
# ============================================================

# Generates random floating-point values.
#
# rand(5) -> 5 random values
# Values are in the range [0, 1)
#
# 0 is included.
# 1 is excluded.

numbers = np.random.rand(5)

print(numbers)
print(numbers.dtype)

# Example output:
# [0.37 0.82 0.14 0.96 0.51]
# float64
#
# The actual values will be different every run.


# ============================================================
# 14. np.random.rand() with a Shape
# ============================================================

# (2, 3) means:
# 2 rows
# 3 columns
#
# Total elements = 2 × 3 = 6

numbers = np.random.rand(2, 3)

print(numbers)
print(numbers.shape)
print(numbers.dtype)

# Example output:
# [[0.23 0.81 0.14]
#  [0.67 0.42 0.95]]
#
# (2, 3)
# float64


# ============================================================
# 15. Final Random Array Experiment
# ============================================================

# 3 rows × 4 columns
# Total values = 12
# Every value is between 0 and 1
# dtype is float64 by default.

numbers = np.random.rand(3, 4)

print(numbers)
print(numbers.shape)
print(numbers.dtype)

# Example output:
# [[0.12 0.74 0.35 0.91]
#  [0.48 0.03 0.67 0.22]
#  [0.85 0.56 0.19 0.77]]
#
# (3, 4)
# float64
#
# Actual random values will be different every run.