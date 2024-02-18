from acl_cffi_python.core.cffi_core.lib import (segtree_rmq_max_new, segtree_rmq_max_new_with_arrll, 
                                                segtree_rmq_max_set, segtree_rmq_max_get, segtree_rmq_max_prod,
                                                segtree_rmq_max_max_right, segtree_rmq_max_min_left)
from acl_cffi_python.std.vector import VecLL
from acl_cffi_python.static import ArrLL
from typing import Optional

class RMQMax(object):
    def __init__(self, n: int = 0, arr: Optional[ArrLL] = None):
        if arr:
            self.obj = segtree_rmq_max_new_with_arrll(vec.obj)
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

    def __init__(self, n: int = 0, arr: Optional[ArrLL] = None):
        if arr:
            minus_arr = VecLL([-a for a in arr])
            self.obj = segtree_rmq_max_new_with_arrll(minus_arr.obj)
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
