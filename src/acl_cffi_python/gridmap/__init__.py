from acl_cffi_python.core.cffi_core.lib import scanner_gridmap


class GridMap(object):
    def __init__(self, H: int, W: int, mode: str):
        self.obj = scanner_gridmap(H, W)

    def up(self, i:int, j:int):
        return self[i-1, j]
     
    def down(self, i:int, j:int):
        return self[i+1, j]
    
    def left(self, i:int, j:int):
        return self[i, j-1]

    def right(self, i: int, j: int):
        return self[i, j+1]    

    def __getitem__(self, i, j):
        if i < 0 or i >= self.obj.h or j < 0 or j >= self.obj.w:
            return None
        return self.obj.ptr[i*self.obj.w+ j]
    