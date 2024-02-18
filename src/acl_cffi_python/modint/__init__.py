from acl_cffi_python.core.cffi_core.lib import mul
# 結局、データの受け渡しをたくさんやるよりintを継承するのがよさそう
MOD = 998244353

class ModInt(int):
    def __add__(self, other):
        ret = super().__add__(other)
        if ret >= MOD:
            return ModInt(ret - MOD)
        return ModInt(ret)
    def __sub__(self, other: int):
        ret = super().__sub__(other)
        if ret < 0:
            return ModInt(ret + MOD)
        return ModInt(ret)
    def __mul__(self, other: int):
        return ModInt(super().__mul__(other) % MOD)
    def __truediv__(self, other: int):
        return (self * pow(other, MOD-2, MOD))
    def __radd__(self, other):
        return self + other
    def __rsub__(self, other: int):
        ret = super().__rsub__(other)
        if ret < 0:
            return ModInt(ret + MOD)
        return ModInt(ret)
    def __rmul__(self, other: int):
        return self * other
    def __rtruediv__(self, other: int):
        return (self**(MOD-2)) * other
    def __pow__(self, other: int):
        return ModInt(pow(int(self), other, MOD))
    def __iadd__(self, other: int):
        return self + other
    def __isub__(self, other: int):
        return self - other
    def __imul__(self, other: int):
        return self * other
    def __itruediv__(self, other: int):
        return self / other
    def __ipow__(self, other: int):
        return self ** other
    def __neg__(self):
        return MOD - self if self != 0 else 0
