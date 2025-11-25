import _cython_3_1_6
from typing import Any

__reduce_cython__: _cython_3_1_6.cython_function_or_method
__setstate_cython__: _cython_3_1_6.cython_function_or_method
__test__: dict

class GetSolutionCallback(PyCallback):
    """GetSolutionCallback()"""
    def __init__(self) -> Any:
        """Initialize self.  See help(type(self)) for accurate signature."""
    def get_native_callback(self) -> Any:
        """GetSolutionCallback.get_native_callback(self)"""
    def __reduce__(self):
        """GetSolutionCallback.__reduce_cython__(self)"""

class PyCallback:
    @classmethod
    def __init__(cls, *args, **kwargs) -> None:
        """Create and return a new object.  See help(type) for accurate signature."""
    def get_numba_matrix(self, data, shape, typestr) -> Any:
        """PyCallback.get_numba_matrix(self, data, shape, typestr)"""
    def get_numpy_array(self, data, shape, typestr) -> Any:
        """PyCallback.get_numpy_array(self, data, shape, typestr)"""
    def __reduce__(self):
        """PyCallback.__reduce_cython__(self)"""
    def __reduce_cython__(self) -> Any:
        """PyCallback.__reduce_cython__(self)"""
    def __setstate_cython__(self, __pyx_state) -> Any:
        """PyCallback.__setstate_cython__(self, __pyx_state)"""

class SetSolutionCallback(PyCallback):
    """SetSolutionCallback()"""
    def __init__(self) -> Any:
        """Initialize self.  See help(type(self)) for accurate signature."""
    def get_native_callback(self) -> Any:
        """SetSolutionCallback.get_native_callback(self)"""
    def __reduce__(self):
        """SetSolutionCallback.__reduce_cython__(self)"""
