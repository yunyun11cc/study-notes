"""
请你设计并实现一个满足  LRU (最近最少使用) 缓存 约束的数据结构。

实现 LRUCache 类：
LRUCache(int capacity) 以 正整数 作为容量 capacity 初始化 LRU 缓存

int get(int key) 如果关键字 key 存在于缓存中，则返回关键字的值，否则返回 -1 。

void put(int key, int value) 如果关键字 key 已经存在，则变更其数据值 value ；
如果不存在，则向缓存中插入该组 key-value 。如果插入操作导致关键字数量超过 capacity ，则应该 逐出 最久未使用的关键字。

函数 get 和 put 必须以 O(1) 的平均时间复杂度运行。
"""



class Node:
    def __init__(self, key: int, value: int):
        self.key = key
        self.val = value
        self.prev = None
        self.next = None

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