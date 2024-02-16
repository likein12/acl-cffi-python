from acl_cffi_python.mincostflow.cffi_core.lib import (mcf_graph_ll_ll_new, mcf_graph_ll_ll_add_edge, mcf_graph_ll_ll_flow, mcf_graph_ll_ll_flow_with_limit,
                                                        mcf_graph_ll_ll_edge_from, mcf_graph_ll_ll_edge_to, mcf_graph_ll_ll_edge_cap, mcf_graph_ll_ll_edge_flow, mcf_graph_ll_ll_edge_cost, mcf_graph_ll_ll_get_edge)
from acl_cffi_python.std.utility import PLL
from typing import List

class MCFEdge(object):
    def __init__(self, ptr):
        self.obj = ptr
    @property
    def frm(self):
        return mcf_graph_ll_ll_edge_from(self.obj)
    @property
    def to(self):
        return mcf_graph_ll_ll_edge_to(self.obj)
    @property
    def cap(self):
        return mcf_graph_ll_ll_edge_cap(self.obj)
    @property
    def flow(self):
        return mcf_graph_ll_ll_edge_flow(self.obj)
    @property
    def cost(self):
        return mcf_graph_ll_ll_edge_cost(self.obj)

class MCFGraph(object):
    def __init__(self, n: int):
        self.obj = mcf_graph_ll_ll_new(n)
        self.n_edges = 0
    def add_edge(self, frm: int, to: int, cap: int, cost: int) -> int:
        self.n_edges += 1
        return mcf_graph_ll_ll_add_edge(self.obj, frm, to, cap, cost)
    def flow(self, s: int, t: int) -> PLL:
        ret = mcf_graph_ll_ll_flow(self.obj, s, t)
        return PLL(ptr=self.obj)
    def flow_with_limit(self, s: int, t: int, flow_limit: int) -> PLL:
        ret = mcf_graph_ll_ll_flow_with_limit(self.obj, s, t, flow_limit)
        return PLL(ptr=self.obj)
    def get_edge(self, index: int) -> MCFEdge:
        return mcf_graph_ll_ll_get_edge(self.obj, index)
    def edges(self) -> List[MCFEdge]:
        return [self.get_edge(i) for i in range(self.n_edges)]