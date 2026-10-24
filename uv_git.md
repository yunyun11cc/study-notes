# 🚀 uv 与 Git 常用命令速查手册

这份手册汇总了现代 Python 包管理工具 **`uv`** 与版本控制工具 **`Git`** 的高频核心指令，以及两者在日常项目中的最佳实践配合流程。

---

## 第一部分：📦 `uv` 常用命令速查

### 1. 安装与自更新
```bash
# macOS / Linux 官方独立安装
curl -LsSf https://astral.sh/uv/install.sh | sh

# Windows (PowerShell) 安装
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"

# Homebrew 安装 (macOS)
brew install uv

# 更新 uv 自身到最新版本
uv self update
```

### 2. Python 版本管理（替代 pyenv / conda）
| 操作说明 | 命令 |
| :--- | :--- |
| 查看已安装和可安装的 Python 版本 | `uv python list` |
| 下载并安装指定的 Python 版本 | `uv python install 3.12` |
| 固定当前项目的 Python 版本（生成 `.python-version`） | `uv python pin 3.12` |
| 卸载指定的 Python 版本 | `uv python uninstall 3.10` |

### 3. 现代项目依赖管理（核心工作流）
| 操作说明 | 命令 |
| :--- | :--- |
| 新建项目并生成目录骨架 | `uv init my_project` |
| 在当前已有目录初始化项目 | `uv init` |
| 添加生产环境依赖 | `uv add fastapi requests` |
| 添加指定版本限制的依赖 | `uv add "pydantic>=2.0"` |
| 添加开发环境依赖（测试、代码检查等） | `uv add --dev pytest ruff` |
| 从 `requirements.txt` 批量导入依赖 | `uv add -r requirements.txt` |
| 移除某个依赖包 | `uv remove requests` |
| **根据 `uv.lock` 同步/构建本地虚拟环境** | `uv sync` |
| 查看项目的依赖关系树 | `uv tree` |
| 升级所有依赖包并更新锁文件 | `uv lock --upgrade` |
| 仅升级指定的依赖包 | `uv lock --upgrade-package fastapi` |

### 4. 运行代码与全局工具（无需手动激活虚拟环境）
```bash
# 在项目虚拟环境中运行脚本
uv run python main.py

# 运行项目环境内的命令行工具（如 pytest）
uv run pytest

# 临时附带某个包运行一次性脚本（不写入项目依赖）
uv run --with httpx python test.py

# 临时下载并运行全局 CLI 工具（用完即弃，替代 pipx）
uvx ruff check .

# 全局持久化安装 CLI 工具
uv tool install ruff
```

### 5. 传统 `pip` / `venv` 兼容模式与缓存清理
```bash
# 仅创建虚拟环境（默认生成 .venv 目录）
uv venv

# 直接向当前虚拟环境安装包（不修改 pyproject.toml）
uv pip install -r requirements.txt

# 导出锁文件为传统的 requirements.txt（用于兼容旧部署流程）
uv export --format requirements-txt > requirements.txt

# 清理无用或全量缓存（释放磁盘空间）
uv cache prune
uv cache clean
```

---

## 第二部分：🌿 `Git` 常用命令速查

### 1. 初始配置與仓库初始化
```bash
# 配置全局用户名与邮箱
git config --global user.name "Your Name"
git config --global user.email "you@example.com"

# 在当前目录初始化 Git 仓库
git init

# 克隆远程仓库到本地
git clone <远程仓库地址>
```

### 2. 日常提交与状态查看
| 操作说明 | 命令 |
| :--- | :--- |
| 查看当前工作区与暂存区状态 | `git status` |
| 查看未暂存的文件修改细节 | `git diff` |
| 将指定文件添加到暂存区 | `git add <文件名>` |
| 将所有修改和新文件添加到暂存区 | `git add .` |
| 提交暂存区内容到本地仓库 | `git commit -m "feat: 添加用户登录接口"` |
| 修改最后一次提交的信息或补充漏交文件 | `git commit --amend` |

### 3. 分支管理（推荐使用现代 `git switch` 指令）
| 操作说明 | 命令 |
| :--- | :--- |
| 查看本地所有分支（加 `-a` 查看含远程的所有分支） | `git branch` / `git branch -a` |
| 创建并切换到新分支 | `git switch -c feat/login` *(旧写法：`git checkout -b`)* |
| 切换到已有的分支 | `git switch main` *(旧写法：`git checkout main`)* |
| 将指定分支合并到当前所在分支 | `git merge feat/login` |
| 删除已合并的本地分支（强制删除用 `-D`） | `git branch -d feat/login` |

### 4. 远程同步与协作
| 操作说明 | 命令 |
| :--- | :--- |
| 查看已关联的远程仓库地址 | `git remote -v` |
| 关联远程仓库 | `git remote add origin <远程仓库地址>` |
| 拉取远程分支最新代码并合并 | `git pull` |
| 拉取远程最新代码并以变基方式保持线性历史 | `git pull --rebase` |
| 首次推送本地新分支到远程并建立追踪关系 | `git push -u origin <分支名>` |
| 常规推送本地提交到远程 | `git push` |

### 5. 撤销、回退与救场指令
| 操作说明 | 命令 |
| :--- | :--- |
| 丢弃工作区某个文件的未暂存修改 | `git restore <文件名>` |
| 将文件从暂存区撤回工作区（取消 `git add`） | `git restore --staged <文件名>` |
| **软回退**：撤销上一次 commit，但保留写好的代码在暂存区 | `git reset --soft HEAD~1` |
| **硬回退**：彻底丢弃上一次 commit 及对应修改（慎用） | `git reset --hard HEAD~1` |
| 生成一个反向 commit 来抵消某次历史提交（适合已推送到远程的代码） | `git revert <commit-id>` |
| 临时封存当前写了一半的代码（切换分支救火时常用） | `git stash` |
| 恢复最近一次封存的代码并删除封存记录 | `git stash pop` |

### 6. 日志与历史排查
```bash
# 单行紧凑显示提交历史与分支图谱
git log --oneline --graph --all

# 查看所有分支移动和 reset 的操作记录（误删分支/硬回退后的救命稻草）
git reflog
```

---

## 第三部分：🤝 `uv` + `Git` 协同工作流最佳实践

### 1. 从 0 创建新项目并推送到 Git
```bash
# 1. 使用 uv 初始化项目（uv 会自动帮你執行 git init 并生成 .gitignore）
uv init my_awesome_project --python 3.12
cd my_awesome_project

# 2. 添加项目依赖
uv add fastapi uvicorn
uv add --dev pytest ruff

# 3. 编写代码并测试运行
uv run python main.py

# 4. 提交到 Git 并推送到远程
git add .
git commit -m "chore: 初始化项目与 uv 依赖锁文件"
git branch -M main
git remote add origin git@github.com:username/my_awesome_project.git
git push -u origin main
```

### 2. 团队成员克隆项目并快速还原环境
```bash
# 1. 克隆仓库
git clone git@github.com:username/my_awesome_project.git
cd my_awesome_project

# 2. 一键创建虚拟环境并精确安装 uv.lock 中的所有依赖
uv sync

# 3. 直接运行项目
uv run uvicorn main:app --reload
```

### 3. `.gitignore` 黄金准则
在 `uv` 与 `Git` 配合的项目中，请始终确保以下版本控制原则：
* ✅ **必须提交到 Git**：
  * `pyproject.toml`（项目依赖声明）
  * `uv.lock`（跨平台精确版本锁定文件，保证团队环境 100% 一致）
  * `.python-version`（锁定 Python 版本）
* ❌ **绝对不要提交到 Git**（`uv init` 默认已写入 `.gitignore`）：
  * `.venv/`（本地虚拟环境目录）
  * `__pycache__/`、`*.pyc`（Python 字节码缓存）