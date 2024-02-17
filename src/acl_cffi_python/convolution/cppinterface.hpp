#ifndef CFFI_CONVOLUTION_HPP
#define CFFI_CONVOLUTION_HPP 1
#include <atcoder/convolution>
#include <vector>
#include "../static/cppinterface.hpp"

extern "C"{
    using mint = atcoder::modint998244353;
    static_arrll convolution(static_arrll a, static_arrll b){
        auto ret = atcoder::convolution(*a.to_other_vector(), *b.to_other_vector());
        return static_arri(ret, ret.size());
    }

    static_arrll convolution_ll(static_arrll a, static_arrll b){
        auto ret = atcoder::convolution_ll(*a.to_vector(), *b.to_vector());
        return static_arrll(ret, ret.size());
    }
}

#endif