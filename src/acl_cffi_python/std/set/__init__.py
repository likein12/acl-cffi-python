from acl_cffi_python.std.set.cffi_core.lib import (
    setll_new, setll_insert, setll_find, setll_erase,
    setll_erase_val, setll_clear, setll_contain, setll_size,
    setll_begin,setll_end, setll_rbegin, setll_rend, setll_lower_bound,
    setll_upper_bound, setll_itr_deref, setll_itr_increment,
    setll_itr_decrement, setll_ritr_deref, setll_ritr_increment, setll_ritr_decrement,
    setll_itr_compare, setll_ritr_compare
)

class SetLLItr(object):
    def __init__(self, ptr):
        self.obj = ptr
    def deref(self) -> int:
        return setll_itr_deref(self.obj)
    def increment(self) -> None:
        setll_itr_increment(self.obj)
    def decrement(self) -> None:
        setll_itr_decrement(self.obj)
    def __eq__(self, rhs) -> bool:
        return setll_itr_compare(self.obj, rhs.obj) != 0

class SetLLRItr(object):
    def __init__(self, ptr):
        self.obj = ptr
    def deref(self) -> int:
        return setll_ritr_deref(self.obj)
    def increment(self) -> None:
        setll_ritr_increment(self.obj)
    def decrement(self) -> None:
        setll_ritr_decrement(self.obj)
    def __eq__(self, rhs) -> bool:
        return setll_ritr_compare(self.obj, rhs.obj) != 0

class SetLL(object):
    """
    std::setのwrapper. 挿入, 検索, 削除を, 要素数をnとしたときにO(log n)で可能.
    さらに, lower_bound, upper_boundにより, 二分探索もO(log n)でできる.
    このクラスはlong long型を扱う.
    """
    def __init__(self):
        """
        コンストラクタ. 空のstd::set<long long>を生成.計算量O(1)
        """
        self.obj = setll_new()
    def insert(self, x: int):
        setll_insert(self.obj, x)
    def find(self, x: int) -> SetLLItr:
        return SetLLItr(setll_find(self.obj, x))
    def erase(self, itr: SetLLItr):
        setll_erase(self.obj, itr)
    def erase_val(self, x: int):
        setll_erase_val(self.obj, x)
    def clear(self):
        setll_clear(self.obj)
    def size(self) -> int:
        return len(self)
    def __len__(self) -> int:
        return setll_size(self.obj)
    def lower_bound(self, x) -> SetLLItr:
        return SetLLItr(setll_lower_bound(self.obj, x))
    def upper_bound(self, x) -> SetLLItr:
        return SetLLItr(setll_upper_bound(self.obj, x))
    def begin(self) -> SetLLItr:
        return SetLLItr(setll_begin(self.obj))
    def min(self) -> int:
        return self.begin().deref()
    def rbegin(self) -> SetLLRItr:
        return SetLLRItr(setll_rbegin(self.obj))
    def max(self) -> int:
        return self.rbegin().deref()
    def end(self) -> SetLLItr:
        return SetLLItr(setll_end(self.obj))
    def rend(self) -> SetLLRItr:
        return SetLLRItr(setll_rend(self.obj))
    def contain(self, x: int) -> bool:
        return x in self
    def __contains__(self, x: int) -> bool:
        return setll_contain(self.obj, x) != 0
    def __iter__(self):
        self.now_itr = self.begin()
        return self
    def __next__(self) -> int:
        if self.now_itr == self.end(): raise StopIteration
        v = self.now_itr.deref()
        self.now_itr.increment()
        return v
    def __repr__(self) -> str:
        return "[" + ", ".join(str(v) for v in self) + "]"

from acl_cffi_python.std.set.cffi_core.lib import (
    mlsetll_new, mlsetll_insert, mlsetll_find, mlsetll_erase,
    mlsetll_erase_val_one, mlsetll_erase_val_all, mlsetll_clear, mlsetll_contain, mlsetll_size,
    mlsetll_begin,mlsetll_end, mlsetll_rbegin, mlsetll_rend, mlsetll_lower_bound,
    mlsetll_upper_bound, mlsetll_itr_deref, mlsetll_itr_increment,
    mlsetll_itr_decrement, mlsetll_ritr_deref, mlsetll_ritr_increment, mlsetll_ritr_decrement,
    mlsetll_itr_compare, mlsetll_ritr_compare, mlsetll_count
)

class MlSetLLItr(object):
    def __init__(self, ptr):
        self.obj = ptr
    def deref(self) -> int:
        return mlsetll_itr_deref(self.obj)
    def increment(self) -> None:
        mlsetll_itr_increment(self.obj)
    def decrement(self) -> None:
        mlsetll_itr_decrement(self.obj)
    def __eq__(self, rhs) -> bool:
        return mlsetll_itr_compare(self.obj, rhs.obj) != 0

class MlSetLLRItr(object):
    def __init__(self, ptr):
        self.obj = ptr
    def deref(self) -> int:
        return mlsetll_ritr_deref(self.obj)
    def increment(self) -> None:
        mlsetll_ritr_increment(self.obj)
    def decrement(self) -> None:
        mlsetll_ritr_decrement(self.obj)
    def __eq__(self, rhs) -> bool:
        return mlsetll_ritr_compare(self.obj, rhs.obj) != 0

class MlSetLL(object):
    """
    std::setのwrapper. 挿入, 検索, 削除を, 要素数をnとしたときにO(log n)で可能.
    さらに, lower_bound, upper_boundにより, 二分探索もO(log n)でできる.
    このクラスはlong long型を扱う.
    """
    def __init__(self):
        """
        コンストラクタ. 空のstd::set<long long>を生成.計算量O(1)
        """
        self.obj = mlsetll_new()
    def insert(self, x: int):
        mlsetll_insert(self.obj, x)
    def find(self, x: int) -> MlSetLLItr:
        return MlSetLLItr(mlsetll_find(self.obj, x))
    def erase(self, itr: MlSetLLItr):
        mlsetll_erase(self.obj, itr)
    def erase_val_one(self, x: int):
        mlsetll_erase_val_one(self.obj, x)
    def erase_val_all(self, x: int):
        mlsetll_erase_val_all(self.obj, x)
    def clear(self):
        mlsetll_clear(self.obj)
    def size(self) -> int:
        return len(self)
    def __len__(self) -> int:
        return mlsetll_size(self.obj)
    def lower_bound(self, x) -> MlSetLLItr:
        return MlSetLLItr(mlsetll_lower_bound(self.obj, x))
    def upper_bound(self, x) -> MlSetLLItr:
        return MlSetLLItr(mlsetll_upper_bound(self.obj, x))
    def begin(self) -> MlSetLLItr:
        return MlSetLLItr(mlsetll_begin(self.obj))
    def min(self) -> int:
        return self.begin().deref()
    def rbegin(self) -> MlSetLLRItr:
        return MlSetLLRItr(mlsetll_rbegin(self.obj))
    def max(self) -> int:
        return self.rbegin().deref()
    def end(self) -> MlSetLLItr:
        return MlSetLLItr(mlsetll_end(self.obj))
    def rend(self) -> MlSetLLRItr:
        return MlSetLLRItr(mlsetll_rend(self.obj))
    def contain(self, x: int) -> bool:
        return x in self
    def count(self, x: int) -> int:
        return self[x]
    def __getitem__(self, x: int) -> int:
        if x in self:
            mlsetll_count(x)
        else:
            return 0
    def __contains__(self, x: int) -> bool:
        return mlsetll_contain(self.obj, x) != 0
    def __iter__(self):
        self.now_itr = self.begin()
        return self
    def __next__(self) -> int:
        if self.now_itr == self.end(): raise StopIteration
        v = self.now_itr.deref()
        c = self[v]
        self.now_itr.increment()
        return v, c
    def __repr__(self) -> str:
        return "[" + ", ".join(f"{v}:{c}" for v, c in self) + "]"

if __name__ == "__main__":
    st = SetLL()
    for i in range(3,10,2):
        st.insert(i)
    v = st.begin()
    print(v, v.deref())
    v.increment()
    print(v, v.deref())
    v.increment()
    print(v, v.deref())
    v.increment()
    print(v, v.deref())
    v.increment()
    print(v == st.end())
    v.increment()
    print(v.obj)
    print(st.end().obj)
    print(st.begin() == st.begin())
    print(st)
    print(3 in st)
    print(4 in st)