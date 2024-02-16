"""
Disjoint Set Union
"""
from acl_cffi_python.dsu.cffi_core.lib import dsu_new, dsu_merge, dsu_same, dsu_leader, dsu_size


class DSU(object):
    """
    Disjoint Set Union, UnionFindとも。
    グラフのサイズをnとし、辺の追加や、連結性の判定をならしO(α(n))で行える。
    """

    def __init__(self, n: int):
        """
        コンストラクタ。O(n)

        Args:
            n: int: 頂点数
        """
        self.obj = dsu_new(n)
    def merge(self, a: int, b: int) -> int:
        """
        二つの頂点aとbの間に辺を追加する。
        ならしO(α(n))
        
        Args:
            a: int: 頂点番号
            b: int: 頂点番号
        
        Returns:
            aとbが連結だった場合はその代表元、
            非連結だった場合は、連結したのちに新たな代表元を返す
        """
        return dsu_merge(self.obj, a, b)
    def same(self, a: int, b: int) -> bool:
        """
        二つの頂点aとbが同じ連結成分に属するか判定。
        ならしO(α(n))
        
        Args:
            a: int: 頂点番号
            b: int: 頂点番号
        
        Returns:
            aとbが連結だった場合はTrue、そうでなければFalse
        """
        return dsu_same(self.obj, a, b) != 0
    def leader(self, a: int) -> int:
        """
        頂点aが属する連結成分の代表元を返す。
        ならしO(α(n))
        
        Args:
            a: int: 頂点番号
        
        Returns:
            頂点aが属する連結成分の代表元
        """
        return dsu_leader(self.obj, a)
    def size(self, a: int) -> int:
        """
        頂点aが属する連結成分のサイズを返す。
        ならしO(α(n))

        Args:
            a: int: 頂点番号
        
        Returns:
            頂点aが属する連結成分のサイズ
        """
        return dsu_size(self.obj, a)

if __name__ == "__main__":
    dsu = DSU(10)
    dsu.merge(1,2)
    print(dsu.same(1,2))
    print(dsu.same(2,3))
    print(dsu.size(2))