import os
from cffi import FFI

current_directory = os.getcwd()
ffibuilder = FFI()
ffibuilder.cdef("""
int get_int_n(int *v, int n);                
int *get_int_ptr(int *v);                
""")

ffibuilder.set_source(f"cffi_test", """
extern "C"{
    int get_int_n(int *v, int n){ return v[n]; }
    int *get_int_ptr(int *v){
        int *a = (int *)malloc(sizeof(int) * 4);
        a[0] = v[0];
        a[1] = v[1];
        return a;
    }
}
                      
""",
    source_extension='.cpp',
    library_dirs=[current_directory],
    extra_link_args=['-Wl,-rpath=' + current_directory])

ffibuilder.compile(verbose=True, debug=True)