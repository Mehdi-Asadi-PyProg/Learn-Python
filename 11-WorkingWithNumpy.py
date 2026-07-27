# NumPy (Numerical Python) is the fundamental package for scientific computing in Python.
# It provides a high-performance multidimensional array object (ndarray) and tools for working with these arrays.
# Almost every scientific Python library (Pandas, SciPy, scikit-learn, TensorFlow, PyTorch, etc.) is built on top of NumPy.

# pip install numpy


import numpy as np
# From Python lists
a = np.array([1, 2, 3, 4])
b = np.array([[1, 2], [3, 4]])          # 2D array

# Common constructors
print(np.zeros((3, 4)))                       # 3x4 array of zeros
np.ones((2, 3), dtype=np.float32)       # 2x3 array of ones
np.full((2, 2), 7)                      # filled with a constant
np.eye(3)                               # 3x3 identity matrix
np.arange(0, 10, 2)                     # [0, 2, 4, 6, 8]
np.linspace(0, 1, 5)                    # 5 equally spaced points between 0 and 1
np.random.rand(2, 3)                    # uniform [0, 1)
np.random.randn(2, 3)                   # standard normal
np.random.randint(0, 10, size=(3, 3))   # random integers


# Array Attributes
a = np.array([[1, 2, 3], [4, 5, 6]])
print(a.shape)      # (2, 3)
a.ndim       # 2
a.dtype      # int64 (or int32 depending on platform)
a.size       # 6
a.itemsize   # bytes per element
a.nbytes     # total bytes

# Indexing, Slicing & Boolean Masking
a = np.array([[1, 2, 3],
              [4, 5, 6],
              [7, 8, 9]])

a[1, 2]          # 6
a[0:2, 1:]       # [[2, 3], [5, 6]]
a[:, 0]          # first column → [1, 4, 7]
a[a > 5]         # boolean indexing → [6, 7, 8, 9]
a[[0, 2], [1, 2]] # fancy indexing → [2, 9]


# Vectorized Operations (No Python loops!)
Pythona = np.array([1, 2, 3])
b = np.array([10, 20, 30])

a + b          # element-wise
a * 2
a ** 2
np.sin(a)
np.exp(a)
np.sqrt(a)
a + 5          # broadcasting
# Broadcasting Rules NumPy automatically expands arrays of different shapes when possible:
a = np.array([[1], [2], [3]])   # (3, 1)
b = np.array([10, 20, 30])      # (3,)
a + b                           # → (3, 3)


# Aggregation & Statistics
a = np.random.randn(1000, 5)

a.mean()
a.mean(axis=0)      # mean of each column
a.std(axis=1)
a.min(), a.max()
a.argmin(), a.argmax()
np.percentile(a, 95)
np.unique(a)

# Linear Algebra
A = np.array([[1, 2], [3, 4]])
b = np.array([5, 6])
A @ b                    # matrix-vector product (preferred)
A.dot(b)
np.linalg.inv(A)         # inverse
np.linalg.det(A)         # determinant
np.linalg.eig(A)         # eigenvalues & eigenvectors
np.linalg.solve(A, b)    # solve Ax = b


# Reshaping & Manipulation

a = np.arange(12)                       # shape (12,)
print("a:", a)
print("shape of a:", a.shape)

# --- Reshape ---
print("\nReshape to (3, 4):")
print(a.reshape(3, 4))

print("\nReshape with -1 (infer size):")
print(a.reshape(3, -1))

# --- Flatten ---
print("\nravel() → usually a view:")
print(a.ravel())

print("\nflatten() → always a copy:")
print(a.flatten())

# --- Create a second array with compatible shape ---
b = np.arange(12, 24).reshape(3, 4)     # shape (3, 4)
print("\nb:")
print(b)
print("shape of b:", b.shape)

# --- Stacking / Concatenation ---
print("\nvstack (vertical):")
print(np.vstack([a.reshape(3, 4), b]))

print("\nhstack (horizontal):")
print(np.hstack([a.reshape(3, 4), b]))

print("\nconcatenate along axis=0:")
print(np.concatenate([a.reshape(3, 4), b], axis=0))

print("\nconcatenate along axis=1:")
print(np.concatenate([a.reshape(3, 4), b], axis=1))

# --- Split ---
print("\nSplit 1D array into 3 parts:")
print(np.split(a, 3))

print("\nSplit 2D array along rows:")
print(np.split(a.reshape(3, 4), 3, axis=0))