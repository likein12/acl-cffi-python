#ifndef CFFI_MAXFLOW_HPP
#define CFFI_MAXFLOW_HPP 1
#include <atcoder/maxflow>


extern "C" {
    using mf_graph_ll = atcoder::mf_graph<long long>;
    void *mf_graph_ll_new(int n){ return new mf_graph_ll(n); }
    int mf_graph_ll_add_edge(void *obj, int from, int to, long long cap){ return ((mf_graph_ll*)obj)->add_edge(from, to, cap); }
    long long mf_graph_ll_flow(void *obj, int s, int t){
        return ((mf_graph_ll*)obj)->flow(s, t);
    }
    long long mf_graph_ll_flow_with_limit(void *obj, int s, int t, long long flow_limit){
        return ((mf_graph_ll*)obj)->flow(s, t, flow_limit);
    }
    using mf_graph_ll_edge = atcoder::mf_graph<long long>::edge;
    int mf_graph_ll_edge_from(void *obj) { return ((mf_graph_ll_edge*)obj)->from;}
    int mf_graph_ll_edge_to(void *obj) { return ((mf_graph_ll_edge*)obj)->to;}
    long long mf_graph_ll_edge_cap(void *obj) { return ((mf_graph_ll_edge*)obj)->cap;}
    long long mf_graph_ll_edge_flow(void *obj) { return ((mf_graph_ll_edge*)obj)->flow;}

    void *mf_graph_ll_get_edge(void *obj, int i) { return new mf_graph_ll_edge(((mf_graph_ll*)obj)->get_edge(i)); }
    // edges()は作らなくてよいと判断, Python側でiterationを回して取得してもそこまでロスじゃないはず
    void mf_graph_ll_change_edge(void *obj, int i, long long new_cap, long long new_flow){
        ((mf_graph_ll*)obj)->change_edge(i, new_cap, new_flow);
    }
}

#endif