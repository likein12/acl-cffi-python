#ifndef CFFI_SCC_HPP
#define CFFI_SCC_HPP 1
#include <atcoder/scc>
#include "../std/vector/cppinterface.hpp"

extern "C" {
    using scc_graph = atcoder::scc_graph;
    void *scc_graph_new(int n){ return new scc_graph(n); }
    void scc_graph_add_edge(void *obj, int from, int to){ ((scc_graph*)obj)->add_edge(from, to); }
    void *scc_graph_scc(void *obj) { return new vvi(((scc_graph*)obj)->scc()); }
}

#endif