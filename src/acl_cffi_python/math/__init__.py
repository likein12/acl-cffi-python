from acl_cffi_python.math.cffi_core.lib import math_ext_gcd, math_crt, math_floor_sum
from acl_cffi_python.static import ArrLL
from acl_cffi_python.std.utility import PLL

def ExtGCD(a: int, b: int) -> PLL:
    return PLL(ptr=math_ext_gcd(a, b))

def CRT(r: ArrLL, m: ArrLL) -> PLL:
    return PLL(ptr=math_crt(r.obj, m.obj))

def FloorSum(n: int, m: int, a: int, b: int) -> int:
    return math_floor_sum(n, m, a, b)