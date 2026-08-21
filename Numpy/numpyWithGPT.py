import numpy as np


# ============================================================
# 1. NumPy Array vs Python List
# ============================================================

# Python list
numbers_list = [10, 20, 30, 40]

# * 3 repeats the list three times
print(numbers_list * 3)


# NumPy array
numbers = np.array([10, 20, 30, 40])

# * 3 multiplies every element by 3
print(numbers * 3)


# ============================================================
# 2. ndarray
# ============================================================

# np.array() creates a NumPy ndarray
print(type(numbers))


# ============================================================
# 3. 1D Array
# ============================================================

numbers_1d = np.array([10, 20, 30, 40])

# ndim tells us how many dimensions the array has
print(numbers_1d.ndim)  # 1


# ============================================================
# 4. 2D Array
# ============================================================

numbers_2d = np.array([
    [10, 20, 30, 40],
    [50, 60, 70, 80]
])

print(numbers_2d)
print(numbers_2d.ndim)  # 2


# ============================================================
# 5. Adding More Rows Does NOT Create More Dimensions
# ============================================================

numbers_2d = np.array([
    [10, 20, 30, 40],
    [50, 60, 70, 80],
    [90, 100, 110, 120]
])

# Still 2D because we still have rows containing values
print(numbers_2d.ndim)  # 2


# ============================================================
# 6. 3D Array
# ============================================================

# Here we add another level of nesting
numbers_3d = np.array([
    [
        [1, 2, 3],
        [4, 5, 6]
    ],
    [
        [7, 8, 9],
        [10, 11, 12]
    ]
])

print(numbers_3d)
print(numbers_3d.ndim)  # 3


# ============================================================
# 7. Shape
# ============================================================

numbers = np.array([
    [1, 2],
    [3, 4],
    [5, 6],
    [7, 8]
])

# shape tells us the size of each dimension
# (4, 2) = 4 rows and 2 columns
print(numbers.shape)

# shape returns a tuple
print(type(numbers.shape))


# ============================================================
# 8. 2D Indexing
# ============================================================

# Format:
# numbers[row, column]

print(numbers[2, 0])  # 5
print(numbers[0, 1])  # 2
print(numbers[3, 0])  # 7


# ============================================================
# 9. Negative Indexing
# ============================================================

# Negative indexes count from the end

print(numbers[-1, -1])  # 8
print(numbers[-3, -2])  # 3


# ============================================================
# 10. Slicing Rows
# ============================================================

# start is included, stop is excluded
# 1:3 means rows 1 and 2

print(numbers[1:3])

# Output:
# [[3 4]
#  [5 6]]


# ============================================================
# 11. Slicing Rows + Selecting a Column
# ============================================================

# Rows 1 and 2 + column 0
print(numbers[1:3, 0])

# Output:
# [3 5]


# ============================================================
# 12. Slicing Rows + Selecting Another Column
# ============================================================

# Rows 1 and 2 + column 1
print(numbers[1:3, 1])

# Output:
# [4 6]


# ============================================================
# 13. Slicing Rows + All Columns
# ============================================================

# 1:3  -> rows 1 and 2
# :    -> all columns

print(numbers[1:3, :])

# Output:
# [[3 4]
#  [5 6]]