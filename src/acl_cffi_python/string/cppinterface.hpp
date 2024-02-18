#ifndef CFFI_STRING_HPP
#define CFFI_STRING_HPP 1
#include <atcoder/string>
#include "../std/string/cppinterface.hpp"
#include "../static/cppinterface.hpp"

extern "C" {
    // 長さ変更不可とする
    static_arri string_suffix_array_str(void *s){
         std::vector<int> temp = atcoder::suffix_array(*(string*)s);
         static_arri ret = static_arri(temp, temp.size());
         return ret;
    }

    static_arri string_lcp_array_str(void *s, static_arri sa){
         std::vector<int> temp = atcoder::lcp_array(*(string*)s, *sa.to_vector());
         static_arri ret = static_arri(temp, temp.size());
         return ret;
    }

}

#endif