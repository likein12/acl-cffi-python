from acl_cffi_python.core.cffi_core.lib import (string_new, string_push_back, string_at,
                                                  string_size, string_sub)


class String(object):
    def __init__(self, s: bytes):
        """
        s.encode()で変換
        """
        self.obj = string_new(s)
    def __getitem__(self, index: int) -> bytes:
        return string_at(self.obj, index)
    def __setitem__(self, index: int, c: bytes) -> bytes:
        return string_sub(self.obj, index, c)
    def __len__(self) -> int:
        return string_size(self.obj)

if __name__ == "__main__":
    s = String("abc".encode())
    s[2] = b'x'
    print(s[2])