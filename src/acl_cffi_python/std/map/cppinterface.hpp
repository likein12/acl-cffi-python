#ifndef CFFI_STD_MAP_HPP
#define CFFI_STD_MAP_HPP 1
#include <map>
#include "../utility/cppinterface.hpp"

extern "C" {
    using mapll = std::map<long long, long long>;
    using mapll_itr = std::map<long long, long long>::iterator;
    using mapll_ritr = std::map<long long, long long>::reverse_iterator;

    void *mapll_new(){ return new mapll(); }
    void mapll_set(void *obj, long long k, long long v){ (*(mapll*)obj)[k] = v; }
    void *mapll_find(void *obj, long long x){ return new mapll_itr(((mapll*)obj)->find(x)); }
    void mapll_erase(void *obj, void *itr){ ((mapll*)obj)->erase(*(mapll_itr*)itr);}
    void mapll_erase_val_one(void *obj, long long x){ ((mapll*)obj)->erase(((mapll*)obj)->find(x));}
    void mapll_erase_val_all(void *obj, long long x){ ((mapll*)obj)->erase(x);}
    void mapll_clear(void *obj){ ((mapll*)obj)->clear(); }
    int mapll_contain(void *obj, long long x){ return ((mapll*)obj)->find(x) != ((mapll*)obj)->end(); }
    int mapll_size(void *obj){ return ((mapll*)obj)->size(); }
    void *mapll_begin(void *obj){ return new mapll_itr(((mapll*)obj)->begin()); }
    void *mapll_end(void *obj){ return new mapll_itr(((mapll*)obj)->end()); }
    void *mapll_rbegin(void *obj){ return new mapll_ritr(((mapll*)obj)->rbegin()); }
    void *mapll_rend(void *obj){ return new mapll_ritr(((mapll*)obj)->rend()); }
    int mapll_itr_compare(void *itr1, void *itr2){ return (*(mapll_itr*)itr1) == (*(mapll_itr*)itr2); }
    int mapll_ritr_compare(void *ritr1, void *ritr2){ return (*(mapll_ritr*)ritr1) == (*(mapll_ritr*)ritr2); }

    void *mapll_lower_bound(void *obj, long long x){ return new mapll_itr(((mapll*)obj)->lower_bound(x)); }
    void *mapll_upper_bound(void *obj, long long x){ return new mapll_itr(((mapll*)obj)->upper_bound(x)); }

    void *mapll_itr_deref(void *obj){ return new pll(**(mapll_itr*)obj); }
    void mapll_itr_increment(void *obj){ ++(*(mapll_itr*)obj); }
    void mapll_itr_decrement(void *obj){ --(*(mapll_itr*)obj); }
    void *mapll_ritr_deref(void *obj){ return new pll(**(mapll_ritr*)obj); }
    void mapll_ritr_increment(void *obj){ ++(*(mapll_ritr*)obj); }
    void mapll_ritr_decrement(void *obj){ --(*(mapll_ritr*)obj); }
}

#endif