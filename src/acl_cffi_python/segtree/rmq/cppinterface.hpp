#ifndef CFFI_SEGTREERMQ_HPP
#define CFFI_SEGTREERMQ_HPP 1
#include <atcoder/segtree>
#include "../../std/vector/cppinterface.hpp"
#include "../../static/cppinterface.hpp"

extern "C" {
    long long segtree_rmq_max_op(long long a, long long b) { return (a>=b)?a:b;}
    long long segtree_rmq_max_e() { return std::numeric_limits<long long>::min();}
    using segtree_rmq_max = atcoder::segtree<long long, segtree_rmq_max_op, segtree_rmq_max_e>;
    void *segtree_rmq_max_new(int n){ return new segtree_rmq_max(n); }
    void *segtree_rmq_max_new_with_vec(void *obj){ return new segtree_rmq_max(*(vecll*)obj);}
    void *segtree_rmq_max_new_with_arrll(static_arrll obj){ return new segtree_rmq_max(*obj.to_vector());}
    void segtree_rmq_max_set(void *obj, int p, long long x){ ((segtree_rmq_max*)obj)->set(p, x); }
    long long segtree_rmq_max_get(void *obj, int p) { return ((segtree_rmq_max*)obj)->get(p); }
    long long segtree_rmq_max_prod(void *obj, int l, int r) { return ((segtree_rmq_max*)obj)->prod(l, r); }
    static long long segtree_rmq_max_threshold;
    bool segtree_rmq_max_judge_func(long long a){ return a < segtree_rmq_max_threshold; }
    int segtree_rmq_max_max_right(void *obj, int l, int threshold){
        segtree_rmq_max_threshold = threshold;
        return ((segtree_rmq_max*)obj)->max_right<segtree_rmq_max_judge_func>(l);
    }
    int segtree_rmq_max_min_left(void *obj, int r, int threshold){
        segtree_rmq_max_threshold = threshold;
        return ((segtree_rmq_max*)obj)->min_left<segtree_rmq_max_judge_func>(r);
    }
}

#endif