#ifndef CFFI_STRING_HPP
#define CFFI_STRING_HPP 1
#include <atcoder/string>
#include "../std/string/cppinterface.hpp"
#include "../static/cppinterface.hpp"

extern "C" {
    // 長さ変更不可とする
    int *string_suffix_array_str(void *s){
         std::vector<int> temp = atcoder::suffix_array(*(string*)s);
         int *ret = static_arri_new_with_vector(temp, temp.size());
         return ret;
    }

    int *string_lcp_array_str(void *s, int *sa){
         std::vector<int> temp = atcoder::lcp_array(*(string*)s, *static_arri_to_vector(sa));
         int *ret = static_arri_new_with_vector(temp, temp.size());
         return ret;
    }

}

#endif