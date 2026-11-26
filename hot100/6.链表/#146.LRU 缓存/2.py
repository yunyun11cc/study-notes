"""
实现容量为正整数的 LRUCache（最近最少使用缓存）。
get(key) 命中时返回对应的值并更新该键的使用顺序，未命中时返回 -1。
put(key, value) 插入或更新键值，同时将该键设为最近使用。超出容量时淘汰最久未使用的键。
get 和 put 都应在平均 O(1) 时间内完成。示例输出中的 null 表示该操作没有返回值。

示例 1
输入：操作 = ["LRUCache", "put", "put", "get", "put", "get", "get"], 参数 = [[2], [1, 10], [2, 20], [1], [3, 30], [2], [3]]
输出：[null, null, null, 10, null, -1, 30]
解释：读取键 1 后，插入键 3 会淘汰键 2。

示例 2
输入：操作 = ["LRUCache", "put", "put", "get", "put", "get"], 参数 = [[1], [1, 10], [1, 11], [1], [2, 20], [1]]
输出：[null, null, null, 11, null, -1]
解释：更新已有键不会增加占用，插入键 2 后键 1 被淘汰。
"""


class Node:
    def __init__(self, key: int = 0, val: int = 0):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None


# 1. 用字典定位节点，双向链表从头到尾保存从最近到最久使用的顺序。
# 2. 把摘除、头插和移动封装成辅助方法，读取与更新共用移到头部的操作。
# 3. 新增节点超过容量时弹出尾部节点，同时更新字典与计数。


class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
        self.size = 0
        # 两个哨兵把真实节点的插入和删除统一成普通的链表操作。
        self.head = Node()
        self.tail = Node()
        self.head.next = self.tail
        self.tail.prev = self.head

    def _add_to_head(self, node: Node) -> None:
        node.prev = self.head
        node.next = self.head.next
        self.head.next.prev = node
        self.head.next = node

    def _remove_node(self, node: Node) -> None:
        node.prev.next = node.next
        node.next.prev = node.prev

    def _move_to_head(self, node: Node) -> None:
        self._remove_node(node)
        self._add_to_head(node)

    def _pop_tail(self) -> Node:
        node = self.tail.prev
        self._remove_node(node)
        return node

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        curr = self.cache[key]
        self._move_to_head(curr)
        return curr.val

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            curr = self.cache[key]
            curr.val = value
            self._move_to_head(curr)
        else:
            new_node = Node(key, value)
            self.cache[key] = new_node
            self._add_to_head(new_node)
            self.size += 1
            if self.size > self.capacity:
                removed = self._pop_tail()
                del self.cache[removed.key]
                self.size -= 1
