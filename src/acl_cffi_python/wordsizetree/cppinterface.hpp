#ifndef CFFI_WORDSIZETREE_HPP
#define CFFI_WORDSIZETREE_HPP 1
#include "./wordsizetree.hpp"

extern "C"{
    using wstree = nachia::WordsizeTree;
    void *wstree_new(int length){ return new wstree(length); }
    void *wstree_new_with_string(char *s){ return new wstree(s); }
    void wstree_insert(void *obj, int x){ ((wstree*)obj)->insert(x); }
    void wstree_erase(void *obj, int x){ return ((wstree*)obj)->erase(x); }
    int wstree_count(void *obj, int x) { return ((wstree*)obj)->count(x); }
    int wstree_no_less_than(void *obj, int x) { return ((wstree*)obj)->noLessThan(x); }
    int wstree_no_greater_than(void *obj, int x) { return ((wstree*)obj)->noGreaterThan(x); }
}


#endif