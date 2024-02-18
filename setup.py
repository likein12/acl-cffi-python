from cffi import FFI
import os
from setuptools import setup, find_packages


setup(
    name="acl-cffi-python",
    version="0.1.0",
    packages=find_packages(where='src'),
    package_dir={'': 'src'},
)

root_directory = os.getcwd()

os.chdir(f"src/acl_cffi_python/core")

ffibuilder = FFI()
current_directory = os.getcwd()
print(current_directory)
import re
print(open("cinterface.h", "r").read())
cinterface = ""
for line in open("cinterface.h", "r"):
    line = line.rstrip()
    print(line)
    if re.match(r'#include ".+"', line):
        print("expand", line)
        cinterface += "\n" + open(line.split('#include "')[1][:-1], "r").read()
print(cinterface)
ffibuilder.cdef(cinterface)

ffibuilder.set_source(f"cffi_core", open(f"cppinterface.hpp", "r").read(),
    source_extension='.cpp',
    library_dirs=[current_directory],
    include_dirs=[root_directory + "/ac-library"],
    extra_link_args=['-Wl,-rpath=' + current_directory])

ffibuilder.compile(verbose=True, debug=True)
os.chdir(root_directory)
