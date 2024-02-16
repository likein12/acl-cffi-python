from acl_cffi_python.std.vector.cffi_core.lib import (veci_new, veci_push_back, veci_at, veci_size, veci_sub,
                                                    vecll_new, vecll_push_back, vecll_at, vecll_size, vecll_sub,
                                                    vecm_new, vecm_push_back, vecm_at, vecm_size, vecm_sub,
                                                    vvi_get, vvi_size, vvi_size_of_i)

class VecI(object):
    def __init__(self, L = [], ptr = None):
        if ptr:
            self.obj = ptr
        else:
            self.obj = veci_new()
            if L:
                for x in L:
                    self.push_back(x)
            
    def push_back(self, x: int):
        veci_push_back(self.obj, x)

    def __getitem__(self, index: int):
        return veci_at(self.obj, index)

    def __setitem__(self, index: int, item: int):
        veci_sub(self.obj, index, item)

    def __len__(self):
        return veci_size(self.obj)

    def __repr__(self) -> str:
        return "[" + ", ".join(str(x) for x in self) + "]"

    def __iter__(self):
        self._now_index = -1
        return self

    def __next__(self):
        if self._now_index + 1 >= len(self): raise StopIteration
        self._now_index += 1
        return self[self._now_index]


class VecLL(object):
    def __init__(self, L = [], ptr = None):
        if ptr:
            self.obj = ptr
        else:
            self.obj = vecll_new()
            if L:
                for x in L:
                    self.push_back(x)
            
    def push_back(self, x: int):
        vecll_push_back(self.obj, x)

    def __getitem__(self, index: int):
        return vecll_at(self.obj, index)

    def __setitem__(self, index: int, item: int):
        vecll_sub(self.obj, index, item)

    def __len__(self):
        return vecll_size(self.obj)

    def __repr__(self) -> str:
        return "[" + ", ".join(str(x) for x in self) + "]"

    def __iter__(self):
        self._now_index = -1
        return self

    def __next__(self):
        if self._now_index + 1 >= len(self): raise StopIteration
        self._now_index += 1
        return self[self._now_index]

class VecM(object):
    def __init__(self, L = [], ptr = None):
        if ptr:
            self.obj = ptr
        else:
            self.obj = vecm_new()
            if L:
                for x in L:
                    self.push_back(x)
            
    def push_back(self, x: int):
        vecm_push_back(self.obj, x)

    def __getitem__(self, index: int):
        return vecm_at(self.obj, index)

    def __setitem__(self, index: int, item: int):
        vecm_sub(self.obj, index, item)

    def __len__(self):
        return vecm_size(self.obj)

    def __repr__(self) -> str:
        return "[" + ", ".join(str(x) for x in self) + "]"

    def __iter__(self):
        self._now_index = -1
        return self

    def __next__(self):
        if self._now_index + 1 >= len(self): raise StopIteration
        self._now_index += 1
        return self[self._now_index]


class VVI(object):
    def __init__(self, ptr):
        self.obj = ptr
    def push_back(self):
        NotImplementedError
    def sizeof(self, index: int) -> int:
        return vvi_size_of_i(self.obj, index)
    def __getitem__(self, index1: int, index2: int) -> int:
        return vvi_get(self.obj, index1, index2)
    def __setitem__(self):
        NotImplementedError
    def __len__(self) -> int:
        return vvi_size(self.obj)
    def __repr__(self) -> str:
        return "[" + ", ".join("[" + ", ".join(
            str(self[i, j]) for j in range(self.sizeof(i))
        ) + "]" for i in range(len(self))) + "]"
    def __iter__(self):
        NotImplementedError
    def __next__(self):
        NotImplementedError

if __name__ == "__main__":
    vec = VecLL([1,2,5])
    print(vec)
    vec = VecM([1,2,5])
    print(vec)
