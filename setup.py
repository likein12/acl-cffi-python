from cffi import FFI
import os
from setuptools import setup, find_packages


setup(
    name="acl-cffi-python",
    version="0.1.0",
    packages=find_packages(where='src'),
    package_dir={'': 'src'},
)

tags = ["convolution", "dsu", "std/vector", "std/utility", "std/string", "std/set", "string",
        "maxflow", "mincostflow", "scc", "twosat", "segtree/rmq", "io", "math", "fenwicktree"]


root_directory = os.getcwd()

for tag in tags:
    os.chdir(f"src/acl_cffi_python/{tag}")

    ffibuilder = FFI()
    current_directory = os.getcwd()
    ffibuilder.cdef(open("cinterface.h", "r").read())

    ffibuilder.set_source(f"cffi_core", open(f"cppinterface.hpp", "r").read(),
        source_extension='.cpp',
        library_dirs=[current_directory],
        include_dirs=[root_directory + "/ac-library"],
        extra_link_args=['-Wl,-rpath=' + current_directory])

    ffibuilder.compile(verbose=True, debug=True)
    os.chdir(root_directory)
