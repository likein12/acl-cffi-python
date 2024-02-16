from acl_cffi_python.core.cffi_core.lib import (static_arri_new, static_arri_new_with_value,
                                               static_arri_push_back, static_arri_at, static_arri_sub,
                                               static_arri_max_len, static_arri_now_len)


class ArrI(object):
    def __init__(self, max_len, L = [], ptr = None):
        if ptr:
            self.obj = ptr
        else:
            self.obj = static_arri_new(max_len)
            if L:
                for x in L:
                    self.push_back(x)

            
    def push_back(self, x: int):
        static_arri_push_back(self.obj, x)

    def __getitem__(self, index: int):
        return static_arri_at(self.obj, index)

    def __setitem__(self, index: int, item: int):
        static_arri_sub(self.obj, index, item)

    def __len__(self):
        return static_arri_now_len(self.obj)

    @property
    def now_len(self):
        return static_arri_now_len(self.obj)

    @property
    def max_len(self):
        return static_arri_max_len(self.obj)
    
    def __repr__(self) -> str:
        return "[" + ", ".join(str(x) for x in self) + "]"

    def __iter__(self):
        self._now_index = -1
        return self

    def __next__(self):
        if self._now_index + 1 >= len(self): raise StopIteration
        self._now_index += 1
        return self[self._now_index]
