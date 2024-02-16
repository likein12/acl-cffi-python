#ifndef CFFI_MATH_HPP
#define CFFI_MATH_HPP 1
//#include <atcoder/internal_math>
#include <atcoder/math>
#include "../std/utility/cppinterface.hpp"
#include "../std/vector/cppinterface.hpp"

extern "C" {
    // void *math_ext_gcd(long long a, long long b){
    //     pll ret = atcoder::internal::inv_gcd(a, b);
    //     long long g = ret.first;
    //     long long x = ret.second;
    //     long long y = (a*x - g)/b;
    //     return new pll(x, y);
    // }
    void *math_crt(void *r, void *m){
        return new pll(atcoder::crt(*((vecll*)r), *((vecll*)m)));
    }
    long long math_floor_sum(long long n, long long m, long long a, long long b){
        return atcoder::floor_sum(n, m, a, b);
    }

}

#endif