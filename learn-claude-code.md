# learn-claude-code

## 0.agent是什么

````
agent = LLM 大模型 + Harness

Harness = Tools + Knowledge + Observation + Action Interfaces + Permissions

    Tools:          文件读写、Shell、网络、数据库、浏览器
    Knowledge:      产品文档、领域资料、API 规范、风格指南
    Observation:    git diff、错误日志、浏览器状态、传感器数据
    Action:         CLI 命令、API 调用、UI 交互
    Permissions:    沙箱隔离、审批流程、信任边界
````

大模型是 agent 的大脑，Harness 是 agent 赋予大模型的眼睛和手脚

开发 agent 就是为 LLM 开发一个厉害的 Harness

> 只有有一个好鞍的马才能行千里
>
> 
>
> 学习 claude-code 整体开发给我们的经验



## 1.The Agent Loop

**为什么需要循环？** 模型往往看到第一步的实际结果，才能决定第二步做什么。程序每执行一次工具，就把新的观察结果交给模型。

> 这里也是一个 thought -> action -> observation 的一个小过程，不断的循环来完成我们的目标
>
> 暂时只用简单的 loop 来实现我们一个简单的 agent



核心思想

````python
 def agent_loop(messages):
    while True:
        response = 调用模型(messages, 工具定义)

        messages.append(模型的响应)

        tool_calls = 提取工具调用(response)
        if not tool_calls:
            break  # 循环结束的边界：没有调用工具

        results = 执行工具(tool_calls)
        messages.append(工具执行结果)
````





### 1.1 `messages`和`response`

这里的 `messages` 是用来保存用户任务、模型响应和工具结果的一个**列表**

我们维护的最简单的 `messages` 列表

````
messages = [
    {"role": "user", "content": "你好"},
    {"role": "assistant", "content": "你好，有什么可以帮你？"},
    {"role": "user", "content": "解释一下 Python 列表"},
]
````

每条消息主要包含两个字段：

- `role`：这条消息来自哪一方。
- `content`：这条消息的具体内容，可以是字符串（str），也可以是内容块（block）列表。



通过我们的 `client` 返回的 `JSON`转换成我们的`response`，然后提取 `response.content`

在这段非流式调用中，API 返回的 `JSON` 响应体大致如下。下面只是示意，字段值是假设的：

````json
{
  "id": "msg_example",
  "type": "message",
  "role": "assistant",
  "model": "某个模型",
  
  "content": [
    {
      "type": "text",
      "text": "我先查看当前目录。"
    },
    {
      "type": "tool_use",
      "id": "toolu_example",
      "name": "bash",
      "input": {
        "command": "ls"
      }
    }
  ], # 这是 agent 从模型那里需要的主要内容
  
  "stop_reason": "tool_use",
  "stop_sequence": null,
  "usage": {
    "input_tokens": 120,
    "output_tokens": 40
  }
}
````

在这里我们将response.content作为一个列表，然后列表中的每一个元素作为一个`block`

````python
就会有
block[0] = {
      "type": "text",
      "text": "我先查看当前目录。"
    }
    
block[1] = {
      "type": "tool_use",
      "id": "toolu_example",
      "name": "bash",
      "input": {
        "command": "ls"
      }
````





最后我们维护的`messages`会变成下面的样子：

````python
messages = [
    # 1. 用户提出任务
    {
        "role": "user",
        "content": "看看当前目录有哪些文件",
    },

    # 2. 模型请求调用工具
    {
        "role": "assistant",
        "content": [
            {
                "type": "tool_use",
                "id": "tool_01",
                "name": "bash",
                "input": {"command": "ls"},
            }
        ],
    },

    # 3. 你的程序执行工具，再把结果交给模型
    {
        "role": "user",
        "content": [
            {
                "type": "tool_result",
                "tool_use_id": "tool_01",
                "content": "README.md\ncode.py",
            }
        ],
    },

    # 4. 模型根据工具结果回答
    {
        "role": "assistant",
        "content": [
            {
                "type": "text",
                "text": "当前目录有 README.md 和 code.py。",
            }
        ],
    },
]
````





### 1.2 `Tool-use`

Tool-use 就是：**模型提出工具调用请求，程序执行工具，再把结果交给模型，让它继续判断。**

例如，用户说“读取 README.md，告诉我这个项目做什么”，整个过程是：

```
用户提出任务
    ↓
模型请求调用 read_file
    ↓
程序读取 README.md
    ↓
程序把文件内容作为 tool_result 返回
    ↓
模型根据文件内容回答，或继续调用工具
```



这里有两个不同的职责：

- **模型（LLM）负责决策**：调用哪个工具、传什么参数、看到结果后做什么。
- **程序（Harness）负责执行**：调用实际函数，访问文件或运行命令，再返回结果。

所以，模型生成一段工具调用，并不意味着文件已经被读取；程序执行对应函数后，才真正发生了操作。

从程序实现来看，一个工具需要三个部分：

| 部分     | 作用                         | 例子            |
| -------- | ---------------------------- | --------------- |
| 工具定义 | 告诉模型有哪些能力、怎样传参 | `TOOLS`         |
| 处理函数 | 实际完成操作                 | `run_read()`    |
| 分发表   | 把模型请求的工具名对应到函数 | `TOOL_HANDLERS` |



以 `read_file` 为例，它的定义是：

````
{
    "name": "read_file",
    "description": "Read file contents.",
    "input_schema": {
        "type": "object",
        "properties": {
            "path": {"type": "string"},
            "limit": {"type": "integer"},
        },
        "required": ["path"],
    },
}
````

各字段的含义：

- `name`：工具名，程序用它寻找处理函数。
- `description`：工具的用途，帮助模型选择工具。
- `input_schema`：参数的结构。
- `properties`：有哪些参数，以及它们的类型。
- `required`：哪些参数必须提供。

这里的 `path` 必填，`limit` 可选；在这一章中，`limit` 表示最多读取多少行。

**模型收到的是工具说明；真正的 Python 函数仍在本地程序里。** Schema 描述了期望的参数格式，程序仍然需要处理参数错误和执行失败。



模型怎么请求调用工具？

````
{
  "type": "tool_use",
  "id": "tool_example",
  "name": "read_file",
  "input": {
    "path": "README.md",
    "limit": 20
  }
}
````

| 字段    | 含义                             |
| ------- | -------------------------------- |
| `type`  | 表示这是工具调用请求             |
| `id`    | 标识这一次调用，后面用来匹配结果 |
| `name`  | 请求使用的工具                   |
| `input` | 传给工具的参数                   |

要注意，**`response.content` 是内容块列表**，其中可以同时有 `text` 和 `tool_use`，也可以有多个 `tool_use`。因此程序需要筛选，而不能只看第一个块。



根据工具名找到对应函数：

````python
TOOL_HANDLERS = {
    "bash": run_bash,
    "read_file": run_read,
    "write_file": run_write,
    "edit_file": run_edit,
    "glob": run_glob,
}

handler = TOOL_HANDLERS.get(block.name)
output = (
    handler(**block.input)
    if handler
    else f"Unknown: {block.name}"
)
````

新增工具时通常要完成三件事：实现处理函数、添加工具定义、注册到分发表。**Agent Loop 的基本结构可以继续复用。**



`Tool-use` 接入 `Agent Loop` 整个循环

````
1. 把 messages 和 TOOLS 发给模型
2. 把 response.content 作为 assistant 消息保存
3. 筛选其中的 tool_use
4. 没有 tool_use → 本章代码结束循环
5. 有 tool_use → 查分发表，执行工具
6. 把结果作为 user 消息保存
7. 再次调用模型
````



几个注意点：

- **一次返回多个工具调用，不等于并行执行。** s02 用 `for` 循环，按返回顺序逐个执行。
- **同一批调用的参数在模型回复时就已确定。** 如果后一个操作需要根据前一个工具的输出决定参数，就需要先返回结果，再让模型生成下一次调用。
- **工具报错也是模型需要看到的反馈。** 本章会把许多异常转换成 `Error: ...` 返回，模型才能据此调整下一步。
- **工具执行成功，不等于整个任务完成。** 后续可能还需要读取检查、运行测试或继续调用其他工具。



### 1.3 `Permission`

`Tool-use ` 解决了“模型如何使用多个工具”：模型返回 `tool_use`，程序根据工具名找到处理函数并执行。

但工具可以读取文件、覆盖内容、删除数据，因此执行之前还需要判断：

> **这次操作能不能直接执行？需要用户确认，还是必须禁止？**

例如，用户说“清理一下项目”，模型可能请求删除文件。程序必须在执行删除命令之前检查权限。

这里各部分的职责是：

| 部分     | 职责                     |
| -------- | ------------------------ |
| 模型     | 根据任务提出操作请求     |
| 权限系统 | 根据规则判断是否允许操作 |
| 工具函数 | 执行已经通过检查的操作   |

权限检查属于 **Harness 的执行逻辑**。系统提示词可以提醒模型注意安全，代码中的检查负责实际拦截。



整体流程：

````
用户提出任务
    ↓
模型返回 tool_use
    ↓
权限检查
    ├─ 允许 → 执行工具 → 返回执行结果
    └─ 拒绝 → 跳过工具 → 返回拒绝信息
    ↓
模型根据 tool_result 继续判断
````





这里设计了三道闸门来做权限管理：

| 闸门          | 判断内容                   | 处理方式       |
| ------------- | -------------------------- | -------------- |
| 1. 硬拒绝列表 | 是否命中明确禁止的命令     | 直接拒绝       |
| 2. 规则匹配   | 是否属于需要用户确认的操作 | 命中后进入审批 |
| 3. 用户审批   | 用户是否允许本次操作       | 允许或拒绝     |

优先级如下：

````
命中硬拒绝列表 → 直接拒绝，不询问用户
未命中硬拒绝，但命中审批规则 → 询问用户
两者都未命中 → 直接放行
````



几个例子理解执行路径，以下假设工作区是 `/project`，并使用表中指定的工具：

| 工具请求                             | 权限处理                 |
| ------------------------------------ | ------------------------ |
| `read_file(path="README.md")`        | 工作区内，直接放行       |
| `write_file(path="test.txt", ...)`   | 工作区内，直接放行       |
| `bash(command="rm test.txt")`        | 命中审批规则，询问用户   |
| `read_file(path="/other/notes.txt")` | 工作区外，询问用户       |
| `bash(command="sudo ...")`           | 命中硬拒绝列表，直接拒绝 |



### 1.4 `Hooks`-在固定时机执行扩展逻辑

为什么需要 Hook？

`Permission`已经在工具执行前加入了权限检查：

````python
if not check_permission(block):
    # 返回拒绝信息，跳过执行
    continue
````

但如果继续增加日志、输出检查、结束统计，就需要不断往循环中添加代码。

**在流程中的固定位置设置事件，把扩展逻辑注册为回调函数；事件发生时，程序调用这些函数。**

这里设计的整体做法：
````
工具执行前 → 权限检查、记录日志
工具执行后 → 检查输出大小
循环退出前 → 打印调用统计
````

Hook 可以理解为一个“扩展接口”，回调函数是挂在这个接口上的具体逻辑。



Hook 和 Tool 的区别

| 对比     | Tool                         | Hook                           |
| -------- | ---------------------------- | ------------------------------ |
| 谁触发   | 模型通过 `tool_use` 请求     | 程序在固定流程位置触发         |
| 如何选择 | 模型选择工具名和参数         | 程序按事件查找已注册的回调     |
| 主要用途 | 读取文件、执行命令等具体操作 | 权限检查、日志、收尾等流程扩展 |
| 本章例子 | `read_file`、`bash`          | `permission_hook`、`log_hook`  |

**模型决定调用什么工具，程序决定什么时候触发 Hook。**

本章的 Hook 不放进 `TOOLS`，也不需要模型生成一个“调用 Hook”的请求。在固定的位置Hook会自动调用。



这里整体的流程

| 事件               | 触发时机                           | 回调收到的参数  | 本章实现           |
| ------------------ | ---------------------------------- | --------------- | ------------------ |
| `UserPromptSubmit` | 用户提交有效输入后，加入消息历史前 | `query`         | 打印当前工作目录   |
| `PreToolUse`       | 每次工具执行前                     | `block`         | 权限检查、调用日志 |
| `PostToolUse`      | 工具处理函数返回后，保存结果前     | `block, output` | 大输出提醒         |
| `Stop`             | 模型没有请求工具，循环准备返回时   | `messages`      | 打印工具调用统计   |

````
用户输入
    ↓
UserPromptSubmit
    ↓
加入 messages，调用模型
    ↓
模型返回回复
    ├─ 有 tool_use
    │     ↓
    │   PreToolUse
    │     ├─ 拒绝 → 保存拒绝结果
    │     └─ 通过 → 执行工具 → PostToolUse → 保存执行结果
    │     ↓
    │   把结果交回模型，继续循环
    │
    └─ 没有 tool_use
          ↓
        Stop
          ├─ 要求继续 → 添加消息，再次调用模型
          └─ 允许结束 → 返回
````



- **`context_inject_hook` 当前只打印工作目录。** 虽然名字包含“注入”，它没有修改 `query` 或 `messages`，打印内容也不会自动成为模型上下文。
- **`large_output_hook` 只提醒，不截断。** 它检查输出是否超过 100000 个字符，原来的 `output` 仍会作为工具结果返回。
- **PostToolUse 不等于操作成功。** 工具返回 `"Error: ..."` 时，这个回调仍然会触发；关键是处理函数已经返回。
- **统计包含被拒绝的调用。** `summary_hook` 统计的是整个历史中的 `tool_result`，拒绝结果也算在内，多次用户输入之间会累计。
- **Hook 本身不提供安全保证。** 能否正确拦截，仍取决于权限回调中的具体规则。
- **加入 Hook 机制时，需要修改流程的触发位置。** 机制建立后，在已有事件上增加扩展，通常只需实现并注册回调。





## 2. Harness

### 2.1 TodoWrite——把计划和进度记录下来

 **为什么需要 TodoWrite？**

前几章已经让 Agent 能调用工具、检查权限，并在关键位置触发 Hook。

但遇到复杂任务时，Agent 仍可能漏掉步骤。例如：

````
任务：添加类型注解、补充文档、运行测试

开始修改代码
    ↓
测试失败，转去修复
    ↓
修复结束，却忘记补充文档
````

增加一个 `todo_write` **工具**，让模型把任务拆成步骤，并在执行过程中更新状态。

它帮助模型持续看到：

- 需要完成哪些事情。
- 当前正在做哪一步。
- 哪些已经完成，哪些还没开始。

**TodoWrite 管理的是计划状态；读取文件、修改代码、运行测试仍由原来的工具完成。**



每条任务有两个字段：

````json
{
  "content": "给函数添加类型注解",
  "status": "pending"
}
````

| 字段      | 含义             |
| --------- | ---------------- |
| `content` | 要完成的具体步骤 |
| `status`  | 这一步当前的状态 |

| status        | 含义     | 显示标记 |
| ------------- | -------- | -------- |
| `pending`     | 尚未开始 | `[ ]`    |
| `in_progress` | 正在进行 | `[--]`   |
| `completed`   | 已经完成 | `[√]`    |



模型通过 `tool_use` 请求调用 `todo_write`：

````json
{
  "type": "tool_use",
  "id": "todo_01",
  "name": "todo_write",
  "input": {
    "todos": [
      {
        "content": "添加类型注解",
        "status": "in_progress"
      },
      {
        "content": "补充函数文档",
        "status": "pending"
      },
      {
        "content": "运行测试并修复问题",
        "status": "pending"
      }
    ]
  }
}
````



第一步完成后，模型再次调用工具，提交更新后的列表：

````json
{
  "todos": [
    {
      "content": "添加类型注解",
      "status": "completed"
    },
    {
      "content": "补充函数文档",
      "status": "in_progress"
    },
    {
      "content": "运行测试并修复问题",
      "status": "pending"
    }
  ]
}
````

这里最重要的是：

> **每次提交的列表会整体替换旧列表。**

它不是“只修改某一项”的接口。如果只传第二项，原来的第一项和第三项就会从当前列表中消失。

同样，传入空列表 `[]` 会清空计划。



`TodoManager` 负责保存、校验和渲染任务列表：

```python
class TodoManager:
    def __init__(self):
        self.items = []

    def update(self, todos):
        # 解析输入
        # 校验每一项
        # 全部通过后，替换当前列表
        self.items = validated
        return self.render()

    def render(self):
        # 把任务列表转换成可读文本
        ...
```

实际更新顺序：

````
解析输入 → 检查列表 → 校验所有任务 → 替换旧状态 → 渲染结果
````



处理函数，这里处理函数会调用创建好的对象`TODO = TodoManager()`

````python
def run_todo_write(todos: list | str) -> str:
    try:
        output = TODO.update(todos)
    except ValueError as e:
        return f"Error: {e}"

    print(output)
    return output
````

返回结果如下：

````
[√] 添加类型注解
[--] 补充函数文档
[ ] 运行测试并修复问题

(1/3 completed)
````

为了避免模型一直执行操作却忘记更新 TODO，循环增加了计数器：

````
本轮使用 todo_write → 计数清零
本轮没有使用 → 计数加一
连续三轮没有使用 → 追加提醒，再清零
````



- **计划不会自动执行。** 标记某项为 `in_progress` 后，模型仍需要调用文件或命令工具完成工作。
- **完成状态由模型提交。** 程序不会因为某项被标记为 `completed`，就自动验证文件或测试结果。
- **未完成的 TODO 不会阻止结束。** 当前 Stop Hook 只打印统计，没有检查计划是否全部完成。
- **TODO 只保存在内存里。** 同一次程序运行中的多次用户输入共用 `TODO`；程序重启后不会恢复。
- **提醒计数与 TODO 的生命周期不同。** `rounds_since_todo` 在每次进入 `agent_loop()` 时重新初始化，不跨用户输入累计。
- **调用失败也可能重置提醒计数。** 当前代码根据工具名设置 `used_todo`；即使 `todo_write` 返回校验错误，该轮仍会被记为使用过它。



### 2.2 Subagent——给子任务一段独立上下文

**为什么需要子 Agent？**

主 Agent 处理复杂任务时，读取文件、搜索代码等中间结果会不断积累在 `messages` 中，占用上下文。

可以把一个明确的子任务交给子 Agent，让它独立探索，最后只返回结论。

> 就是在不占用大量上下文的同时能够完成特定的任务。

````
主 Agent：修复一个 bug
    ↓ task
子 Agent：查找相关函数和调用链
    ↓ 返回最终文本
主 Agent：根据结论继续修复
````



子 Agent 本质上是：**使用新消息列表运行另一段 Agent Loop。**

````Python
def run_subagent(prompt):
    messages = [{"role": "user", "content": prompt}]
    # 这个messages是根据父agent 给的 prompt 建立的，每次进子 agent 都是全新的 messages

    # 用自己的 messages 调用模型、执行工具
    # 结束后提取并返回最终文本
````

它不会复制父 Agent 的对话历史。因此，父 Agent 需要在 `prompt` 中明确说明任务、必要背景和期望返回的内容。



通过新增的 `task` 工具调用子agent，沿用前面学过的工具分发机制：

````Python
TOOLS = [*BASE_TOOLS, TASK_TOOL]
TOOL_HANDLERS = {**BASE_HANDLERS, "task": run_subagent}
````



几个边界：

| 项目     | 本章实现                                           |
| -------- | -------------------------------------------------- |
| 上下文   | 子 Agent 使用全新的 `messages`                     |
| 返回内容 | 正常结束时只返回最终文本，中间消息不进入父上下文   |
| 执行方式 | 同步运行，父 Agent 等待子任务结束                  |
| 工作区   | 共享进程和 `WORKDIR`，文件修改彼此可见             |
| 工具     | 子 Agent 有五个基础工具，没有 `task`，不能继续委派 |
| 权限     | 父子工具调用共用权限和 Hook 机制                   |
| 轮数限制 | 子循环最多调用模型 30 轮，超限返回停止提示         |

**这里隔离的是对话上下文，文件系统仍然共享。** 子 Agent 适合承担范围明确的探索或独立任务；返回结论后，由主 Agent 接着处理整体任务。



### 2.3 Skill Loading——技能按需加载

Agent 处理不同任务时，需要不同的知识和规范，例如代码审查流程、PDF 处理方法。

如果把所有说明都放进 system prompt，无关内容也会占用上下文。

> **先让模型看到技能名称和简介，需要时再读取完整说明。**

| 内容            | 放在哪里      | 何时进入模型上下文       |
| --------------- | ------------- | ------------------------ |
| 技能名称、描述  | system prompt | 构建提示词时             |
| 完整 `SKILL.md` | `tool_result` | 模型调用 `load_skill` 时 |



**Skill 长什么样？**

每个技能放在独立目录中：

```
skills/
  code-review/
    SKILL.md
  pdf/
    SKILL.md
```

`SKILL.md` 由元数据和正文组成，例如：

```
---
name: code-review
description: 审查代码的正确性、安全性和可维护性。
---

# 代码审查流程

1. 理解代码用途。
2. 检查潜在问题。
3. 给出修改建议。
```

- `name`：模型加载技能时使用的名称。
- `description`：帮助模型判断什么时候使用。
- 正文：具体知识、规范和操作步骤。



**SkillLoader **

| 方法                  | 作用                                     |
| --------------------- | ---------------------------------------- |
| `scan()`              | 扫描 `skills/*/SKILL.md`，读取并保存内容 |
| `parse_frontmatter()` | 解析开头的 YAML 元数据                   |
| `catalog()`           | 生成只有名称和描述的技能目录             |
| `load(name)`          | 根据名称返回完整文件内容                 |

启动时建立的注册表类似：

```
self.skills[name] = {
    "name": name,
    "description": description,
    "content": content,
}
```

如果没有提供名称，使用目录名；没有描述，则使用正文第一行作为简介。

````
模型看到技能目录
    ↓
判断 code-review 适用于当前任务
    ↓
请求 load_skill(name="code-review")
    ↓
程序返回完整 SKILL.md，保存为 tool_result
    ↓
模型读取说明，再调用其他工具完成审查
````

Skill、Tool、Subagent 的区别：

| 概念     | 提供什么                 | 例子               |
| -------- | ------------------------ | ------------------ |
| Tool     | 执行具体操作的接口       | 读取文件、运行命令 |
| Skill    | 完成某类任务的知识与流程 | 代码审查规范       |
| Subagent | 使用独立上下文处理子任务 | 委派一次代码探索   |



**几个细节**

- **按需加载指进入模型上下文。** 当前实现启动时已经把技能全文读入内存，调用工具时再返回给模型。
- **正文进入消息历史，不会修改 system prompt。** 后续请求会继续携带这段历史，加载后仍然占用上下文。
- **按名称查注册表。** `name` 不会被直接当成文件路径；名称不存在时返回错误和可用技能列表。
- **加载不是强制执行。** 系统提示词引导模型在适用时读取技能，代码没有强制要求它先加载再行动。
- **只返回 `SKILL.md`。** 文档引用的其他文件，需要模型另行读取；当前实现不会自动展开。





### 2.4Context Compact——上下文压缩

当 Agent 执行了很多的操作之后，用户的输入、Agent 工具处理后的结果（tool_result）、模型的调用（assistant.content）都会放在 messages 中保存，这样会导致 messages 越来越大，最后会超过模型能接收的最大上下文长度。

对整个 agent_loop 做上下文压缩管理：

````python
# 整个压缩的主体
messages[:] = COMPACTOR.prepare(messages, active_request)
````

整体流程：

````
1.tool_result_budget # 对工具结果压缩，每轮都会执行
         ↓
2.snip_compact # 每轮都执行，消息数超过 50 时生效
         ↓
  if（estimate_chars > 50000） # 对前两轮处理完后的总字符数做判断
3.micro_compact/fit_tool_results # 先把旧的工具结果换成路径，再不够就把所有结果都换成预览
         ↓
  if（estimate_chars > 50000）
4.compact_history # 让 LLM 把整段历史写成摘要
````

核心思想就一句话：先用便宜的方法，不够了再用贵的。



