# LeetCode Hot 100 · C++ 语法速查

适用 C++17。按题目给定的函数签名提交，通常不用自己写 `main` 或处理输入输出。用 `⌘F` / `Ctrl+F` 搜函数名，或从目录跳转。

- [vector 动态数组](#vector-动态数组)
- [string 字符串](#string-字符串)
- [哈希表和集合](#哈希表和集合)
- [栈、队列和堆](#栈队列和堆)
- [迭代器和标准算法](#迭代器和标准算法)
- [链表和树的指针](#链表和树的指针)
- [遍历和 pair](#遍历和-pair)

`T` 是元素类型，`K`、`V` 分别是键和值的类型；`x` 是操作的值，`it` 是迭代器。表中的名称都是语法占位符。

## vector 动态数组

头文件：`<vector>`

| 操作 | 写法 | 参数和注意点 |
| --- | --- | --- |
| 创建 | `std::vector<T> v;` / `std::vector<T> v(n, value);` | 前者为空；后者有 `n` 个元素，每个都是 `value`。 |
| 创建二维数组 | `std::vector<std::vector<T>> grid(rows, std::vector<T>(cols, value));` | `rows` 是行数，`cols` 是列数。 |
| 访问 | `v[i]` / `v.front()` / `v.back()` | `i` 从 `0` 开始，`[]` 不检查越界；首尾访问要求非空。 |
| 长度和判空 | `v.size()` / `v.empty()` | `size()` 返回无符号整数。空容器的 `v.size() - 1` 会下溢。 |
| 末尾增删 | `v.push_back(x)` / `v.pop_back()` | `pop_back()` 不返回元素，且要求非空；扩容时旧迭代器、指针和引用会失效。 |
| 按位置删除 | `v.erase(it)` | 参数是指向待删元素的迭代器；返回删除后的下一个位置，可能是 `v.end()`。删除处及之后的旧迭代器失效。 |

## string 字符串

头文件：`<string>`

| 操作 | 写法 | 参数和注意点 |
| --- | --- | --- |
| 创建和访问 | `std::string s;` / `s[i]` / `s.size()` | 先检查 `i < s.size()` 再访问字符。 |
| 拼接 | `s += text` / `s.push_back(ch)` | `+=` 可追加字符串，`push_back` 只接收单个字符。 |
| 查找 | `s.find(text, pos)` / `s.find(ch, pos)` | 从下标 `pos` 开始查找，默认从 `0` 开始；找不到返回 `std::string::npos`。 |
| 截取 | `s.substr(pos, len)` | `pos` 是起始下标，`len` 是长度。省略 `len` 就取到末尾；`pos > s.size()` 会抛出异常。 |

## 哈希表和集合

头文件：`<unordered_map>`、`<unordered_set>`；有序版本用 `<map>`、`<set>`。

| 操作 | 写法 | 参数和注意点 |
| --- | --- | --- |
| 哈希表读写 | `std::unordered_map<K, V> m;` / `m[key]` | 键不存在时，`m[key]` 会插入新元素；如果值类型是整数，初始值为 `0`。 |
| 哈希表查找 | `m.find(key)` / `m.count(key)` | `find` 返回迭代器，没找到返回 `m.end()`；`count` 返回 `0` 或 `1`。 |
| 哈希集合 | `std::unordered_set<T> st;` / `st.insert(x)` / `st.count(x)` / `st.erase(x)` | 元素不重复，`count` 返回 `0` 或 `1`。 |
| 有序表和集合 | `std::map<K, V> m;` / `std::set<T> st;` | 分别按键、元素排序，默认升序；哈希版本不保证遍历顺序。 |

## 栈、队列和堆

| 结构 | 声明 | 访问和增删 | 头文件 |
| --- | --- | --- | --- |
| 栈 | `std::stack<T> st;` | `top()` 看栈顶，`push(x)` 入栈，`pop()` 出栈。 | `<stack>` |
| 队列 | `std::queue<T> q;` | `front()` 看队首，`push(x)` 从队尾加入，`pop()` 移除队首。 | `<queue>` |
| 最大堆 | `std::priority_queue<T> pq;` | `top()` 看最大元素，`push(x)` 加入，`pop()` 移除堆顶。 | `<queue>` |
| 最小堆 | `std::priority_queue<T, std::vector<T>, std::greater<T>> pq;` | 操作同上，`top()` 取最小元素。 | `<queue>`、`<vector>`、`<functional>` |

`pop()` 不返回元素。需要取出元素时先读取，再弹出；访问或弹出前先确认非空。

## 迭代器和标准算法

`v.begin()` 是起始位置，`v.end()` 是末尾之后的位置，不能解引用；空容器两者相等。下面的 `first, last` 是迭代器，表示左闭右开区间 `[first, last)`。

| 操作 | 写法 | 参数和注意点 | 头文件 |
| --- | --- | --- | --- |
| 排序 | `std::sort(first, last)` / `std::sort(first, last, comp)` | 默认升序，直接修改原区间。`comp(a, b)` 表示 `a` 是否应排在 `b` 前面，不能用 `<=`。 | `<algorithm>` |
| 线性查找 | `std::find(first, last, x)` | 返回第一个等于 `x` 的位置；找不到返回 `last`。 | `<algorithm>` |
| 二分下界 | `std::lower_bound(first, last, x)` | 对升序区间，返回第一个 `>= x` 的位置；可能返回 `last`。 | `<algorithm>` |
| 二分上界 | `std::upper_bound(first, last, x)` | 对升序区间，返回第一个 `> x` 的位置；可能返回 `last`。 | `<algorithm>` |
| 反转和填充 | `std::reverse(first, last)` / `std::fill(first, last, value)` | 直接修改原区间；`value` 是填入的值。 | `<algorithm>` |
| 累加 | `std::accumulate(first, last, init)` | `init` 是初始值，也决定累加类型；总和可能很大时用 `long long` 类型的初始值。 | `<numeric>` |

## 链表和树的指针

`ListNode` 和 `TreeNode` 通常由题目提供。`p`、`q` 表示节点指针。

| 操作 | 写法 | 注意点 |
| --- | --- | --- |
| 声明和判空 | `ListNode* p = nullptr;` / `TreeNode* p = nullptr;` / `p == nullptr` | `nullptr` 表示没有指向节点。 |
| 访问节点成员 | `p->val` / `p->next` / `p->left` / `p->right` | `->` 用于通过指针访问成员；`p` 必须指向有效节点。 |
| 移动指针 | `p = q` / `p = p->next` | 只改变 `p` 指向的位置，不改变节点之间的连接。 |
| 修改连接 | `p->next = q` / `p->left = q` / `p->right = q` | 修改 `p` 所指节点的成员。如果后面还要访问旧连接，先保存旧指针。 |

## 遍历和 pair

| 操作 | 写法 | 注意点 |
| --- | --- | --- |
| 按值遍历 | `for (auto x : v)` | 对普通容器元素，`x` 是副本。 |
| 按引用遍历 | `for (auto& x : v)` / `for (const auto& x : v)` | 前者可修改原元素（若元素本身可写）；后者只读且不复制。 |
| 保存两个值 | `std::pair<A, B>` / `p.first` / `p.second` | `A`、`B` 是两个值的类型；头文件是 `<utility>`。此处 `p` 是 `pair` 对象。 |
| 拆开两个值 | `auto [a, b] = p;` / `const auto& [a, b] = p;` | C++17 结构化绑定；前者复制 `pair`，后者只读引用原对象。 |
