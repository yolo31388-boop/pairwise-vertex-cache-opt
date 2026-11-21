import math

def cache_hit(cache, index):
    """缓存命中。"""
    raise NotImplementedError("TODO: cache_hit")

def acmr(vertices, triangles):
    """ACMR。"""
    raise NotImplementedError("TODO: acmr")

def pack_stride(bytes_used):
    """属性打包。"""
    raise NotImplementedError("TODO: pack_stride")

def batch_count(vertices, limit):
    """分批数量。"""
    raise NotImplementedError("TODO: batch_count")

def attr_bytes(count, size):
    """属性字节。"""
    raise NotImplementedError("TODO: attr_bytes")

def restart_index(index):
    """restart 索引。"""
    raise NotImplementedError("TODO: restart_index")

def shared_index(a, b):
    """共享索引。"""
    raise NotImplementedError("TODO: shared_index")

def fifo_insert(cache, index, capacity):
    """FIFO 插入。"""
    raise NotImplementedError("TODO: fifo_insert")

def optimize_count(triangles):
    """优化后数量。"""
    raise NotImplementedError("TODO: optimize_count")

def instance_order(instance):
    """实例顺序。"""
    raise NotImplementedError("TODO: instance_order")

def multipass_same(a, b):
    """多 pass 一致。"""
    raise NotImplementedError("TODO: multipass_same")

def mesh_key(seed, index):
    """网格键。"""
    raise NotImplementedError("TODO: mesh_key")

def degenerate(a, b, c):
    """退化三角形。"""
    raise NotImplementedError("TODO: degenerate")

def align4(value):
    """4 字节对齐。"""
    raise NotImplementedError("TODO: align4")

def is_16bit(max_vertex):
    """16bit 判定。"""
    raise NotImplementedError("TODO: is_16bit")
