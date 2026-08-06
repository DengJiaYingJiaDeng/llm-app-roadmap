# Day006 NumPy 复习笔记

> 目标：
>
> - 掌握 NumPy ndarray 基础
> - 理解 shape、dtype、axis、broadcast
> - 掌握 reshape、transpose
> - 实现向量标准化
> - 实现余弦相似度
> - 理解 Embedding 检索中的向量计算


---

# 1. NumPy 基础

## 1.1 NumPy 是什么？

NumPy 是 Python 数值计算基础库。

核心对象：

```python
numpy.ndarray
```

特点：

- 多维数组
- 高效矩阵运算
- 支持广播
- 支持向量化计算


导入：

```python
import numpy as np
```


---

# 2. ndarray 基础属性


创建数组：

```python
arr = np.array([1,2,3,4])
```


查看属性：

```python
arr.shape
arr.dtype
arr.ndim
arr.size
```


|属性|含义|
|-|-|
|shape|数组每个维度大小|
|dtype|元素类型|
|ndim|维度数量|
|size|元素总数量|


示例：

```python
matrix = np.array([
    [1,2,3],
    [4,5,6]
])
```


结果：

```
shape = (2,3)
ndim = 2
size = 6
```


含义：

```
2行
3列
```


---

# 3. Shape 理解（重点）


## 一维数组

```python
x = np.array([1,2,3])
```

shape：

```
(3,)
```


表示：

```
一个长度为3的一维向量
```


不是：

```
(3,1)
```


---

## 二维数组


列向量：

```python
x = np.array([
    [1],
    [2],
    [3]
])
```


shape：

```
(3,1)
```


行向量：

```python
x = np.array([
    [1,2,3]
])
```


shape：

```
(1,3)
```


区别：

```
(3,)
(3,1)
(1,3)
```

在矩阵计算中完全不同。


---

# 4. dtype


查看：

```python
arr.dtype
```


常见类型：

|类型|说明|
|-|-|
|int32|32位整数|
|int64|64位整数|
|float32|32位浮点|
|float64|64位浮点|
|bool|布尔值|


指定：

```python
arr = np.array(
    [1,2,3],
    dtype=np.float32
)
```


转换：

```python
arr.astype(np.int32)
```


注意：

```python
np.array([1.8,2.9]).astype(np.int32)
```


结果：

```
[1,2]
```

直接截断小数。


---

# 5. 创建数组


## zeros

```python
np.zeros((2,3))
```


结果：

```
2×3 全0矩阵
```


---

## ones

```python
np.ones((2,3))
```


---

## full

```python
np.full(
    (2,3),
    7
)
```


---

## arange


```python
np.arange(
    0,
    10,
    2
)
```


结果：

```
[0 2 4 6 8]
```


特点：

按步长生成。


---

## linspace


```python
np.linspace(
    0,
    1,
    5
)
```


结果：

```
[0 0.25 0.5 0.75 1]
```


特点：

指定数量。


---

# 6. 索引和切片


## 一维数组


```python
x = np.array(
    [10,20,30,40,50]
)
```


访问：

```python
x[0]
x[-1]
```


切片：

```python
x[:3]
x[1:4]
x[::-1]
```


---

## 二维数组


格式：

```python
array[row,column]
```


例如：

```python
matrix[0,1]
```


表示：

```
第1行第2列
```


常见：

```python
matrix[:,1]
```

含义：

```
所有行，第2列
```


---

# 7. 视图 View 与 Copy


NumPy 切片默认可能共享数据。


例如：

```python
a = np.array(
    [1,2,3,4]
)

b = a[1:3]

b[0]=999
```


可能导致：

```python
a
```

也改变。


如果需要独立数据：

```python
b = a[1:3].copy()
```


原则：

```
需要修改 → copy()
只读计算 → slice
```


---

# 8. reshape


作用：

改变 shape，不改变数据。


例如：

```python
x = np.arange(12)

x.reshape(3,4)
```


原：

```
(12,)
```


变：

```
(3,4)
```


要求：

```
元素数量必须一致
```


错误：

```python
np.arange(12).reshape(5,3)
```


因为：

```
12 != 15
```


---

## -1 自动推断


```python
x.reshape(3,-1)
```


NumPy 自动计算：

```
(3,4)
```


常用于：

```python
batch_size,-1
```


---

# 9. transpose 转置


作用：

交换维度。


二维：

```python
x.T
```


例如：

```
(2,3)
```

变：

```
(3,2)
```


---

三维：

LLM 常见：

```
(batch,seq,dim)
```


例如：

```
(8,128,768)
```


交换：

```python
x.transpose(1,0,2)
```


变：

```
(seq,batch,dim)
```


---

# 10. axis


axis 表示计算方向。


二维：

```
(rows,columns)
```


## axis=0


按列计算：

```python
matrix.sum(axis=0)
```


例如：

```
[
[1,2,3],
[4,5,6]
]
```


结果：

```
[5,7,9]
```


---

## axis=1


按行计算：

```python
matrix.sum(axis=1)
```


结果：

```
[6,15]
```


记忆：

```
axis=0 删除行维度

axis=1 删除列维度
```


---

# 11. keepdims


问题：

```python
norm = np.linalg.norm(
    x,
    axis=1
)
```


shape:

```
(n,)
```


可能导致广播失败。


使用：

```python
norm = np.linalg.norm(
    x,
    axis=1,
    keepdims=True
)
```


shape:

```
(n,1)
```


方便：

```python
x / norm
```


---

# 12. 广播 Broadcast


作用：

不同 shape 自动扩展计算。


例如：

```python
x=np.array([1,2,3])

x+10
```


相当于：

```
[1,2,3]
+
[10,10,10]
```


---

矩阵：

```python
matrix.shape

(2,3)
```


bias：

```
(3,)
```


可以：

```python
matrix+bias
```


---

广播规则：

从右往左比较：

满足：

1. 相同
2. 一个为1
3. 缺失


例如：

可以：

```
(2,3)

(3,)
```


不能：

```
(2,3)

(2,)
```


---

# 13. 布尔索引


条件筛选：

```python
scores=np.array(
[50,80,90]
)


scores>70
```


得到：

```
False True True
```


筛选：

```python
scores[
    scores>70
]
```


结果：

```
[80,90]
```


多条件：

```python
(
scores>60
)
&
(
scores<90
)
```


注意：

不能：

```python
and
or
```


NumPy 使用：

```
&
|
~
```


---

# 14. 随机数


推荐：

```python
rng=np.random.default_rng(42)
```


生成：

```python
rng.random(
(3,4)
)
```


随机种子作用：

```
保证实验可复现
```


---

# 15. 向量标准化


公式：

```
x / ||x||
```


目的：

让向量长度变成1。


代码：

```python
def normalize_vector(x):

    norm=np.linalg.norm(x)

    if norm==0:
        raise ValueError()

    return x/norm
```


例如：

```
[3,4]
```


长度：

```
5
```


标准化：

```
[0.6,0.8]
```


长度：

```
1
```


---

# 16. 批量标准化


输入：

```
(num_vectors,dim)
```


例如：

```
(1000,768)
```


代码：

```python
norms=np.linalg.norm(
    vectors,
    axis=1,
    keepdims=True
)

vectors/norms
```


---

# 17. 余弦相似度


公式：

```
cos(a,b)

=
a·b
--------
||a|| ||b||
```


范围：

```
-1 ~ 1
```


含义：

|值|意义|
|-|-|
|1|完全相似|
|0|无关|
|-1|相反|


---

代码：

```python
def cosine_similarity(a,b):

    return np.dot(a,b) / (
        np.linalg.norm(a)
        *
        np.linalg.norm(b)
    )
```


---

# 18. Embedding 检索


LLM 中：

文本：

```
Document
```

↓

Embedding模型

↓

向量：

```
[0.1,0.2,...]
```


多个文档：

```
documents

(num_documents,dim)
```


查询：

```
query

(dim,)
```


计算：

```python
scores = documents @ query
```


结果：

```
(num_documents,)
```


每个数字代表一个文档相似度。


---

# 19. Top-K 检索


目标：

找到最高相似度的K个。


简单方法：

```python
indices=np.argsort(scores)[::-1][:k]
```


流程：

```
排序
↓
反转
↓
取前K
```


---

大数据：

```python
np.argpartition()
```


优势：

只寻找Top-K，不完整排序。


---

# 20. Python循环 vs NumPy向量化


Python：

```
for循环
逐个计算
```


NumPy：

```
矩阵计算
批量处理
```


NumPy 快原因：

- 底层C实现
- SIMD优化
- BLAS库
- 减少Python解释器开销


---

# 21. 常见Shape错误


## reshape错误


错误：

```python
np.arange(12).reshape(5,3)
```


原因：

```
12 != 15
```


---

## 广播错误


错误：

```
matrix=(3,4)

bias=(3,)
```


解决：

```python
bias.reshape(3,1)
```


---

## 维度不匹配


错误：

```
documents=(100,768)

query=(512,)
```


原因：

```
768 != 512
```


---

## axis错误


文档向量：

```
(num_documents,dim)
```


求每个文档长度：

正确：

```python
axis=1
```


---

# 22. LLM 常见 Shape


## Token embedding


```
(batch,seq,dim)
```


例如：

```
(8,128,768)
```


含义：

|维度|含义|
|-|-|
|batch|样本数量|
|seq|token数量|
|dim|向量维度|


---

## Embedding数据库


文档：

```
(100000,768)
```


查询：

```
(768,)
```


结果：

```
(100000,)
```


---

# 23. Day006 核心口诀


```
shape先看清
axis不要乱
广播从右看
reshape数量不能变

向量先归一化
点积变相似度
Top-K找最近
错误先打印shape
```


---

# Day006 完成标准


能够回答：

1. ndarray是什么？

答：

NumPy多维数组。


2. reshape和transpose区别？

答：

reshape改变形状；
transpose交换维度。


3. 为什么normalize？

答：

统一向量长度，方便计算余弦相似度。


4. 为什么LLM大量使用NumPy？

答：

因为Embedding、矩阵运算、本质都是向量计算。


5. 遇到计算错误怎么办？

第一步：

```python
print(array.shape)
```


先确认维度，再检查公式。
