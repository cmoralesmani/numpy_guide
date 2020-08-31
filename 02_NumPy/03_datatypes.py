'''
    Datatypes
    Numpy tries to guess a datatype when you create an array, but functions that
    construct arrays usuarlly also include an optional argument to explicitly
    specify the datatype.
'''

import numpy as np

x = np.array([1, 2])   # Let numpy choose the datatype
print(x.dtype)         # Prints "int64"

x = np.array([1.0, 2.0])   # Let numpy choose the datatype
print(x.dtype)             # Prints "float64"

x = np.array([1, 2], dtype=np.int64)   # Force a particular datatype
print(x.dtype)                         # Prints "int64"

'''
For more: https://numpy.org/doc/stable/reference/arrays.dtypes.html
'''