from acl_cffi_python.segtree.rmq.core_cffi.lib import (segtree_rmq_max_new, segtree_rmq_max_new_with_vec, 
                                                segtree_rmq_max_set, segtree_rmq_max_get, segtree_rmq_max_prod,
                                                segtree_rmq_max_max_right, segtree_rmq_max_min_left)
from acl_cffi_python.std.vector import VecLL
from typing import Optional

class RMQMax(object):
    def __init__(self, n: int = 0, vec: Optional[VecLL] = None):
        if vec:
            self.obj = segtree_rmq_max_new_with_vec(vec.obj)
        else:
            self.obj = segtree_rmq_max_new(n)
    def set(self, p: int, x: int):
        segtree_rmq_max_set(self.obj, p, x)
    def get(self, p: int) -> int:
        return segtree_rmq_max_get(self.obj, p)
    def prod(self, l: int, r: int) -> int:
        return segtree_rmq_max_prod(self.obj, l, r)
    def max_right(self, l, threshold: int) -> int:
        return segtree_rmq_max_max_right(self.obj, l, threshold)
    def min_left(self, r, threshold: int) -> int:
        return segtree_rmq_max_min_left(self.obj, r, threshold)

class RMQMin(object):
    def __init__(self, n: int = 0, vec: Optional[VecLL] = None):
        if vec:
            minus_vec = VecLL([-a for a in vec])
            self.obj = segtree_rmq_max_new_with_vec(minus_vec.obj)
        else:
            self.obj = segtree_rmq_max_new(n)
    def set(self, p: int, x: int):
        segtree_rmq_max_set(self.obj, p, - x)
    def get(self, p: int) -> int:
        return - segtree_rmq_max_get(self.obj, p)
    def prod(self, l: int, r: int) -> int:
        return - segtree_rmq_max_prod(self.obj, l, r)
    def max_right(self, l, threshold: int) -> int:
        return segtree_rmq_max_max_right(self.obj, l, - threshold)
    def min_left(self, r, threshold: int) -> int:
        return segtree_rmq_max_min_left(self.obj, r, - threshold)
