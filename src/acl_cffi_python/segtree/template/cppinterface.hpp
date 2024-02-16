#ifndef CFFI_SEGTREERMQ_HPP
#define CFFI_SEGTREERMQ_HPP 1
#include <atcoder/segtree>
#include <vector>
#include "../../std/vector/cppinterface.hpp"


extern "C" {
    struct segtree_TAG_S {
        // modify
        // 下は例
        long long a; int b;
        segtree_TAG_S(long long _a, int _b) : a(_a), b(_b){}
    };

    // modifiy
    // 下は例示
    segtree_TAG_S segtree_TAG_S_new(long long a, int b){ return {a, b}; }

    segtree_TAG_S segtree_TAG_op(segtree_TAG_S a, segtree_TAG_S b) {
        // modify
    }
    segtree_TAG_S segtree_TAG_e() {
        // modify
    }

    bool segtree_TAG_judge_func(segtree_TAG_S a){
        // modify
        // max_rightやmin_leftを使わないのならそのままでもよい
        return true;
    }

    using vec_segtree_TAG_S = std::vector<segtree_TAG_S>;
    void *vec_segtree_TAG_S_new() {return new vec_segtree_TAG_S();}
    void *vec_segtree_TAG_S_new_with_size(int n) {return new vec_segtree_TAG_S(n);}
    void vec_segtree_TAG_S_push_back(void *obj, segtree_TAG_S &x) { ((vec_segtree_TAG_S*)obj)->push_back(x);}
    segtree_TAG_S vec_segtree_TAG_S_at(void *obj, int index) { return ((vec_segtree_TAG_S*)obj)->at(index);}
    int vec_segtree_TAG_S_size(void *obj) { return ((vec_segtree_TAG_S*)obj)->size();}
    void vec_segtree_TAG_S_sub(void *obj, int index, segtree_TAG_S &x) {(*((vec_segtree_TAG_S*)obj))[index] = x;}

    using segtree_TAG = atcoder::segtree<segtree_TAG_S, segtree_TAG_op, segtree_TAG_e>;
    void *segtree_TAG_new(int n){ return new segtree_TAG(n); }
    void *segtree_TAG_new_with_vec(void *obj){ return new segtree_TAG(*(vec_segtree_TAG_S*)obj);}
    void segtree_TAG_set(void *obj, int p, segtree_TAG_S x){ ((segtree_TAG*)obj)->set(p, x); }
    segtree_TAG_S segtree_TAG_get(void *obj, int p) { return ((segtree_TAG*)obj)->get(p); }
    segtree_TAG_S segtree_TAG_prod(void *obj, int l, int r) { return ((segtree_TAG*)obj)->prod(l, r); }

    int segtree_TAG_max_right(void *obj, int l){
        return ((segtree_TAG*)obj)->max_right<segtree_TAG_judge_func>(l);
    }
    int segtree_TAG_min_left(void *obj, int r){
        return ((segtree_TAG*)obj)->min_left<segtree_TAG_judge_func>(r);
    }
}

#endif