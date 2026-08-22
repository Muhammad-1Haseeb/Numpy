# import numpy as np


# # ============================================================
# # 1. NumPy Array vs Python List
# # ============================================================

# # Python list
# numbers_list = [10, 20, 30, 40]

# # * 3 repeats the list three times
# print(numbers_list * 3)


# # NumPy array
# numbers = np.array([10, 20, 30, 40])

# # * 3 multiplies every element by 3
# print(numbers * 3)


# # ============================================================
# # 2. ndarray
# # ============================================================

# # np.array() creates a NumPy ndarray
# print(type(numbers))


# # ============================================================
# # 3. 1D Array
# # ============================================================

# numbers_1d = np.array([10, 20, 30, 40])

# # ndim tells us how many dimensions the array has
# print(numbers_1d.ndim)  # 1


# # ============================================================
# # 4. 2D Array
# # ============================================================

# numbers_2d = np.array([
#     [10, 20, 30, 40],
#     [50, 60, 70, 80]
# ])

# print(numbers_2d)
# print(numbers_2d.ndim)  # 2


# # ============================================================
# # 5. Adding More Rows Does NOT Create More Dimensions
# # ============================================================

# numbers_2d = np.array([
#     [10, 20, 30, 40],
#     [50, 60, 70, 80],
#     [90, 100, 110, 120]
# ])

# # Still 2D because we still have rows containing values
# print(numbers_2d.ndim)  # 2


# # ============================================================
# # 6. 3D Array
# # ============================================================

# # Here we add another level of nesting
# numbers_3d = np.array([
#     [
#         [1, 2, 3],
#         [4, 5, 6]
#     ],
#     [
#         [7, 8, 9],
#         [10, 11, 12]
#     ]
# ])

# print(numbers_3d)
# print(numbers_3d.ndim)  # 3


# # ============================================================
# # 7. Shape
# # ============================================================

# numbers = np.array([
#     [1, 2],
#     [3, 4],
#     [5, 6],
#     [7, 8]
# ])

# # shape tells us the size of each dimension
# # (4, 2) = 4 rows and 2 columns
# print(numbers.shape)

# # shape returns a tuple
# print(type(numbers.shape))


# # ============================================================
# # 8. 2D Indexing
# # ============================================================

# # Format:
# # numbers[row, column]

# print(numbers[2, 0])  # 5
# print(numbers[0, 1])  # 2
# print(numbers[3, 0])  # 7


# # ============================================================
# # 9. Negative Indexing
# # ============================================================

# # Negative indexes count from the end

# print(numbers[-1, -1])  # 8
# print(numbers[-3, -2])  # 3


# # ============================================================
# # 10. Slicing Rows
# # ============================================================

# # start is included, stop is excluded
# # 1:3 means rows 1 and 2

# print(numbers[1:3])

# # Output:
# # [[3 4]
# #  [5 6]]


# # ============================================================
# # 11. Slicing Rows + Selecting a Column
# # ============================================================

# # Rows 1 and 2 + column 0
# print(numbers[1:3, 0])

# # Output:
# # [3 5]


# # ============================================================
# # 12. Slicing Rows + Selecting Another Column
# # ============================================================

# # Rows 1 and 2 + column 1
# print(numbers[1:3, 1])

# # Output:
# # [4 6]


# # ============================================================
# # 13. Slicing Rows + All Columns
# # ============================================================

# # 1:3  -> rows 1 and 2
# # :    -> all columns

# print(numbers[1:3, :])

# # Output:
# # [[3 4]
# #  [5 6]]


import numpy as np


# ============================================================
# NUMPY BRICK #2 — dtype
# ============================================================


# ============================================================
# 1. Checking dtype of an Integer Array
# ============================================================

numbers = np.array([10, 20, 30, 40])

# dtype tells us the data type of the array
print(numbers.dtype)

# Output:
# int64


# ============================================================
# 2. Checking dtype of a Float Array
# ============================================================

numbers = np.array([10.5, 20.5, 30.5])

print(numbers.dtype)

# Output:
# float64


# ============================================================
# 3. Mixed Integers + Floats
# ============================================================

# NumPy needs a compatible/common dtype
# so the integers are converted to floats

mixed = np.array([1, 2, 3.5])

print(mixed)
print(mixed.dtype)

# Output:
# [1.  2.  3.5]
# float64


# ============================================================
# 4. Explicitly Choosing a dtype
# ============================================================

# We can tell NumPy which dtype we want

numbers = np.array([10, 20, 30, 40], dtype=np.float32)

print(numbers)
print(numbers.dtype)

# Output:
# [10. 20. 30. 40.]
# float32


# ============================================================
# 5. Converting Floats to Integers
# ============================================================

# dtype=int tells NumPy to convert the values to integers

numbers = np.array([1, 2, 3.5], dtype=int)

print(numbers)
print(numbers.dtype)

# Output:
# [1 2 3]
# int64

# Notice:
# 3.5 became 3.
# This is truncation, NOT rounding.


# ============================================================
# 6. More Truncation Examples
# ============================================================

numbers = np.array([1.9, 2.9, 3.9], dtype=int)

print(numbers)

# Output:
# [1 2 3]

# Decimal parts are removed:
# 1.9 -> 1
# 2.9 -> 2
# 3.9 -> 3


# ============================================================
# 7. float32 vs float64
# ============================================================

# float64 = 64 bits = 8 bytes per number
# float32 = 32 bits = 4 bytes per number

numbers_64 = np.array([10, 20, 30, 40], dtype=np.float64)
numbers_32 = np.array([10, 20, 30, 40], dtype=np.float32)

print(numbers_64.dtype)
print(numbers_32.dtype)

# Output:
# float64
# float32


# ============================================================
# 8. Checking the Number of Bytes Used by Each Element
# ============================================================

# itemsize tells us how many bytes each element uses

print(numbers_64.itemsize)
print(numbers_32.itemsize)

# Output:
# 8
# 4

# Why?
# 64 bits / 8 = 8 bytes
# 32 bits / 8 = 4 bytes


# ============================================================
# 9. Why dtype Matters in AI / ML
# ============================================================

# AI/ML often works with very large numerical arrays.
# Using a smaller dtype can reduce memory usage.

# float64 -> 8 bytes per number
# float32 -> 4 bytes per number

# Less memory per number can matter when working
# with millions or billions of numerical values.