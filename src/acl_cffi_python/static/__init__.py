from acl_cffi_python.core.cffi_core.lib import (static_arri_new, static_arri_new_with_value,
                                                static_arrll_new, static_arrll_new_with_value,
                                                static_arrui_new, static_arrui_new_with_value)
from acl_cffi_python.modint import MOD, ModInt
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
    def slice_helper(self, index: slice, cls):
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
        ret = cls(nxt_max_len)
        for i in range(nxt_max_len):
            ret.append(self.obj.ptr[start + step * i])
        return ret

    def __getitem__(self, index: Union[int, slice]):
        NotImplementedError

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
    def __getitem__(self, index: Union[int, slice]):
        now_len = self.obj._now_len
        if type(index) == int:
            if index < 0: index = now_len + index
            assert 0 <= index < now_len, "index out of range"
            return self.obj.ptr[index]
        elif type(index) == slice:
            return self.slice_helper(index, ArrI)

class ArrLL(BaseStaticArrayInt):
    def __init__(self, max_len = -1, L = [], ptr = None):
        if ptr:
            self.obj = ptr
        else:
            if max_len != -1:
                self.obj = static_arrll_new(max_len)
            else:
                self.obj = static_arrll_new(len(L))
            if L:
                for x in L:
                    self.append(x)

    def __getitem__(self, index: Union[int, slice]):
        now_len = self.obj._now_len
        if type(index) == int:
            if index < 0: index = now_len + index
            assert 0 <= index < now_len, "index out of range"
            return self.obj.ptr[index]
        elif type(index) == slice:
            return self.slice_helper(index, ArrLL)



class ArrM(BaseStaticArrayInt):
    def __init__(self, max_len = -1, L = [], ptr = None):
        if ptr:
            self.obj = ptr
        else:
            if max_len != -1:
                self.obj = static_arrui_new(max_len)
            else:
                self.obj = static_arrui_new(len(L))
            if L:
                for x in L:
                    self.append(x)
    def append(self, x: int):
        self.obj.ptr[self.now_len] = x % MOD
        self.obj._now_len += 1
    def __getitem__(self, index: Union[int, slice]):
        return self.obj.ptr[index]
        # now_len = self.obj._now_len
        # if type(index) == int:
        #     if index < 0: index = now_len + index
        #     assert 0 <= index < now_len, "index out of range"
        #     return self.obj.ptr[index]
        # elif type(index) == slice:
        #    return self.slice_helper(index, ArrM)
    def __setitem__(self, index: int, item: int):
        self.obj.ptr[index] = item % MOD
    # def __setitem__(self, index: int, item: int):
    #     return super().__setitem__(index, item % MOD)

class ArrUI(BaseStaticArrayInt):
    def __init__(self, max_len = -1, L = [], ptr = None):
        if ptr:
            self.obj = ptr
        else:
            if max_len != -1:
                self.obj = static_arrui_new(max_len)
            else:
                self.obj = static_arrui_new(len(L))
            if L:
                for x in L:
                    self.append(x)
    def append(self, x: int):
        self.obj.ptr[self.now_len] = x
        self.obj._now_len += 1
    def __getitem__(self, index: Union[int, slice]):
        return self.obj.ptr[index]
    def __setitem__(self, index: int, item: int):
        self.obj.ptr[index] = item


class Mimic:
    def __init__(self, L, max_len, now_len) -> None:
        self.ptr = L
        self._max_len = max_len
        self._now_len = now_len

class SString(bytes):
    def __init__(self, max_len = -1, L = [], ptr = None):
        if ptr:
            self.obj = ptr
        else:
            if max_len != -1:
                self.obj = static_arrui_new(max_len)
            else:
                self.obj = static_arrui_new(len(L))
            if L:
                for x in L:
                    self.append(x)
    def append(self, x: int):
        super().append(x % MOD)
    def __getitem__(self, index: Union[int, slice]):
        now_len = self.obj._now_len
        if type(index) == int:
            if index < 0: index = now_len + index
            assert 0 <= index < now_len, "index out of range"
            return ModInt(self.obj.ptr[index])
        elif type(index) == slice:
            return self.slice_helper(index, ArrM)

    def __setitem__(self, index: int, item: int):
        return super().__setitem__(index, item % MOD)
    