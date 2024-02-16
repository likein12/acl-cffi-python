#ifndef CFFI_VECTOR_HPP
#define CFFI_VECTOR_HPP 1
#include <vector>
#include <atcoder/modint>


extern "C"{
    using veci = std::vector<int>;
    void *veci_new() {return new veci();}
    void veci_push_back(void *obj, int x) { ((veci*)obj)->push_back(x);}
    int veci_at(void *obj, int index) { return ((veci*)obj)->at(index);}
    int veci_size(void *obj) { return ((veci*)obj)->size();}
    void veci_sub(void *obj, int index, int x) {(*((veci*)obj))[index] = x;}

    using vecll = std::vector<long long>;
    void *vecll_new() {return new vecll();}
    void vecll_push_back(void *obj, long long x) { ((vecll*)obj)->push_back(x);}
    long long vecll_at(void *obj, int index) { return ((vecll*)obj)->at(index);}
    int vecll_size(void *obj) { return ((vecll*)obj)->size();}
    void vecll_sub(void *obj, int index, long long x) {(*((vecll*)obj))[index] = x;}

    using mint = atcoder::modint998244353;
    using vecm = std::vector<mint>;
    void *vecm_new() {return new vecm();}
    void vecm_push_back(void *obj, long long x) { ((vecm*)obj)->push_back(x);}
    int vecm_at(void *obj, int index) { return ((vecm*)obj)->at(index).val();}
    int vecm_size(void *obj) { return ((vecm*)obj)->size();}
    void vecm_sub(void *obj, int index, long long x) {(*((vecm*)obj))[index] = x;}

    using vvi = std::vector<std::vector<int>>;
    int vvi_get(void *obj, int index1, int index2) { return ((vvi*)obj)->at(index1).at(index2); }
    int vvi_size(void *obj) { return ((vvi*)obj)->size(); }
    int vvi_size_of_i(void *obj, int index) { return ((vvi*)obj)->at(index).size(); }
}

#endif