from acl_cffi_python.string.cffi_core.lib import (string_suffix_array_str, string_suffix_array_int, string_suffix_array_int_upper,
                                            string_lcp_array_str, string_lcp_array_int, string_z_algorithm_str, string_z_algorithm_int)
from acl_cffi_python.std.vector import VecI, VecLL
from acl_cffi_python.std.string import String


def SuffixArray(s: String) -> VecI:
    return VecI(ptr=string_suffix_array_str(s.obj))

def SuffixArrayLL(v: VecLL) -> VecI:
    return VecI(ptr=string_suffix_array_int(v.obj))

def SuffixArrayUpper(v: VecI, upper: int) -> VecI:
    return VecI(ptr=string_suffix_array_int_upper(v.obj, upper))

def LCPArray(s: String, sa: VecI) -> VecI:
    return VecI(ptr=string_lcp_array_str(s.obj, sa.obj))

def LCPArrayLL(v: VecLL, sa: VecI) -> VecI:
    return VecI(ptr=string_lcp_array_int(v.obj, sa.obj))

def ZAlgorithm(s: String) -> VecI:
    return VecI(ptr=string_z_algorithm_str(s.obj))

def ZAlgorithmInt(v: VecLL) -> VecI:
    return VecI(ptr=string_z_algorithm_int(v.obj))
