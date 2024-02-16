from acl_cffi_python.fenwicktree.core_cffi.lib import fenwick_tree_ll_new, fenwick_tree_ll_add, fenwick_tree_ll_sum


class FenwickTree(object):
    def __init__(self, n: int):
        self.obj = fenwick_tree_ll_new(n)
    def add(self, p: int, x: int) -> None:
        fenwick_tree_ll_add(self.obj, p, x)
    def sum(self, l: int, r: int) -> int:
        return fenwick_tree_ll_sum(self.obj, l, r)
