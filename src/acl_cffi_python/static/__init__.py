from acl_cffi_python.core.cffi_core.lib import (static_arri_new, static_arri_new_with_value,
                                                get_static_arri_hl, get_static_arri_max_len_index,
                                                get_static_arri_now_len_index)
from typing import Union

STATIC_ARRI_HL = get_static_arri_hl()
STATIC_ARRI_MAX_LEN = get_static_arri_max_len_index()
STATIC_ARRI_NOW_LEN = get_static_arri_now_len_index()

class ArrI(object):
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

            
    def append(self, x: int):
        now_len = self.obj[STATIC_ARRI_NOW_LEN]
        max_len = self.obj[STATIC_ARRI_MAX_LEN]
        assert now_len < max_len
        self.obj[now_len + STATIC_ARRI_HL] = x
        self.obj[STATIC_ARRI_NOW_LEN] += 1

    def pop(self) -> int:
        now_len = self.obj[STATIC_ARRI_NOW_LEN]
        assert now_len > 0, "empty"
        self.obj[STATIC_ARRI_NOW_LEN] -= 1
        return self.obj[now_len - 1 + STATIC_ARRI_HL]

    def extend(self, other):
        now_len = self.obj[STATIC_ARRI_NOW_LEN]
        other_len = other.obj[STATIC_ARRI_NOW_LEN]
        assert now_len + other_len <= self.obj[STATIC_ARRI_MAX_LEN], "exceed max_len"
        for i in range(other_len):
            self.append(other[i])

    def __getitem__(self, index: Union[int, slice]):
        now_len = self.obj[STATIC_ARRI_NOW_LEN]
        if type(index) == int:
            if index < 0: index = now_len + index
            assert 0 <= index < now_len, "index out of range"
            return self.obj[index + STATIC_ARRI_HL]
        elif type(index) == slice:
            start = index.start
            stop = index.stop
            step = index.step
            now_len = self.obj[STATIC_ARRI_NOW_LEN]
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
                ret.append(self.obj[start + step * i + STATIC_ARRI_HL])
            return ret

    def __setitem__(self, index: int, item: int):
        now_len = self.obj[STATIC_ARRI_NOW_LEN]
        if index < 0: index = now_len - index
        assert 0 <= index < now_len, "index out of range"
        self.obj[index + STATIC_ARRI_HL] = item

    def __len__(self):
        return self.obj[STATIC_ARRI_NOW_LEN]

    @property
    def now_len(self):
        return self.obj[STATIC_ARRI_NOW_LEN]

    @property
    def max_len(self):
        return self.obj[STATIC_ARRI_MAX_LEN]
    
    def __repr__(self) -> str:
        return "[" + ", ".join(str(x) for x in self) + "]"

    def __iter__(self):
        self._now_index = -1
        return self

    def __next__(self):
        if self._now_index + 1 >= len(self): raise StopIteration
        self._now_index += 1
        return self[self._now_index]
