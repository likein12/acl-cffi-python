from acl_cffi_python.core.cffi_core.lib import (mf_graph_ll_new, mf_graph_ll_add_edge, mf_graph_ll_flow, mf_graph_ll_flow_with_limit,
                                                mf_graph_ll_get_edge, mf_graph_ll_change_edge)
from typing import List


class MFEdge(object):
    def __init__(self, ptr):
        self.obj = ptr
    @property
    def frm(self):
        return self.obj.frm
    @property
    def to(self):
        return self.obj.to
    @property
    def cap(self):
        return self.obj.cap
    @property
    def flow(self):
        return self.obj.flow


class MFGraph(object):
    def __init__(self, n: int):
        self.obj = mf_graph_ll_new(n)
        self.n_edges = 0
    def add_edge(self, frm: int, to: int, cap: int) -> int:
        self.n_edges += 1
        return mf_graph_ll_add_edge(self.obj, frm, to, cap)
    def flow(self, s: int, t: int) -> int:
        return mf_graph_ll_flow(self.obj, s, t)
    def flow_with_limit(self, s: int, t: int, flow_limit: int) -> int:
        return mf_graph_ll_flow_with_limit(self.obj, s, t, flow_limit)
    def get_edge(self, index: int) -> MFEdge:
        return MFEdge(mf_graph_ll_get_edge(self.obj, index))
    def edges(self) -> List[MFEdge]:
        return [self.get_edge(i) for i in range(self.n_edges)]
    def change_edge(self, index: int, new_cap: int, new_flow: int) -> None:
        mf_graph_ll_change_edge(self.obj, index, new_cap, new_flow)
