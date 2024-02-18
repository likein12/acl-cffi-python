import ctypes

libc = ctypes.cdll.LoadLibrary("./test.so")

libc.get_int_n([1,2,3],1)