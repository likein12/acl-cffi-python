from acl_cffi_python.scc.cffi_core import scc_graph_new, scc_graph_add_edge, scc_graph_scc
from acl_cffi_python.std.vector import VVI

class SCCGraph(object):
    def __init__(self, n: int):
        self.obj = scc_graph_new(n)
    def add_edge(self, a: int, b: int) -> None:
        scc_graph_add_edge(self.obj, a, b)
    def scc(self) -> VVI:
        return VVI(scc_graph_scc(self.obj))