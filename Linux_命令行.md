---
title: Linux 命令行常用速查
created: 2026-05-07
updated: 2026-05-07
tags:
  - Linux
  - 命令行
  - 服务器
  - 深度学习
  - 终端
  - SSH
  - tmux
aliases:
  - Linux 终端速查
  - 服务器跑代码命令
  - Linux CLI
status: evergreen
---

# Linux 命令行常用速查

> [!summary] 使用目标
> 这份笔记主要服务于：**在服务器上跑代码、管理文件、查看日志、传输文件、管理进程、查看 GPU/内存/磁盘状态**。  
> 不追求一次性学成 Linux 系统管理员，先掌握科研和深度学习项目中最常用的一批命令。

---

## 目录

- [[#一、最常用命令总表]]
- [[#二、Linux 命令的基本格式]]
- [[#三、路径基础]]
- [[#四、文件和目录操作]]
- [[#五、查看文本和日志]]
- [[#六、搜索文件内容]]
- [[#七、查找文件]]
- [[#八、管道和重定向]]
- [[#九、服务器跑代码必会]]
- [[#十、tmux 终端复用]]
- [[#十一、查看系统资源]]
- [[#十二、压缩和解压]]
- [[#十三、远程登录和传文件]]
- [[#十四、权限管理]]
- [[#十五、环境变量]]
- [[#十六、Python 项目常用命令]]
- [[#十七、Git 常用命令]]
- [[#十八、编辑文件]]
- [[#十九、命令历史和自动补全]]
- [[#二十、服务器训练代码完整流程]]
- [[#二十一、我的常用命令清单]]
- [[#二十二、常见危险命令提醒]]

---

# 一、最常用命令总表

| 类别 | 命令 | 作用 | 常用例子 |
|---|---|---|---|
| 查看位置 | `pwd` | 显示当前所在目录 | `pwd` |
| 切换目录 | `cd` | 进入某个文件夹 | `cd project`、`cd ..`、`cd ~` |
| 查看文件 | `ls` | 列出当前目录内容 | `ls`、`ls -lh`、`ls -lha` |
| 创建文件夹 | `mkdir` | 创建目录 | `mkdir logs`、`mkdir -p data/raw` |
| 创建空文件 | `touch` | 创建空文件 | `touch train.py` |
| 复制 | `cp` | 复制文件或文件夹 | `cp a.py b.py`、`cp -r data data_bak` |
| 移动/改名 | `mv` | 移动或重命名 | `mv old.py new.py` |
| 删除 | `rm` | 删除文件或文件夹 | `rm a.txt`、`rm -r logs` |
| 查看文本 | `cat` | 一次性输出文件内容 | `cat config.yaml` |
| 分页查看 | `less` | 分页查看长文件 | `less train.log` |
| 看开头 | `head` | 查看前几行 | `head -n 50 train.log` |
| 看结尾 | `tail` | 查看后几行 | `tail -f train.log` |
| 搜索文本 | `grep` | 在文件中搜索关键词 | `grep "loss" train.log` |
| 查找文件 | `find` | 按名字或条件查文件 | `find . -name "*.py"` |
| 磁盘空间 | `df` | 查看磁盘总体空间 | `df -h` |
| 文件夹大小 | `du` | 查看目录占用大小 | `du -sh data` |
| 内存情况 | `free` | 查看内存 | `free -h` |
| 进程查看 | `ps` | 查看进程 | `ps aux \| grep python` |
| 实时资源 | `top` / `htop` | 查看 CPU/内存占用 | `top`、`htop` |
| 杀进程 | `kill` | 结束进程 | `kill 12345`、`kill -9 12345` |
| 后台运行 | `nohup` | 断开终端后继续运行 | `nohup python train.py > train.log 2>&1 &` |
| 终端复用 | `tmux` | 服务器跑代码神器 | `tmux new -s train` |
| 压缩解压 | `tar` | 打包/解压 `.tar.gz` | `tar -xzvf data.tar.gz` |
| 下载 | `wget` / `curl` | 从网络下载文件 | `wget URL` |
| 远程登录 | `ssh` | 登录服务器 | `ssh user@ip` |
| 传文件 | `scp` | 本地和服务器互传文件 | `scp file user@ip:/path` |
| 同步文件 | `rsync` | 更强的远程同步 | `rsync -av data/ user@ip:/data/` |
| 权限修改 | `chmod` | 修改文件执行权限 | `chmod +x run.sh` |
| 环境变量 | `export` | 设置环境变量 | `export CUDA_VISIBLE_DEVICES=0` |
| 命令历史 | `history` | 查看历史命令 | `history` |
| 查看命令位置 | `which` | 查看程序路径 | `which python` |
| 帮助文档 | `man` / `--help` | 查看命令用法 | `ls --help`、`man ls` |

---

# 二、Linux 命令的基本格式

Linux 命令一般是：

```bash
命令 选项 参数
```

例如：

```bash
ls -lh /home/yuri/project
```

含义：

| 部分 | 含义 |
|---|---|
| `ls` | 列出目录内容 |
| `-l` | 用详细格式显示 |
| `-h` | 文件大小用 KB、MB、GB 等可读形式显示 |
| `/home/yuri/project` | 要查看的目录 |

很多选项可以合并：

```bash
ls -l -h
```

等价于：

```bash
ls -lh
```

---

# 三、路径基础

## 1. 查看当前目录

```bash
pwd
```

可能输出：

```bash
/home/yuri/project
```

表示你现在位于 `/home/yuri/project` 目录下。

---

## 2. 绝对路径和相对路径

### 绝对路径

从根目录 `/` 开始写：

```bash
/home/yuri/project/train.py
```

### 相对路径

从当前目录开始写：

```bash
train.py
```

或者：

```bash
./train.py
```

其中 `./` 表示当前目录。

---

## 3. 常见路径符号

| 符号 | 含义 |
|---|---|
| `/` | 根目录 |
| `.` | 当前目录 |
| `..` | 上一级目录 |
| `~` | 当前用户的家目录 |
| `-` | 上一次所在目录 |

例子：

```bash
cd ..
```

回到上一级目录。

```bash
cd ~
```

回到家目录。

```bash
cd -
```

回到上一次所在目录。

---

# 四、文件和目录操作

## 1. 查看目录内容：`ls`

```bash
ls
```

详细显示：

```bash
ls -l
```

更常用：

```bash
ls -lh
```

查看隐藏文件：

```bash
ls -a
```

最常用组合：

```bash
ls -lha
```

> [!tip] 记忆
> `ls -lha` 基本可以当作默认查看命令。  
> `l` = long，详细信息；  
> `h` = human readable，人类可读大小；  
> `a` = all，显示隐藏文件。

---

## 2. 切换目录：`cd`

```bash
cd project
```

回到上一级：

```bash
cd ..
```

回到家目录：

```bash
cd ~
```

进入绝对路径：

```bash
cd /home/yuri/project
```

---

## 3. 创建文件夹：`mkdir`

创建一个文件夹：

```bash
mkdir logs
```

创建多级目录：

```bash
mkdir -p data/raw
```

一次性创建常用项目目录：

```bash
mkdir -p data/raw data/processed logs checkpoints outputs
```

---

## 4. 创建空文件：`touch`

```bash
touch train.py
```

---

## 5. 复制文件或文件夹：`cp`

复制文件：

```bash
cp train.py train_backup.py
```

复制文件夹：

```bash
cp -r data data_backup
```

`-r` 表示递归复制整个目录。

---

## 6. 移动或重命名：`mv`

重命名：

```bash
mv old_train.py train.py
```

移动文件：

```bash
mv train.py src/
```

---

## 7. 删除：`rm`

删除文件：

```bash
rm test.txt
```

删除文件夹：

```bash
rm -r logs
```

强制删除：

```bash
rm -rf logs
```

> [!danger] 谨慎使用 `rm -rf`
> `rm -rf` 不会进回收站，删了通常就没了。  
> 建议先用 `ls` 或 `find` 确认目标，再删除。

---

# 五、查看文本和日志

服务器跑代码时，经常查看：

- `.py`
- `.sh`
- `.log`
- `.yaml`
- `.json`
- `.txt`

---

## 1. 一次性查看：`cat`

```bash
cat config.yaml
```

适合查看短文件，不适合看很长的日志。

---

## 2. 分页查看：`less`

```bash
less train.log
```

常用按键：

| 按键 | 作用 |
|---|---|
| `空格` | 向下翻页 |
| `b` | 向上翻页 |
| `/关键词` | 搜索关键词 |
| `n` | 下一个搜索结果 |
| `q` | 退出 |

例如在日志里搜索 loss：

```bash
/loss
```

退出：

```bash
q
```

---

## 3. 查看开头：`head`

默认看前 10 行：

```bash
head train.log
```

看前 50 行：

```bash
head -n 50 train.log
```

---

## 4. 查看结尾：`tail`

默认看最后 10 行：

```bash
tail train.log
```

看最后 100 行：

```bash
tail -n 100 train.log
```

实时追踪日志：

```bash
tail -f train.log
```

退出实时追踪：

```bash
Ctrl + C
```

> [!tip] 训练时最常用
> 如果训练输出写到了 `train.log`，就用：
>
> ```bash
> tail -f train.log
> ```
>
> 这样可以实时看 loss、epoch、报错信息。

---

# 六、搜索文件内容

## 1. 在单个文件中搜索：`grep`

搜索日志中所有包含 `loss` 的行：

```bash
grep "loss" train.log
```

忽略大小写：

```bash
grep -i "error" train.log
```

显示行号：

```bash
grep -n "error" train.log
```

常用组合：

```bash
grep -in "error" train.log
```

---

## 2. 在整个项目中搜索

```bash
grep -rn "batch_size" .
```

含义：

| 部分 | 含义 |
|---|---|
| `grep` | 搜索文本 |
| `-r` | 递归搜索目录 |
| `-n` | 显示行号 |
| `"batch_size"` | 要搜索的关键词 |
| `.` | 当前目录 |

常用例子：

```bash
grep -rn "CUDA_VISIBLE_DEVICES" .
```

```bash
grep -rn "class" .
```

```bash
grep -rn "learning_rate" .
```

---

# 七、查找文件

## 1. 按文件名查找：`find`

查找 `train.py`：

```bash
find . -name "train.py"
```

查找所有 Python 文件：

```bash
find . -name "*.py"
```

查找所有日志文件：

```bash
find . -name "*.log"
```

---

## 2. 查找大文件

查找当前目录下大于 1GB 的文件：

```bash
find . -type f -size +1G
```

---

## 3. 查找并删除

删除所有 `.pyc` 文件：

```bash
find . -name "*.pyc" -delete
```

> [!warning] 删除前先确认
> 推荐先运行：
>
> ```bash
> find . -name "*.pyc"
> ```
>
> 确认没问题后，再加 `-delete`。

---

# 八、管道和重定向

## 1. 管道：`|`

管道的作用是：**把前一个命令的输出，交给后一个命令继续处理**。

例如：

```bash
ps aux | grep python
```

含义：

1. `ps aux` 列出所有进程；
2. `|` 把输出传给后面的命令；
3. `grep python` 筛选包含 `python` 的行。

> [!tip] 常见用途
> 查自己正在跑的 Python 程序：
>
> ```bash
> ps aux | grep python
> ```

---

## 2. 标准输出重定向：`>`

```bash
python train.py > train.log
```

把程序的普通输出写入 `train.log`。

> [!warning] 注意
> `>` 会覆盖原文件。

---

## 3. 追加输出：`>>`

```bash
python train.py >> train.log
```

追加到文件末尾，不覆盖原内容。

---

## 4. 错误输出也写入日志

```bash
python train.py > train.log 2>&1
```

含义：

| 部分 | 含义 |
|---|---|
| `>` | 标准输出写入文件 |
| `2>` | 错误输出 |
| `2>&1` | 把错误输出也合并到标准输出 |

也就是：普通打印和报错都会进入 `train.log`。

---

# 九、服务器跑代码必会

## 1. 前台运行

```bash
python train.py
```

缺点：如果 SSH 断开，程序可能停止。

---

## 2. 指定 GPU 运行

使用第 0 张 GPU：

```bash
CUDA_VISIBLE_DEVICES=0 python train.py
```

使用第 1 张 GPU：

```bash
CUDA_VISIBLE_DEVICES=1 python train.py
```

使用多张 GPU：

```bash
CUDA_VISIBLE_DEVICES=0,1 python train.py
```

---

## 3. 后台运行：`nohup`

```bash
nohup python train.py > train.log 2>&1 &
```

解释：

| 部分 | 含义 |
|---|---|
| `nohup` | 断开终端后程序继续运行 |
| `python train.py` | 运行训练脚本 |
| `> train.log` | 标准输出写入日志 |
| `2>&1` | 错误输出也写入日志 |
| `&` | 放到后台运行 |

运行后查看日志：

```bash
tail -f train.log
```

---

## 4. 查看 Python 进程

```bash
ps aux | grep python
```

可能看到：

```bash
yuri  12345  98.0  20.1  python train.py
```

其中 `12345` 是进程 ID，也就是 PID。

---

## 5. 杀掉训练进程

正常结束：

```bash
kill 12345
```

强制结束：

```bash
kill -9 12345
```

> [!warning] 建议
> 先用普通 `kill`。  
> 程序卡死、普通 kill 没反应时，再用 `kill -9`。

---

## 6. 查看 GPU

```bash
nvidia-smi
```

实时刷新：

```bash
watch -n 1 nvidia-smi
```

退出：

```bash
Ctrl + C
```

重点看：

| 信息 | 含义 |
|---|---|
| GPU Memory | 显存占用 |
| GPU-Util | GPU 利用率 |
| Processes | 哪些进程在占 GPU |
| PID | 进程 ID |

杀掉占 GPU 的进程：

```bash
kill -9 PID
```

---

# 十、tmux 终端复用

> [!summary] tmux 是什么
> `tmux` 可以创建一个“不会因为 SSH 断开而消失的终端”。  
> 对于服务器训练模型，非常好用。

---

## 1. 新建 tmux 会话

```bash
tmux new -s train
```

创建一个名为 `train` 的会话。

然后可以在里面运行：

```bash
python train.py
```

或者：

```bash
CUDA_VISIBLE_DEVICES=0 python train.py
```

---

## 2. 暂时退出 tmux，但不停止程序

按：

```text
Ctrl + B
```

松开后，再按：

```text
D
```

这叫 detach。

程序仍然在 tmux 里继续运行。

---

## 3. 重新进入 tmux

```bash
tmux attach -t train
```

简写：

```bash
tmux a -t train
```

---

## 4. 查看所有 tmux 会话

```bash
tmux ls
```

---

## 5. 关闭 tmux 会话

在 tmux 里面输入：

```bash
exit
```

或者在外面杀掉会话：

```bash
tmux kill-session -t train
```

---

## 6. 推荐训练流程

```bash
ssh user@server_ip
cd your_project
tmux new -s exp1
CUDA_VISIBLE_DEVICES=0 python train.py
```

退出 tmux：

```text
Ctrl + B，然后按 D
```

重新进入：

```bash
tmux a -t exp1
```

---

# 十一、查看系统资源

## 1. 查看磁盘空间：`df`

```bash
df -h
```

重点看：

| 字段 | 含义 |
|---|---|
| `Size` | 总大小 |
| `Used` | 已使用 |
| `Avail` | 剩余 |
| `Use%` | 使用百分比 |

---

## 2. 查看文件夹大小：`du`

查看某个文件夹大小：

```bash
du -sh data
```

查看当前目录下每个文件夹大小：

```bash
du -h --max-depth=1
```

> [!tip] 磁盘满了怎么办
> 先用：
>
> ```bash
> df -h
> ```
>
> 看哪个盘满了。  
> 再用：
>
> ```bash
> du -h --max-depth=1
> ```
>
> 找哪个目录占空间最大。

---

## 3. 查看内存：`free`

```bash
free -h
```

---

## 4. 查看 CPU/内存进程：`top`

```bash
top
```

退出：

```text
q
```

如果服务器安装了 `htop`：

```bash
htop
```

---

# 十二、压缩和解压

## 1. 解压 `.tar.gz`

```bash
tar -xzvf data.tar.gz
```

参数含义：

| 参数 | 含义 |
|---|---|
| `x` | extract，解压 |
| `z` | gzip 格式 |
| `v` | 显示过程 |
| `f` | 指定文件 |

---

## 2. 打包成 `.tar.gz`

```bash
tar -czvf project.tar.gz project/
```

---

## 3. 解压 `.zip`

```bash
unzip data.zip
```

解压到指定目录：

```bash
unzip data.zip -d data/
```

---

## 4. 压缩成 `.zip`

```bash
zip -r project.zip project/
```

---

# 十三、远程登录和传文件

## 1. 登录服务器：`ssh`

```bash
ssh username@server_ip
```

例如：

```bash
ssh yuri@192.168.1.100
```

指定端口：

```bash
ssh -p 2222 yuri@192.168.1.100
```

---

## 2. 本地传到服务器：`scp`

```bash
scp train.py yuri@server_ip:/home/yuri/project/
```

传文件夹：

```bash
scp -r project yuri@server_ip:/home/yuri/
```

---

## 3. 服务器下载到本地

在本地终端执行：

```bash
scp yuri@server_ip:/home/yuri/project/train.log .
```

最后的 `.` 表示下载到当前本地目录。

下载整个文件夹：

```bash
scp -r yuri@server_ip:/home/yuri/project/logs .
```

---

## 4. 更推荐同步大文件夹：`rsync`

上传：

```bash
rsync -av project/ yuri@server_ip:/home/yuri/project/
```

下载：

```bash
rsync -av yuri@server_ip:/home/yuri/project/logs/ ./logs/
```

> [!tip] rsync 的优势
> 再次同步时，只传变化的部分。  
> 比 `scp` 更适合大项目、大数据文件夹。

---

# 十四、权限管理

## 1. 查看权限

```bash
ls -l
```

可能看到：

```bash
-rw-r--r-- 1 yuri yuri 1024 train.py
-rwxr-xr-x 1 yuri yuri 2048 run.sh
```

权限字母：

| 字母 | 含义 |
|---|---|
| `r` | read，可读 |
| `w` | write，可写 |
| `x` | execute，可执行 |

---

## 2. 给脚本执行权限

```bash
chmod +x run.sh
```

运行脚本：

```bash
./run.sh
```

---

## 3. 修改所有者：`chown`

```bash
sudo chown -R yuri:yuri project/
```

> [!note] 注意
> `chown` 通常需要管理员权限。  
> 普通服务器账号不一定能用。

---

# 十五、环境变量

## 1. 临时指定 GPU

```bash
CUDA_VISIBLE_DEVICES=0 python train.py
```

只对当前这一条命令有效。

---

## 2. 用 `export` 设置环境变量

```bash
export CUDA_VISIBLE_DEVICES=0
python train.py
```

当前终端会话里后续命令都会默认使用 GPU 0。

查看：

```bash
echo $CUDA_VISIBLE_DEVICES
```

取消：

```bash
unset CUDA_VISIBLE_DEVICES
```

---

# 十六、Python 项目常用命令

## 1. 查看 Python 路径和版本

```bash
which python
```

```bash
python --version
```

或者：

```bash
python -V
```

---

## 2. pip 常用命令

查看 pip 路径：

```bash
which pip
```

查看已安装包：

```bash
pip list
```

安装包：

```bash
pip install numpy
```

根据 `requirements.txt` 安装：

```bash
pip install -r requirements.txt
```

---

## 3. Conda 常用命令

查看环境：

```bash
conda env list
```

创建环境：

```bash
conda create -n myenv python=3.10
```

激活环境：

```bash
conda activate myenv
```

退出环境：

```bash
conda deactivate
```

删除环境：

```bash
conda remove -n myenv --all
```

---

## 4. uv 常用命令

创建虚拟环境：

```bash
uv venv
```

激活：

```bash
source .venv/bin/activate
```

安装依赖：

```bash
uv pip install -r requirements.txt
```

运行：

```bash
uv run python train.py
```

---

# 十七、Git 常用命令

## 1. 克隆项目

```bash
git clone https://github.com/xxx/xxx.git
```

进入项目：

```bash
cd xxx
```

---

## 2. 查看状态

```bash
git status
```

---

## 3. 拉取最新代码

```bash
git pull
```

---

## 4. 查看当前分支

```bash
git branch
```

---

## 5. 切换分支

```bash
git checkout branch_name
```

或者新版：

```bash
git switch branch_name
```

---

## 6. 保存修改

```bash
git add .
git commit -m "update training script"
git push
```

> [!tip] 刚开始够用的 Git 命令
> 在服务器上主要先掌握：
>
> ```bash
> git clone
> git pull
> git status
> ```

---

# 十八、编辑文件

## 1. nano：新手友好

```bash
nano train.py
```

常用操作：

| 操作 | 按键 |
|---|---|
| 保存 | `Ctrl + O` |
| 确认保存 | `Enter` |
| 退出 | `Ctrl + X` |
| 搜索 | `Ctrl + W` |

---

## 2. vim：更强，但学习成本高

```bash
vim train.py
```

常用操作：

| 操作 | 按键 |
|---|---|
| 进入编辑模式 | `i` |
| 退出编辑模式 | `Esc` |
| 保存退出 | `:wq` |
| 不保存退出 | `:q!` |
| 保存 | `:w` |

> [!note] 建议
> 刚开始不用强迫自己精通 vim。  
> 会打开、编辑、保存、退出就够了。

---

# 十九、命令历史和自动补全

## 1. 上下方向键

- `↑`：上一条命令
- `↓`：下一条命令

---

## 2. 查看历史命令

```bash
history
```

重新执行第 100 条命令：

```bash
!100
```

---

## 3. 搜索历史命令

按：

```text
Ctrl + R
```

然后输入关键词，例如：

```text
train
```

可以搜索历史命令。

---

## 4. Tab 自动补全

输入文件名前几个字母，然后按：

```text
Tab
```

例如：

```bash
python tra
```

如果当前目录下有 `train_transformer.py`，按 Tab 后可能补全成：

```bash
python train_transformer.py
```

> [!tip] 最重要的效率习惯
> 多用 `Tab` 自动补全，可以减少打错路径和文件名的概率。

---

# 二十、服务器训练代码完整流程

假设你拿到一台服务器，要跑一个深度学习项目。

## Step 1：登录服务器

```bash
ssh yuri@server_ip
```

---

## Step 2：进入工作目录

```bash
cd ~
mkdir -p projects
cd projects
```

---

## Step 3：下载代码

```bash
git clone https://github.com/xxx/project.git
cd project
```

---

## Step 4：创建环境

### Conda 方式

```bash
conda create -n exp python=3.10
conda activate exp
pip install -r requirements.txt
```

### uv 方式

```bash
uv venv
source .venv/bin/activate
uv pip install -r requirements.txt
```

---

## Step 5：检查 GPU

```bash
nvidia-smi
```

---

## Step 6：新建 tmux 会话

```bash
tmux new -s exp1
```

---

## Step 7：运行训练

前台运行：

```bash
CUDA_VISIBLE_DEVICES=0 python train.py
```

写入日志：

```bash
CUDA_VISIBLE_DEVICES=0 python train.py > train.log 2>&1
```

---

## Step 8：退出 tmux，但保持训练

```text
Ctrl + B，然后按 D
```

---

## Step 9：重新查看训练

```bash
tmux a -t exp1
```

或者查看日志：

```bash
tail -f train.log
```

---

## Step 10：查看进程

```bash
ps aux | grep python
```

或者：

```bash
nvidia-smi
```

---

# 二十一、我的常用命令清单

## 基础目录和文件

```bash
pwd
ls -lha
cd
mkdir -p
cp
mv
rm
```

## 查看和搜索

```bash
cat
less
head
tail -f
grep -rn
find
```

## 服务器资源

```bash
df -h
du -sh
du -h --max-depth=1
free -h
top
htop
nvidia-smi
watch -n 1 nvidia-smi
```

## 进程管理

```bash
ps aux | grep python
kill PID
kill -9 PID
```

## 训练运行

```bash
CUDA_VISIBLE_DEVICES=0 python train.py
nohup python train.py > train.log 2>&1 &
tmux new -s exp1
tmux a -t exp1
tmux ls
```

## 远程和传输

```bash
ssh user@server_ip
scp file user@server_ip:/path
scp -r folder user@server_ip:/path
rsync -av local/ user@server_ip:/remote/
```

## Python 环境

```bash
which python
python --version
pip list
pip install -r requirements.txt
conda env list
conda activate myenv
uv venv
uv run python train.py
```

---

# 二十二、常见危险命令提醒

> [!danger] 不要随便运行
> 下面这些命令非常危险，除非你完全确定目标是什么。

```bash
rm -rf /
```

删除根目录，极其危险。

```bash
rm -rf *
```

删除当前目录下所有东西。

```bash
rm -rf ./*
```

删除当前目录下所有普通文件和文件夹。

```bash
kill -9 PID
```

强制杀进程。程序可能来不及保存中间结果。

```bash
chmod -R 777 .
```

把当前目录下所有文件权限改得过于开放，不推荐乱用。

---

# 附录 A：最实用服务器跑代码模板

```bash
# 1. 登录服务器
ssh username@server_ip

# 2. 进入项目
cd ~/projects/my_project

# 3. 激活环境
conda activate myenv

# 4. 查看 GPU
nvidia-smi

# 5. 创建 tmux
tmux new -s exp1

# 6. 跑训练
CUDA_VISIBLE_DEVICES=0 python train.py > train.log 2>&1

# 7. 退出 tmux，不停止训练
# 按 Ctrl + B，然后按 D

# 8. 重新进入 tmux
tmux a -t exp1

# 9. 看日志
tail -f train.log

# 10. 查 Python 进程
ps aux | grep python

# 11. 杀掉进程
kill PID
```

---

# 附录 B：学习优先级

## 第一优先级：必须熟

- `pwd`
- `ls -lha`
- `cd`
- `mkdir -p`
- `cp`
- `mv`
- `rm`
- `cat`
- `less`
- `tail -f`
- `grep -rn`
- `find`

## 第二优先级：服务器跑代码

- `ssh`
- `scp`
- `rsync`
- `tmux`
- `nohup`
- `ps aux | grep python`
- `kill`
- `nvidia-smi`
- `watch -n 1 nvidia-smi`

## 第三优先级：环境和项目

- `conda activate`
- `pip install -r requirements.txt`
- `uv venv`
- `uv run`
- `git clone`
- `git pull`
- `git status`

---

# 附录 C：以后可以拆成多篇笔记

如果后面想让 Obsidian 更模块化，可以拆成：

- [[Linux 命令行常用速查]]
- [[服务器跑代码流程]]
- [[tmux 使用笔记]]
- [[nvidia-smi 和进程管理]]
- [[Linux 文件和目录操作]]
- [[SSH SCP Rsync 远程传输]]
- [[Python 环境管理 Conda uv pip]]
- [[Git 基础命令]]

当前这篇可以作为总入口。
