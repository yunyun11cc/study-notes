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
    def __init__(self, key: int, value: int):
        self.key = key
        self.val = value
        self.prev = None
        self.next = None


# 1. 用字典从键直接定位节点，用带头尾哨兵的双向链表维护使用顺序。
# 2. 读取或更新命中时，把对应节点移到头部。新节点也从头部插入。
# 3. 容量超限时删除尾哨兵之前的节点，并从字典移除对应键。


class LRUCache:
    def __init__(self, capacity: int):
        self.capacity=capacity  # 容量是固定的，每次动的是 size 的值
        self.cache={} # 存的是key对应的节点
        self.size=0
        # 构造双向链表
        self.head=Node(0,0)
        self.tail=Node(0,0)
        self.head.next=self.tail
        self.tail.prev=self.head

    def addTohead(self,node) -> None:
        node.next=self.head.next
        self.head.next.prev=node
        self.head.next=node
        node.prev=self.head

    def linknode(self,node) -> None:
        node.prev.next=node.next
        node.next.prev=node.prev

    def get(self, key: int) -> int:
        if key in self.cache: # 这个缓存最近被使用过，要先移动到头部
            curr=self.cache[key] #拿到当前节点的指针
            self.linknode(curr)
            self.addTohead(curr)
            return self.cache[key].val
        else:
            return -1

    def headInsert(self,key: int,value: int) -> None:
        new_node=Node(key,value)
        self.addTohead(new_node)
        self.cache[key]=new_node
        self.size+=1

    def tailRemove(self) -> None:
        curr=self.tail.prev
        del self.cache[curr.key] # 清空当前 key 的哈希
        curr.prev.next=self.tail
        self.tail.prev=curr.prev
        self.size-=1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            curr=self.cache[key]
            curr.val=value
            self.linknode(curr)
            self.addTohead(curr)

        else:
            self.headInsert(key, value) # 无脑插入头部，如果满了就删除尾部
            if self.size > self.capacity:
                self.tailRemove()
