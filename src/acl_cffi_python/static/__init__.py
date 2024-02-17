from acl_cffi_python.core.cffi_core.lib import (static_arri_new, static_arri_new_with_value)
from typing import Union


class BaseStaticArrayInt(object):
    def __init__(self):
        NotImplementedError
            
    def append(self, x: int):
        now_len = self.obj._now_len
        max_len = self.obj._max_len
        assert now_len < max_len
        self.obj.ptr[now_len] = x
        self.obj._now_len += 1

    def pop(self) -> int:
        now_len = self.obj._now_len
        assert now_len > 0, "empty"
        self.obj._now_len -= 1
        return self.obj.ptr[now_len - 1]

    def extend(self, other):
        now_len = self.obj._now_len
        other_len = other.obj._max_len
        assert now_len + other_len <= self.obj._max_len, "exceed max_len"
        for i in range(other_len):
            self.append(other[i])

    def __getitem__(self, index: Union[int, slice]):
        now_len = self.obj._now_len
        if type(index) == int:
            if index < 0: index = now_len + index
            assert 0 <= index < now_len, "index out of range"
            return self.obj.ptr[index]
        elif type(index) == slice:
            start = index.start
            stop = index.stop
            step = index.step
            now_len = self.obj._now_len
            if start is None: start = 0
            elif start < 0: start = now_len + start
            assert 0 <= start < now_len, "index out of range"

            if stop is None: stop = now_len
            elif stop < 0: stop = now_len + stop
            else: stop = min(stop, now_len)
            assert 0 <= stop, "index out of range"

            if step is None: step = 1
            if start < stop and step > 0:
                nxt_max_len = (stop - start + step - 1)//step
            elif start > stop and step < 0:
                nxt_max_len = (- stop + start - step - 1)//(- step)
            else:
                nxt_max_len = 0
            ret = ArrI(nxt_max_len)
            for i in range(nxt_max_len):
                ret.append(self.obj.ptr[start + step * i])
            return ret

    def __setitem__(self, index: int, item: int):
        now_len = self.obj._now_len
        if index < 0: index = now_len - index
        assert 0 <= index < now_len, "index out of range"
        self.obj.ptr[index] = item

    def __len__(self):
        return self.obj._now_len

    @property
    def now_len(self):
        return self.obj._now_len

    @property
    def max_len(self):
        return self.obj._max_len
    
    def __repr__(self) -> str:
        return "[" + ", ".join(str(x) for x in self) + "]"

    def __iter__(self):
        self._now_index = -1
        return self

    def __next__(self):
        if self._now_index + 1 >= len(self): raise StopIteration
        self._now_index += 1
        return self[self._now_index]

class ArrI(BaseStaticArrayInt):
    def __init__(self, max_len = -1, L = [], ptr = None):
        if ptr:
            self.obj = ptr
        else:
            if max_len != -1:
                self.obj = static_arri_new(max_len)
            else:
                self.obj = static_arri_new(len(L))
            if L:
                for x in L:
                    self.append(x)

class ArrLL(BaseStaticArrayInt):
    def __init__(self, max_len = -1, L = [], ptr = None):
        if ptr:
            self.obj = ptr
        else:
            if max_len != -1:
                self.obj = static_arri_new(max_len)
            else:
                self.obj = static_arri_new(len(L))
            if L:
                for x in L:
                    self.append(x)

from acl_cffi_python.core.cffi_core.lib import (mint_normalize, mint_add, mint_substract, 
                                            mint_prod, mint_div, mint_pow, mint_radd, mint_rsubstract,
                                            mint_rprod, mint_rdiv)

class ModInt(int):
    def __init__(self, _v: int):
        self = mint_normalize(_v)
    def __add__(self, other):
        return ModInt(mint_add(self, other)) 
    def __sub__(self, other: int):
        return ModInt(mint_substract(self, other))
    def __mul__(self, other: int):
        return ModInt(mint_prod(self, other)) 
    def __truediv__(self, other: int):
        return ModInt(mint_div(other, self))
    def __radd__(self, other):
        return ModInt(mint_radd(other, self)) 
    def __rsub__(self, other: int):
        return ModInt(mint_rsubstract(other, self))
    def __rmul__(self, other: int):
        return ModInt(mint_rprod(other, self)) 
    def __rtruediv__(self, other: int):
        return ModInt(mint_rdiv(mint_normalize(other), self))
    def __pow__(self, other: int):
        return ModInt(mint_pow(self, other))
    def __iadd__(self, other):
        return self + other
    def __isub__(self, other: int):
        return self - other
    def __imul__(self, other: int):
        return self * other
    def __itruediv__(self, other: int):
        return self / other
    def __ipow__(self, other: int):
        return self ** other
# 残念ながら遅かった…