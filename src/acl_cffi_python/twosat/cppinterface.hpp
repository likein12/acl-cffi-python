#ifndef CFFI_TWOSAT_HPP
#define CFFI_TWOSAT_HPP 1
#include <atcoder/twosat>
#include "../std/vector/cppinterface.hpp"

extern "C" {
    using two_sat = atcoder::two_sat;
    void *two_sat_new(int n){ return new two_sat(n); }
    void two_sat_add_clause(void *obj, int i, int f, int j, int g){
        ((two_sat*)obj)->add_clause(i, f, j, g);
    }
    int two_sat_satisfiable(void *obj){ return ((two_sat*)obj)->satisfiable(); }
    void *two_sat_answer(void *obj){ 
        auto ans = ((two_sat*)obj)->answer();
        veci *ret = new veci(ans.size());
        for(int i=0;i<ans.size();++i) (*ret)[i] = ans[i];
        return ret;
    }
}

#endif