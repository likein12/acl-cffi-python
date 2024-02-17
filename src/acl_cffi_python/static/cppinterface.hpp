#ifndef CFFI_STATIC_ARRAY_HPP
#define CFFI_STATIC_ARRAY_HPP 1
#include <cassert>
#include <vector>
#include <atcoder/modint>

constexpr int __STATIC_ARRAY_SIZE = 2e8;

static int __static_arri[__STATIC_ARRAY_SIZE];
static int *__static_arri_end_ptr = __static_arri + __STATIC_ARRAY_SIZE;
static int *__static_arri_ptr = __static_arri;

static long long __static_arrll[__STATIC_ARRAY_SIZE];
static long long *__static_arrll_end_ptr = __static_arrll + __STATIC_ARRAY_SIZE;
static long long *__static_arrll_ptr = __static_arrll;

template<typename T, T **now_limit_ptr, T **end_ptr>
struct static_array {
    T *ptr;
    int _max_len;
    int _now_len;
    static_array(int max_len) {
        assert(*now_limit_ptr + max_len < *end_ptr);
        ptr = *now_limit_ptr;
        *now_limit_ptr += max_len;
        _max_len = max_len;
        _now_len = 0;
    }

    static_array(int n, T x, int max_len){
        assert(n <= max_len);
        assert(*now_limit_ptr + max_len < *end_ptr);
        ptr = *now_limit_ptr;
        *now_limit_ptr += max_len;
        for (int i = 0;i < n; ++i) ptr[i] = x;
        _max_len = max_len;
        _now_len = n;
    }

    static_array(std::vector<T> &v, int max_len){
        assert(v.size() <= max_len);
        assert(*now_limit_ptr + max_len < *end_ptr);
        ptr = *now_limit_ptr;
        *now_limit_ptr += max_len;
        for (int i = 0;i < v.size(); ++i) ptr[i] = v[i];
        _max_len = max_len;
        _now_len = v.size();
    }

    void push_back(T x){
        assert(_now_len <= _max_len);
        ptr[_now_len] = x;
        ++_now_len;
    }

    T pop_back(){
        assert(_now_len > 0);
        --_now_len;
        return ptr[_now_len];
    }

    int get_now_len() { return _now_len; }
    int get_max_len() { return _max_len; }

    std::vector<T> *to_vector(){
        std::vector<int> *ret = new std::vector<T>(get_now_len());
        for(int i = 0;i<ret->size();++i) ret->at(i) = ptr[i];
        return ret;
    }
};

using uint = unsigned int;

extern "C"{
    using mint = atcoder::modint998244353;
    
    uint mint_normalize(long long a){ return mint(a).val(); }
    uint mint_add(uint a, long long b){ return (mint(a) + mint(b)).val(); }
    uint mint_substract(uint a, long long b){ return (mint(a) - mint(b)).val(); }
    uint mint_prod(uint a, long long b){ return (mint(a) * mint(b)).val(); }
    uint mint_div(uint a, long long b){ return (mint(a) * mint(b).inv()).val(); }
    uint mint_pow(uint a, long long b){
        if (b >= 0) return (mint(a).pow(b)).val();
        else return (mint(a).inv().pow(-b)).val();
    }
    uint mint_radd(long long a, uint b){ return (mint(a) + mint(b)).val(); }
    uint mint_rsubstract(long long a, uint b){ return (mint(a) - mint(b)).val(); }
    uint mint_rprod(long long a, uint b){ return (mint(a) * mint(b)).val(); }
    uint mint_rdiv(long long a, uint b){ return (mint(a) * mint(b).inv()).val(); }
    
    using static_arri = static_array<int, &__static_arri_ptr, &__static_arri_end_ptr>;
    static_arri static_arri_new(int max_len){ return static_arri(max_len); }
    static_arri static_arri_new_with_value(int n, int x, int max_len){ return static_arri(n, x, max_len); }
    
    using static_arrll = static_array<long long, &__static_arrll_ptr, &__static_arrll_end_ptr>;
    static_arrll static_arrll_new(int max_len){ return static_arrll(max_len); }
    static_arrll static_arrll_new_with_value(int n, int x, int max_len){ return static_arrll(n, x, max_len); }
}

#endif