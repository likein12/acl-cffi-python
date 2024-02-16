from acl_cffi_python.segtree.rmq.core_cffi.lib import (segtree_TAG_S_new, segtree_TAG_new, segtree_TAG_new_with_vec, 
                                                segtree_TAG_set, segtree_TAG_get, segtree_TAG_prod,
                                                segtree_TAG_max_right, segtree_TAG_min_left,
                                                vec_segtree_TAG_S_new, vec_segtree_TAG_S_new_with_size, vec_segtree_TAG_S_push_back,
                                                vec_segtree_TAG_S_at, vec_segtree_TAG_S_size, vec_segtree_TAG_S_sub)
from typing import Optional
import inspect
from ctypes import _CData

segtree_TAG_S = _CData

def S(*args) -> segtree_TAG_S:
    return segtree_TAG_S_new(*args)

class vec_segtree_TAG_S(object):
    def __init__(self, L = [], ptr = None):
        if ptr:
            self.obj = ptr
        else:
            self.obj = vec_segtree_TAG_S_new()
            if L:
                for x in L:
                    self.push_back(x)
            
    def push_back(self, x: int):
        vec_segtree_TAG_S_push_back(self.obj, x)

    def __getitem__(self, index: int):
        return vec_segtree_TAG_S_at(self.obj, index)

    def __setitem__(self, index: int, item: int):
        vec_segtree_TAG_S_sub(self.obj, index, item)

    def __len__(self):
        return vec_segtree_TAG_S_size(self.obj)

    def __repr__(self) -> str:
        return "[" + ", ".join((
            "[" + ", ".join(f"{k}:{v}"for k,v in inspect.getmembers(x)) + "]"
        ) for x in self) + "]"

    def printer(self) -> str:
        return 

    def __iter__(self):
        self._now_index = -1
        return self

    def __next__(self):
        if self._now_index + 1 >= len(self): raise StopIteration
        self._now_index += 1
        return self[self._now_index]

class SegTree_TAG(object):
    def __init__(self, n: int = 0, vec: Optional[vec_segtree_TAG_S] = None):
        if vec:
            self.obj = segtree_TAG_new_with_vec(vec.obj)
        else:
            self.obj = segtree_TAG_new(n)
    def set(self, p: int, x: int):
        segtree_TAG_set(self.obj, p, x)
    def get(self, p: int) -> segtree_TAG_S:
        return segtree_TAG_get(self.obj, p)
    def prod(self, l: int, r: int) -> segtree_TAG_S:
        return segtree_TAG_prod(self.obj, l, r)
    def max_right(self, l) -> int:
        return segtree_TAG_max_right(self.obj, l)
    def min_left(self, r) -> int:
        return segtree_TAG_min_left(self.obj)

