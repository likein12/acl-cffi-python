#ifndef CFFI_FENWICKTREE_HPP
#define CFFI_FENWICKTREE_HPP 1
#include <atcoder/fenwicktree>


extern "C" {
    using fenwick_tree_ll = atcoder::fenwick_tree<long long>;
    void *fenwick_tree_ll_new(int n){ return new fenwick_tree_ll(n); }
    void fenwick_tree_ll_add(void *obj, int p, long long x){ ((fenwick_tree_ll*)obj)->add(p, x); }
    long long fenwick_tree_ll_sum(void *obj, int l, int r){ return ((fenwick_tree_ll*)obj)->sum(l, r);}
}

#endif