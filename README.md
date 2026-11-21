# pairwise-vertex-cache-opt

模型顶点顺序乱了以后，手机上帧率掉了一半，后变换缓存命中率只有三成；索引按建模顺序排列，相邻三角形复用不到刚变换的顶点；顶点缓存按 FIFO 模拟，容量 32 时刚好把最常用的顶点挤出去；三角形列表里夹着退化三角形，光栅化前就浪费了一次顶点着色；16bit 索引在大模型上被迫分批绘制，每批都重跑一次 uniform 更新；顶点属性按 32 字节对齐，但实际只用了 20 字节，带宽被 padding 吃掉；instancing 与顶点缓存优化同时开，实例间的顶点顺序被优化器打乱，GPU 每次都要重新取；strip 与 list 混用，primitive restart 索引出现在错误位置，模型裂开；优化器按单帧顺序重排，动画变形后缓存命中率又掉回去；多 pass 渲染每个 pass 各自重排索引，深度预pass 与主 pass 的顶点顺序不一致。render/vertex_cache_opt.py 是核心，tests/test_vertex_cache_opt.py 15个红。要修的是：按缓存容量重排；FIFO 模拟命中；剔除退化三角形；按批合并绘制；属性紧凑打包；实例顺序固定；restart 位置校验；按蒙皮后的顺序；多 pass 共用索引；优化后校验拓扑。

## 运行

```bash
python -m pytest tests -q
```

初始状态：15 个用例失败。修复实现使全部用例通过，不要修改 `tests/` 下的测试。

子方向：见平台；任务类型：Bugfix；语言/框架：Python 3, pytest；环境可复现等级：无外部依赖。
