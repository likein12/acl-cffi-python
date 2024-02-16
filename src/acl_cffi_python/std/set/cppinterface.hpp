#ifndef CFFI_STD_SET_HPP
#define CFFI_STD_SET_HPP 1
#include <set>

extern "C" {
    using setll = std::set<long long>;
    using setll_itr = std::set<long long>::iterator;
    using setll_ritr = std::set<long long>::reverse_iterator;

    void *setll_new(){ return new setll(); }
    void setll_insert(void *obj, long long x){ ((setll*)obj)->insert(x); }
    void *setll_find(void *obj, long long x){ return new setll_itr(((setll*)obj)->find(x)); }
    void setll_erase(void *obj, void *itr){ ((setll*)obj)->erase(*(setll_itr*)itr);}
    void setll_erase_val(void *obj, long long x){ ((setll*)obj)->erase(((setll*)obj)->find(x));}
    void setll_clear(void *obj){ ((setll*)obj)->clear(); }
    int setll_contain(void *obj, long long x){ return ((setll*)obj)->find(x) != ((setll*)obj)->end(); }
    int setll_size(void *obj){ return ((setll*)obj)->size(); }
    void *setll_begin(void *obj){ return new setll_itr(((setll*)obj)->begin()); }
    void *setll_end(void *obj){ return new setll_itr(((setll*)obj)->end()); }
    void *setll_rbegin(void *obj){ return new setll_ritr(((setll*)obj)->rbegin()); }
    void *setll_rend(void *obj){ return new setll_ritr(((setll*)obj)->rend()); }
    int setll_itr_compare(void *itr1, void *itr2){ return (*(setll_itr*)itr1) == (*(setll_itr*)itr2); }
    int setll_ritr_compare(void *ritr1, void *ritr2){ return (*(setll_ritr*)ritr1) == (*(setll_ritr*)ritr2); }

    void *setll_lower_bound(void *obj, long long x){ return new setll_itr(((setll*)obj)->lower_bound(x)); }
    void *setll_upper_bound(void *obj, long long x){ return new setll_itr(((setll*)obj)->upper_bound(x)); }

    long long setll_itr_deref(void *obj){ return **(setll_itr*)obj; }
    void setll_itr_increment(void *obj){ ++(*(setll_itr*)obj); }
    void setll_itr_decrement(void *obj){ --(*(setll_itr*)obj); }
    long long setll_ritr_deref(void *obj){ return **(setll_ritr*)obj; }
    void setll_ritr_increment(void *obj){ ++(*(setll_ritr*)obj); }
    void setll_ritr_decrement(void *obj){ --(*(setll_ritr*)obj); }

    using mlsetll = std::multiset<long long>;
    using mlsetll_itr = std::multiset<long long>::iterator;
    using mlsetll_ritr = std::multiset<long long>::reverse_iterator;

    void *mlsetll_new(){ return new mlsetll(); }
    void mlsetll_insert(void *obj, long long x){ ((mlsetll*)obj)->insert(x); }
    void *mlsetll_find(void *obj, long long x){ return new mlsetll_itr(((mlsetll*)obj)->find(x)); }
    void mlsetll_erase(void *obj, void *itr){ ((mlsetll*)obj)->erase(*(mlsetll_itr*)itr);}
    void mlsetll_erase_val_one(void *obj, long long x){ ((mlsetll*)obj)->erase(((mlsetll*)obj)->find(x));}
    void mlsetll_erase_val_all(void *obj, long long x){ ((mlsetll*)obj)->erase(x);}
    void mlsetll_clear(void *obj){ ((mlsetll*)obj)->clear(); }
    int mlsetll_contain(void *obj, long long x){ return ((mlsetll*)obj)->find(x) != ((mlsetll*)obj)->end(); }
    int mlsetll_size(void *obj){ return ((mlsetll*)obj)->size(); }
    void *mlsetll_begin(void *obj){ return new mlsetll_itr(((mlsetll*)obj)->begin()); }
    void *mlsetll_end(void *obj){ return new mlsetll_itr(((mlsetll*)obj)->end()); }
    void *mlsetll_rbegin(void *obj){ return new mlsetll_ritr(((mlsetll*)obj)->rbegin()); }
    void *mlsetll_rend(void *obj){ return new mlsetll_ritr(((mlsetll*)obj)->rend()); }
    int mlsetll_itr_compare(void *itr1, void *itr2){ return (*(mlsetll_itr*)itr1) == (*(mlsetll_itr*)itr2); }
    int mlsetll_ritr_compare(void *ritr1, void *ritr2){ return (*(mlsetll_ritr*)ritr1) == (*(mlsetll_ritr*)ritr2); }

    void *mlsetll_lower_bound(void *obj, long long x){ return new mlsetll_itr(((mlsetll*)obj)->lower_bound(x)); }
    void *mlsetll_upper_bound(void *obj, long long x){ return new mlsetll_itr(((mlsetll*)obj)->upper_bound(x)); }

    long long mlsetll_itr_deref(void *obj){ return **(mlsetll_itr*)obj; }
    void mlsetll_itr_increment(void *obj){ ++(*(mlsetll_itr*)obj); }
    void mlsetll_itr_decrement(void *obj){ --(*(mlsetll_itr*)obj); }
    long long mlsetll_ritr_deref(void *obj){ return **(mlsetll_ritr*)obj; }
    void mlsetll_ritr_increment(void *obj){ ++(*(mlsetll_ritr*)obj); }
    void mlsetll_ritr_decrement(void *obj){ --(*(mlsetll_ritr*)obj); }

    int mlsetll_count(void *obj, long long x){ return ((mlsetll*)obj)->count(x); }
}

#endif

