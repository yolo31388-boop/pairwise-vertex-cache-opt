import pytest
import math
from render import vertex_cache_opt as mod

CASES = [
    ("hit", 'm.cache_hit([1, 2], 2) is True'),
    ("acmr", 'm.acmr(6, 2) == approx(3.0)'),
    ("stride", 'm.pack_stride(20) == 32'),
    ("batch", 'm.batch_count(100, 60) == 2'),
    ("bytes", 'm.attr_bytes(4, 8) == 32'),
    ("restart", 'm.restart_index(5) == 5'),
    ("shared", 'm.shared_index(2, 2) == 2'),
    ("fifo", 'm.fifo_insert([1, 2], 3, 2) == [2, 3]'),
    ("count", 'm.optimize_count(100) == 100'),
    ("instance", 'm.instance_order(7) == 7'),
    ("multipass", 'm.multipass_same(1, 1) is True'),
    ("key", 'm.mesh_key(3, 2) == "3:2"'),
    ("degenerate", 'm.degenerate(1, 1, 2) is True'),
    ("align", 'm.align4(5) == 8'),
    ("bits", 'm.is_16bit(60000) is True')
]

@pytest.mark.parametrize("name,expr", CASES, ids=[c[0] for c in CASES])
def test_contract(name, expr):
    assert eval(expr, {"m": mod, "approx": pytest.approx, "math": math})
