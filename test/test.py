from cffi_test.lib import get
import inspect

x = get()
print(x)
x.b = 30
print(x.b)
for xx in inspect.getmembers(x):
    print(xx)