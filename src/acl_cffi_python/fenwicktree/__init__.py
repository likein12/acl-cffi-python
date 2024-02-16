"""
Fenwick Tree
"""

from acl_cffi_python.fenwicktree.cffi_core.lib import fenwick_tree_ll_new, fenwick_tree_ll_add, fenwick_tree_ll_sum


class FenwickTree(object):
    """
    Fenwick Tree。あるいはBIT (Binary Indexed Tree)。
    区間和と一点加算がそれぞれO(log n)で可能。
    足し算以外にもアーベル群なら載る。
    """
    def __init__(self, n: int):
        """
        コンストラクタ。区間の長さnのFenwick Treeを構築。O(n)

        Args:
            n (int):区間長
        """
        self.obj = fenwick_tree_ll_new(n)
    def add(self, p: int, x: int) -> None:
        """
        位置pにx加算。O(log n)

        Args:
            p (int): 位置、0からn-1の間
            x (int): 加算する値
        """
        fenwick_tree_ll_add(self.obj, p, x)
    def sum(self, l: int, r: int) -> int:
        """
        半開区間[l,r)の和を取得。O(log n)

        Args:
            l (int): 左端
            r (int): 右端（半開区間なので含まれないことに注意）
        
        Results:
            半開区間[l,r)
        """
        return fenwick_tree_ll_sum(self.obj, l, r)
