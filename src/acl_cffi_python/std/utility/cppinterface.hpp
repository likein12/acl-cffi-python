#ifndef CFFI_UTILITY_HPP
#define CFFI_UTILITY_HPP 1
#include <utility>
#include <atcoder/modint>


extern "C"{
    using pll = std::pair<long long, long long>;
    void *pll_new(long long f, long long s) {return new pll(f, s);}
    long long pll_first(void *obj) {return ((pll*)obj)->first;}
    long long pll_second(void *obj) {return ((pll*)obj)->second;}
    void pll_set_first(void *obj, long long x) {((pll*)obj)->first = x;}
    void pll_set_second(void *obj, long long x) {((pll*)obj)->second = x;}

    // for dijkstra
    using plli = std::pair<long long, int>;
    void *plli_new(long long f, int s) {return new plli(f, s);}
    long long plli_first(void *obj) {return ((plli*)obj)->first;}
    int plli_second(void *obj) {return ((plli*)obj)->second;}
    void plli_set_first(void *obj, long long x) {((plli*)obj)->first = x;}
    void plli_set_second(void *obj, int x) {((plli*)obj)->second = x;}

    using mint = atcoder::modint998244353;
    using pmint = std::pair<mint, mint>;
    void *pmint_new(long long f, long long s) {return new pmint(f, s);}
    int pmint_first(void *obj) {return ((pmint*)obj)->first.val();}
    int pmint_second(void *obj) {return ((pmint*)obj)->second.val();}
    void pmint_set_first(void *obj, long long x) {((pmint*)obj)->first = x;}
    void pmint_set_second(void *obj, long long x) {((pmint*)obj)->second = x;}
}

#endif