#ifndef CFFI_MINCOSTFLOW_HPP
#define CFFI_MINCOSTFLOW_HPP 1
#include <atcoder/mincostflow>
#include "../std/utility/cppinterface.hpp"

extern "C" {
    using mcf_graph_ll_ll = atcoder::mcf_graph<long long, long long>;
    void *mcf_graph_ll_ll_new(int n){ return new mcf_graph_ll_ll(n); }
    int mcf_graph_ll_ll_add_edge(void *obj, int from, int to, long long cap, long long cost){ return ((mcf_graph_ll_ll*)obj)->add_edge(from, to, cap, cost); }
    void *mcf_graph_ll_ll_flow(void *obj, int s, int t){
        return new pll(((mcf_graph_ll_ll*)obj)->flow(s, t));
    }
    void *mcf_graph_ll_ll_flow_with_limit(void *obj, int s, int t, long long flow_limit){
        return new pll(((mcf_graph_ll_ll*)obj)->flow(s, t, flow_limit));
    }

    using mcf_graph_ll_ll_edge = atcoder::mcf_graph<long long, long long>::edge;

    int mcf_graph_ll_ll_edge_from(void *obj) {return ((mcf_graph_ll_ll_edge*)obj)->from;}
    int mcf_graph_ll_ll_edge_to(void *obj) {return ((mcf_graph_ll_ll_edge*)obj)->to;}
    int mcf_graph_ll_ll_edge_cap(void *obj) {return ((mcf_graph_ll_ll_edge*)obj)->cap;}
    int mcf_graph_ll_ll_edge_flow(void *obj) {return ((mcf_graph_ll_ll_edge*)obj)->flow;}
    int mcf_graph_ll_ll_edge_cost(void *obj) {return ((mcf_graph_ll_ll_edge*)obj)->cost;}

    void *mcf_graph_ll_ll_get_edge(void *obj, int i) {return new mcf_graph_ll_ll_edge(((mcf_graph_ll_ll*)obj)->get_edge(i));}
    // edges()は作らなくてよいと判断, Python側でiterationを回して取得してもそこまでロスじゃないはず
}

#endif