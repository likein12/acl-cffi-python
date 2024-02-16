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
""")

ffibuilder.set_source(f"cffi_test", """
extern "C"{
    struct Test{
        int a;
        long long b;
    };
    Test get(){ return Test({1, 4}); }
}
""",
    source_extension='.cpp',
    library_dirs=[current_directory],
    extra_link_args=['-Wl,-rpath=' + current_directory])

ffibuilder.compile(verbose=True, debug=True)