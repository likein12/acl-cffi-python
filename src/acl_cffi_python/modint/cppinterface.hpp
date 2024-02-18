#ifndef CFFI_MODINT_HPP
#define CFFI_MODINT_HPP 1
#include "./montgomery.hpp"

using lmint = LazyMontgomeryModInt<998244353>;

extern "C"{
    unsigned int mul(unsigned int a, unsigned int b){ return (lmint(a) * lmint(b)).a; }
}
#endif