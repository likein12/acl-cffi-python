#ifndef CFFI_CONVOLUTION_HPP
#define CFFI_CONVOLUTION_HPP 1
#include <atcoder/convolution>
#include "../std/vector/cppinterface.hpp"

extern "C"{
    using mint = atcoder::modint998244353;
    void *convolution(void *a, void *b){
        return new vecm(atcoder::convolution(*(vecm*)a, *(vecm*)b));
    }

    void *convolution_ll(void *a, void *b){
        return new vecll(atcoder::convolution_ll(*(vecll*)a, *(vecll*)b));
    }
}

#endif