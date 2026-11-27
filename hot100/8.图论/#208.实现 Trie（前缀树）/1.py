"""
实现用于存储字符串的 Trie 类。输入的单词和前缀都由小写英文字母组成。
Trie() 初始化一个空前缀树。
insert(word) 插入单词 word。
search(word) 判断是否插入过完全相同的单词。
startsWith(prefix) 判断是否有已插入的单词以 prefix 开头。

示例 1
输入：操作 = ["Trie", "insert", "search", "startsWith", "search"]
      参数 = [[], ["apple"], ["app"], ["app"], ["apple"]]
输出：[None, None, False, True, True]
解释：app 是 apple 的前缀，但目前只有 apple 作为完整单词插入。

示例 2
输入：操作 = ["Trie", "startsWith", "insert", "search", "startsWith"]
      参数 = [[], ["ca"], ["cat"], ["cat"], ["do"]]
输出：[None, False, None, True, False]
解释：空前缀树中没有以 ca 开头的单词。插入 cat 后能查到 cat。
"""


class Trie:
    def __init__(self) -> None:
        pass

    def insert(self, word: str) -> None:
        pass

    def search(self, word: str) -> bool:
        pass

    def startsWith(self, prefix: str) -> bool:
        pass
