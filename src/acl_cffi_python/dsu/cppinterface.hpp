#ifndef CFFI_DSU_HPP
#define CFFI_DSU_HPP 1
#include <atcoder/dsu>


extern "C"{
    using dsu = atcoder::dsu;
    void *dsu_new(int n){ return new dsu(n); }
    int dsu_merge(void *obj, int a, int b){ return ((dsu*)obj)->merge(a, b); }
    int dsu_same(void *obj, int a, int b){ return ((dsu*)obj)->same(a, b); }
    int dsu_leader(void *obj, int a){ return ((dsu*)obj)->leader(a); }
    int dsu_size(void *obj, int a){ return ((dsu*)obj)->size(a); }
}

#endif