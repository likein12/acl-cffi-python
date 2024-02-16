#ifndef CFFI_STRING_HPP
#define CFFI_STRING_HPP 1
#include <atcoder/string>
#include "../std/vector/cppinterface.hpp"
#include "../std/string/cppinterface.hpp"

extern "C" {
    void *string_suffix_array_str(void *s){ return new veci(atcoder::suffix_array(*(string*)s)); }
    void *string_suffix_array_int(void *v){ return new veci(atcoder::suffix_array(*(vecll*)v)); }
    void *string_suffix_array_int_upper(void *v, int upper){ return new veci(atcoder::suffix_array(*(veci*)v, upper)); }

    void *string_lcp_array_str(void *s, void *sa){
        return new veci(atcoder::lcp_array(*(string*)s, *(veci*)sa));
    }
    void *string_lcp_array_int(void *v, void *sa){
        return new veci(atcoder::lcp_array(*(vecll*)v, *(veci*)sa));
    }

    void *string_z_algorithm_str(void *s){
        return new veci(atcoder::z_algorithm(*(string*)s));
    }
    void *string_z_algorithm_int(void *v){
        return new veci(atcoder::z_algorithm(*(vecll*)v));
    }
}

#endif