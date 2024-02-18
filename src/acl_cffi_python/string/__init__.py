from acl_cffi_python.core.cffi_core.lib import (string_suffix_array_str, string_lcp_array_str)
from acl_cffi_python.static import ArrI
from acl_cffi_python.std.string import String


def SuffixArray(s: String) -> ArrI:
    return ArrI(-1, ptr=string_suffix_array_str(s.obj))

def LCPArray(s: String, sa: ArrI) -> ArrI:
    return ArrI(-1, ptr=string_lcp_array_str(s.obj, sa.obj))
