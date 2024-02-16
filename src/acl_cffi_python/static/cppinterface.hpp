#ifndef CFFI_STATIC_ARRAY_HPP
#define CFFI_STATIC_ARRAY_HPP 1
#include <cassert>
#include <vector>

constexpr int __STATIC_ARRAY_SIZE = 3e7;
static int __static_arri[__STATIC_ARRAY_SIZE];
static int *__static_arri_end_ptr = __static_arri + __STATIC_ARRAY_SIZE;
static int *__static_arri_ptr = __static_arri;

// header length
constexpr int __STATIC_ARRI_HL = 2;
constexpr int __STATIC_ARRI_MAX_LEN_INDEX = 0;
constexpr int __STATIC_ARRI_NOW_LEN_INDEX = 1;

extern "C"{
    // max_lenを0番目、now_lenを1番目に配置
    // charなどを扱うときには、4文字分で確保する？
    int *static_arri_new(int max_len) {
        assert(__static_arri_ptr + max_len + __STATIC_ARRI_HL < __static_arri_end_ptr);
        int *ret = __static_arri_ptr;
        ret[__STATIC_ARRI_MAX_LEN_INDEX] = max_len;
        ret[__STATIC_ARRI_NOW_LEN_INDEX] = 0;
        __static_arri_ptr += max_len + __STATIC_ARRI_HL;
        return ret;
    }

    int *static_arri_new_with_value(int n, int x, int sz){
        assert(n <= sz);
        int *ret = static_arri_new(sz);
        for (int i = 0;i < n; ++i) ret[i+__STATIC_ARRI_HL] = x;
        return ret;        
    }

    void static_arri_push_back(int *obj, int x){
        int now_len = obj[__STATIC_ARRI_NOW_LEN_INDEX];
        int max_len = obj[__STATIC_ARRI_MAX_LEN_INDEX];
        assert(now_len <= max_len);
        obj[now_len+__STATIC_ARRI_HL] = x;
        ++obj[__STATIC_ARRI_NOW_LEN_INDEX];
    }

    int static_arri_at(int *obj, int index){
        int now_len = obj[__STATIC_ARRI_NOW_LEN_INDEX];
        assert(index < now_len);
        return obj[index+__STATIC_ARRI_HL];
    }

    void static_arri_sub(int *obj, int index, int x){
        int now_len = obj[__STATIC_ARRI_NOW_LEN_INDEX];
        assert(index < now_len);
        obj[index+__STATIC_ARRI_HL] = x;
    }
    int static_arri_max_len(int *obj){ return obj[__STATIC_ARRI_MAX_LEN_INDEX]; }
    int static_arri_now_len(int *obj){ return obj[__STATIC_ARRI_NOW_LEN_INDEX]; }
}

int *static_arri_new_with_vector(std::vector<int> &v, int sz){
    assert(v.size() <= sz);
    int *ret = static_arri_new(sz);
    for (int i = 0;i < v.size(); ++i) static_arri_push_back(ret, v[i]);
    return ret;        
}

std::vector<int> *static_arri_to_vector(int *obj){
    std::vector<int> *ret = new std::vector<int>(static_arri_now_len(obj));
    for(int i = 0;i<ret->size();++i) ret->at(i) = static_arri_at(obj, i);
    return ret;
}

#endif