from acl_cffi_python.core.cffi_core.lib import (wstree_new, wstree_new_with_string, wstree_insert, wstree_erase, wstree_count,
                                            wstree_no_less_than, wstree_no_greater_than)

class WordsizeTree(object):
    def __init__(self, length = 0, string = None) -> None:
        if string:
            self.obj = wstree_new_with_string(string)
        else:
            self.obj = wstree_new(length)
    def insert(self, x: int):
        wstree_insert(self.obj, x)
    def erase(self, x: int):
        wstree_erase(self.obj, x)
    def count(self, x: int) -> int:
        return wstree_count(self.obj, x)
    def noLessThan(self, x: int) -> int:
        return wstree_no_less_than(self.obj, x)
    def noGreaterThan(self, x:int) -> int:
        return wstree_no_greater_than(self.obj, x)