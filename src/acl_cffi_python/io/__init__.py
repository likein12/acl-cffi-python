from acl_cffi_python.core.cffi_core.lib import (scanner_ll, scanner_vecll, scanner_vecm, scanner_string,
                                                printer_ll_one, printer_array_v_ll, printer_array_h_ll, printer_array_v_m, printer_array_h_m,
                                                scanner_arrll, scanner_arrm, scanner_arrm_safe, printer_array_h_arrm, printer_string)
from acl_cffi_python.static import ArrLL, ArrM
from acl_cffi_python.std.string import String
from typing import Union

def ScanLL() -> int:
    return scanner_ll()

def ScanArrLL(n: int, max_len: int = -1) -> ArrLL:
    return ArrLL(ptr = scanner_arrll(n, n if max_len == -1 else max_len))

def ScanArrM(n: int, max_len: int = -1) -> ArrM:
    return ArrM(ptr = scanner_arrm(n, n if max_len == -1 else max_len))

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


def PrintH(vec: ArrM) -> None:
    printer_array_h_arrm(vec.obj)
