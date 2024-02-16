from acl_cffi_python.twosat.cffi_core.lib import (two_sat_new, two_sat_add_clause,
                                                  two_sat_satisfiable, two_sat_answer)
from acl_cffi_python.std.vector import VecI

class TwoSat(object):
    def __init__(self, n: int):
        self.obj = two_sat_new(n)
    def add_clause(self, i: int, f: bool, j: int, g: bool):
        two_sat_add_clause(self.obj, i, f, j, g)
    def satisfiable(self) -> bool:
        return two_sat_satisfiable(self.obj) != 0
    def answer(self) -> VecI:
        return two_sat_answer(self.obj)