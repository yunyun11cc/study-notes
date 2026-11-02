# 常用方法

## "  ".join(iterable)->str

"  ".join() 传入的参数是一个==**可迭代的对象(iterable)**==，将这个列表中的所有元素用 " " 中的内容连接在一起并返回一个==**字符串**== 

- 参数：**可迭代对象**，其中每个元素都必须是**字符串**（`str`）。
- 返回值：把这些元素用 `" "` 作为分隔符拼接起来的**字符串**。
- 若可迭代对象为空，返回 `""`（空字符串）。

````python
"+".join(["a", "b", "c"])      # 列表 → "a+b+c"
"--".join(("a", "b", "c"))      # 元组 → "a--b--c"
"".join({"a", "b", "c"})      # 集合 → 顺序不定，如 "acb"
"-".join("abc")                # 字符串本身也是可迭代 → "a-b-c"
"  ".join(c for c in "abc")     # 生成器 → "a  b  c"
"  ".join({"a": 1, "b": 2})     # 字典迭代的是键 → "a  b"
"  ".join([])                   # 空列表 → ""
````



## sort() 和 sorted()

list.sort(key)->None：

sort是list的方法之一，只能对列表使用，sort对列表进行原地排序，返回的是排序完以后的列表



sorted(iterable , key=lamda:... , reverse:False)->list

- 参数：**可迭代对象**，key:排序方法，reverse:False为升序排列。
- 返回值：按key排完序后的新列表

































# 字典

## 增删改查

````Python
# 增/改
d[key] = value              # 存在则更新，不存在则插入

# 查存在
key in d                    # True/False，O(1)
key not in d

# 取值
d[key]                      # 不存在 → KeyError
d.get(key)                  # 不存在 → None
d.get(key, default)         # 不存在 → default

# 判断值相等（先保证 key 存在）
if key in d and d[key] == x:
    ...

# 初始化 + 追加（分组）
d.setdefault(key, []).append(x)

# 计数
d[key] = d.get(key, 0) + 1
# 或
from collections import defaultdict
cnt = defaultdict(int); cnt[key] += 1

# 删除
d.pop(key)                  # 不存在 → KeyError
d.pop(key, None)            # 不存在 → 返回 None，不报错
del d[key]                  # 不存在 → KeyError
````

