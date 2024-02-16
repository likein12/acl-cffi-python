import os
from cffi import FFI

current_directory = os.getcwd()
ffibuilder = FFI()
ffibuilder.cdef("""
typedef struct {
    int a;
    long long b;
} Test;
                
Test get();
                
void *setll_new();
void setll_insert(void *obj, long long x);
void *setll_find(void *obj, long long x);
void setll_erase(void *obj, void *itr);
void setll_erase_val(void *obj, long long x);
void setll_clear(void *obj);
int setll_contain(void *obj, long long x);
int size(void *obj);
void *setll_begin(void *obj);
void *setll_end(void *obj);
void *setll_rbegin(void *obj);
void *setll_rend(void *obj);
""")

ffibuilder.set_source(f"cffi_test", """
#include <set>
extern "C"{
    struct Test{
        int a;
        long long b;
    };
    Test get(){ return Test({1, 4}); }
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
    int size(void *obj){ return ((setll*)obj)->size(); }
    void *setll_begin(void *obj){ return new setll_itr(((setll*)obj)->begin()); }
    void *setll_end(void *obj){ return new setll_itr(((setll*)obj)->end()); }
    void *setll_rbegin(void *obj){ return new setll_ritr(((setll*)obj)->rbegin()); }
    void *setll_rend(void *obj){ return new setll_ritr(((setll*)obj)->rend()); }

}
                      
""",
    source_extension='.cpp',
    library_dirs=[current_directory],
    extra_link_args=['-Wl,-rpath=' + current_directory])

ffibuilder.compile(verbose=True, debug=True)