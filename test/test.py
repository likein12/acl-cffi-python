from cffi_test.lib import get
import inspect

x = get()
print(x)
x.b = 30
print(x.b)
for xx in inspect.getmembers(x):
    print(xx)

from cffi_test.lib import setll_new, setll_insert, setll_find


s = setll_new()
setll_insert(s, 4)
print(setll_find(s, 4))