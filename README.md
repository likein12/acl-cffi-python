# acl-cffi-python
Wrapper library of ac-library with CFFI. This library is for both Python and PyPy.

## 構造

ソース側
```acl_cffi_python/[各ライブラリ]```の下部に四つのファイル

- ```__init__.py``` : Python側で呼び出したいのを全部出す
- ```interface.py``` : Python側のインターフェース記述
- ```cinterface.h``` : C言語のインターフェース記述
- ```cppinterface.hpp``` : C++でvoidポインタと各クラスの変換など

ビルドされると、
- ```cffi_core.pypy39-pp73-x86_64-linux-gnu.so```
- ```cffi_core.cpp```
- ```cffi_vector.o```
ができる。

```setup.py```でビルドする。（ジャッジ側でも同じようにやる）

tar.gzに圧縮してバイナリで投げる。

## 予定
|name|interface|build|verify|document|benchmarking|
|:-:|:-:|:-:|:-:|:-:|:-:|
|std/vector vector int|ok|ok|
|std/vector vector ll|ok|ok|
|std/vector vector mod998|ok|ok|
|std/vector vector vvi|ok|ok|
|std/utility pair ll|ok|ok|
|std/string|ok|ok|
|std/set set ll|
|std/set multiset ll|
|std/set map ll|
|io|ok|ok||||
|math/crt|ok|ok||||
|math/floor_sum|ok|ok||||
|math/ext_gcd||||||
|convolution mod998|ok|ok||||
|convolution ll|ok|ok||||
|dsu|ok|ok||||
|maxflow ll|ok|ok||||
|mincostflow ll|ok|ok||||
|modint||||||
|scc|ok|ok||||
|twosat|ok|ok||||
|fenwicktree ll|ok|ok||||
|segtree RMQ|ok|ok||||
|segtree template|ok|||||
|lazysegtree RUQ-RMQ|||||
|lazysegtree range affine range sum|||||
|lazysegtree template|||||
|string/suffix_array|ok|
|string/lcp_array|ok|
|string/z_algorithm|ok|
|string/rolling_hash|

verifyでは各々3問以上は投げたい