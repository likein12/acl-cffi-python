#ifndef CFFI_MATH_HPP
#define CFFI_MATH_HPP 1
//#include <atcoder/internal_math>
#include <atcoder/math>
#include "../std/utility/cppinterface.hpp"
#include "../static/cppinterface.hpp"

extern "C" {
    pll math_ext_gcd(long long a, long long b){
        pll ret = atcoder::internal::inv_gcd(a, b);
        long long g = ret.first;
        long long x = ret.second;
        long long y = (a*x - g)/b;
        return pll(x, y);
    }
    pll math_crt(static_arrll r, static_arrll m){
        return atcoder::crt(*r.to_vector(), *m.to_vector());
    }
    long long math_floor_sum(long long n, long long m, long long a, long long b){
        return atcoder::floor_sum(n, m, a, b);
    }

}

#endif