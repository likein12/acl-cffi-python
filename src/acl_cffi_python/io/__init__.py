from acl_cffi_python.core.cffi_core.lib import (scanner_ll, scanner_vecll, scanner_vecm, scanner_string,
                                                printer_ll_one, printer_array_v_ll, printer_array_h_ll, printer_array_v_m, printer_array_h_m)
# from acl_cffi_python.std.vector import VecLL, VecM
from acl_cffi_python.std.string import String
from typing import Union

def ScanLL() -> int:
    return scanner_ll()

# def ScanVecLL(n: int) -> VecLL:
#     return VecLL(ptr = scanner_vecll(n))

# def ScanVecM(n: int) -> VecM:
#     return VecM(ptr = scanner_vecm(n))

def ScanString(n: int) -> String:
    return String(scanner_string(n))

def PrintLL(x: int) -> None:
    printer_ll_one(x)

# def PrintV(vec: Union[VecLL, VecM]) -> None:
#     if type(vec) == VecLL:
#         printer_array_v_ll(vec.obj)
#     elif type(vec) == VecM:
#         printer_array_v_m(vec.obj)

# def PrintH(vec: Union[VecLL, VecM]) -> None:
#     if type(vec) == VecLL:
#         printer_array_h_ll(vec.obj)
#     elif type(vec) == VecM:
#         printer_array_h_m(vec.obj)

