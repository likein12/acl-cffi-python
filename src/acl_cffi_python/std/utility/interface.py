from acl_cffi_python.std.utility.cffi_core import (pll_new, pll_first, pll_second, pll_set_first, pll_set_second,
                                                    plli_new, plli_first, plli_second, plli_set_first, plli_set_second,
                                                    pmint_new, pmint_first, pmint_second, pmint_set_first, pmint_set_second)

class PLL(object):
    def __init__(self, f: int = 0, s: int = 0, ptr = None):
        if ptr:
            self.obj = ptr
        else:
            self.obj = pll_new(f, s)
    def __getitem__(self, index: int) -> int:
        if index == 0:
            return pll_first(self.obj)
        elif index == 1:
            return pll_second(self.obj)
        else:
            raise IndexError("Index must be 0 or 1.")
    def __setitem__(self, index: int, x: int) -> None:
        if index == 0:
            return pll_set_first(self.obj, x)
        elif index == 1:
            return pll_set_second(self.obj, x)
        else:
            raise IndexError("Index must be 0 or 1.")
        
class PMint(object):
    def __init__(self, f: int, s: int):
        self.obj = pmint_new(f, s)
    def __getitem__(self, index: int) -> int:
        if index == 0:
            return pmint_first(self.obj)
        elif index == 1:
            return pmint_second(self.obj)
        else:
            raise IndexError("Index must be 0 or 1.")
    def __setitem__(self, index: int, x: int) -> None:
        if index == 0:
            return pmint_set_first(self.obj, x)
        elif index == 1:
            return pmint_set_second(self.obj, x)
        else:
            raise IndexError("Index must be 0 or 1.")
        