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

sort是list的方法之一，只能对列表使用，sort对列表进行原地排序，最后返回None



sorted(iterable , key=lamda:... , reverse:False)->list

- 参数：**可迭代对象**，key:排序方法，reverse:False为升序排列。
- 返回值：按key排完序后的新列表



两者的key和reverse都相同

- **原列表可以改、且只关心排序结果** → 用 `list.sort()`（省内存，尤其大列表）。
- **不想动原数据 / 对象不是 list / 需要链式使用返回值** → 用 `sorted()`。
- **永远不要写 `x = list.sort()`**，要写 `x = sorted(list)` 或 `list.sort()` 后直接用 `list`。





























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





# 双端队列

## 基础操作

````python
from collections import deque

# 1. 传入多个元素（列表、元组、range 均可）
q1 = deque([1, 2, 3])        # deque([1, 2, 3])
q2 = deque((10, 20))         # deque([10, 20])
q3 = deque(range(4))         # deque([0, 1, 2, 3])

# 2. 字符串的常见坑：字符串本身是可迭代对象！
q4 = deque("abc")            # deque(['a', 'b', 'c']) -> 会被拆成单个字符
q5 = deque(["abc"])          # deque(['abc'])         -> 想存整个字符串必须套中括号

# 3. 定长队列 maxlen（做滑动窗口、日志缓冲、历史记录极好用）
q6 = deque([1, 2, 3], maxlen=3)
q6.append(4)                 # 队列已满，自动从左侧挤掉 1 -> deque([2, 3, 4])
q6.appendleft(0)             # 从左侧塞入，自动从右侧挤掉 4 -> deque([0, 2, 3])
````



### 写题时最容易踩的 2 个坑

1. **初始化漏掉中括号**： `deque()` 的参数必须是一个**可迭代对象**。如果你直接写 `q = deque(root)`，会立刻报错 `TypeError: 'TreeNode' object is not iterable`。必须写成 `q = deque([root])`，或者先建空队列再 `q.append(root)`。
2. **手滑写成 `q.pop()`**： `deque` 是双端队列，右侧也能弹出。`q.pop()` 弹出的是队尾元素（后进先出，直接退化成栈/DFS 了），写 BFS 队列时一定要盯紧写 **`q.popleft()`**。
