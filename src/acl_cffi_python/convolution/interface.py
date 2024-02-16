from acl_cffi_python.convolution.cffi_core.lib import convolution, convolution_ll
from acl_cffi_python.std.vector import VecM, VecLL

def Convolution(a: VecM, b: VecM) -> VecM:
    """
    高速フーリエ変換を使った畳み込み演算(mod 998244353)
    n = len(a), m = len(b)としたとき、n+m-1の長さのmodint配列VecMが返される。
    計算量O((n+m)log(n+m))
    Args:
        a: VecM: modint配列
        b: VecM: modint配列
    Returns:
        畳み込みの結果のmodint配列
    VecMは大体リストのように使うことが可能。acl_cffi_python.std.vector.VecM
    VecM([1, 2, 4])などのような感じで初期化可能（自動で剰余算が行われる）。
    """
    return VecM(ptr = convolution(a.obj, b.obj))

def ConvolutionLL(a: VecLL, b: VecLL) -> VecLL:
    """
    高速フーリエ変換を使った畳み込み演算（剰余算を行わない）
    n = len(a), m = len(b)としたとき、n+m-1の長さのlong long配列VecLLが返される。
    計算量O((n+m)log(n+m))
    Args:
        a: VecLL: long long配列
        b: VecLL: long long配列
    Returns:
        畳み込みの結果のlong long配列
    VecLLは大体リストのように使うことが可能。acl_cffi_python.std.vector.VecLL
    VecLL([1, 2, 4])などのような感じで初期化可能（C++のデータを使っているのでオーバーフローに注意）。
    """
    return VecM(ptr = convolution(a.obj, b.obj))


if __name__ == "__main__":
    a = VecM([1,0,1])
    b = VecM([3,0,3])
    print(Convolution(a, b))
    