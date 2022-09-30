:::{post} Aug 17, 2022
---
category: 软件工具
tags: Git, rebase
language: cn
author: 子川
exclude: true
---
在工作中，我们可能的一个习惯是将每天编写的代码进行提交，这样本地就会有多次 commit 记录，如果提交到远程主库上就会对远程主库的 commit 记录造成污染。采用 git rebase 可以合并提交记录，避免出现无用的 commit.
:::


# `git rebase` 简要使用方法介绍

## 简介

在工作中，我们可能的一个习惯是将每天编写的代码进行提交，这样本地就会有多次 commit 记录，如果提交到远程主库上就会对远程主库的 commit 记录造成污染，使用 `git rebase` 可以避免出现无用的 commit [^rebase], 更多可参考[^gitrebase]. Git Rebase 有两种使用场景：(1) 对本地分支代码多次 commit 进行合并; (2) 对本地分支代码进行变基操作，将其他分支 commit 合入到当前分支.


## 合并 commit 记录

通过如下的步骤可以简洁化我们的提交记录，

(1) 获取提交记录

如下命令, 确认需要合并最近4条记录:
```bash
git log --pretty=oneline -4
```

(2) 合并提交记录

`git rebase` 合并命令如下：
```bash
git rebase -i HEAD~2
```

:::{note}
针对上面的命令，需要合并几条数据，数字改为几即可。
:::

提交后会进入编辑模式，注意下，这里的顺序会跟 `git log` 查出来相反。

```
pick e0b28b9 test 1
pick 670239a test 2

# Rebase 4195fd7..670239a onto 4195fd7 (2 commands)
#
# Commands:
# p, pick <commit> = use commit
# r, reword <commit> = use commit, but edit the commit message
# e, edit <commit> = use commit, but stop for amending
# s, squash <commit> = use commit, but meld into previous commit
# f, fixup <commit> = like "squash", but discard this commit's log message
# x, exec <command> = run command (the rest of the line) using shell
# b, break = stop here (continue rebase later with 'git rebase --continue')
# d, drop <commit> = remove commit
# l, label <label> = label current HEAD with a name
# t, reset <label> = reset HEAD to a label
# m, merge [-C <commit> | -c <commit>] <label> [# <oneline>]
# .       create a merge commit using the original merge commit's
# .       message (or the oneline, if no original merge commit was
# .       specified). Use -c <commit> to reword the commit message.
#
# These lines can be re-ordered; they are executed from top to bottom.
#
# If you remove a line here THAT COMMIT WILL BE LOST.
#
# However, if you remove everything, the rebase will be aborted.
```


(3) 将后面两个 `pick` 改为 `s`

输入i进入编辑模式， 把除第一行的 `pick` 改为 `s`

```
pick e0b28b9 test 1
s 670239a test 2
```

按esc键退出输入模式，输入:(英文冒号)进入底线命令模式.

:::{figure} /_images/posts/2022-08-17-15-29-26.png
:::


(4) 保存退出
输入 `wq` 保存退出，会自动进入下一个 `vi` 编辑模式, 这时可以对 commit 信息进行修改，

```
# This is a combination of 2 commits.
# This is the 1st commit message:

test 1

# This is the commit message #2:

test 2

# Please enter the commit message for your changes. Lines starting
# with '#' will be ignored, and an empty message aborts the commit.
#
# Date:      Fri Sep 18 14:27:13 2020 +0800
#
# interactive rebase in progress; onto 4195fd7
# Last commands done (2 commands done):
#    pick e0b28b9 test 1
#    squash 670239a test 2
# No commands remaining.
# You are currently rebasing branch 'master' on '4195fd7'.
#
# Changes to be committed:
#       new file:   demo.txt
#

```

第四行为第一条 commit 的注释信息。第六行可以删除掉，是无用信息。第八行是第二条 commit 的注释信息，可以选择删除掉，或合并如第一条。

```
# This is a combination of 2 commits.
# This is the 1st commit message:

test 1 && test 2
```

按esc键退出输入模式，输入:(英文冒号)进入底线命令模式，输入 `wq` 退出编辑。


(5) `rebase` 完成

再次用 `git log --pretty=oneline -2` 查看得到精简后的记录。



## 分支变基

:::{figure} /_images/posts/2022-08-19-20-56-18.png
:::

基本的流程如下：
1. 先从 master 上 chckout 出一个分支；
2. master 和 feature 各自演进；
3. feature 准备合入 master。

现在就直接在 feature 上执行 rebase 操作来代替上述操作：
1. `git checkout master`
2. `git pull origin master`
3. `git checkout feature`
4. `git rebase master`


上述第4步 `rebase` 做了如下的事情：先将 master 分支的代码 checkout，存到工作目录下，然后将 feature 分支的 commit 依次合并。
如果合并的过程没问题，也就是没有冲突，那 `rebase` 到这里就算完成。

如果发生了冲突的情况，就会报错 error:Failed to merge in the changes.
自行解决冲突完毕后，使用 `git add .` 命令添加修改文件，然后使用 `git rebase –continue` 完成整个 `rebase` 过程。

如果你不想处理冲突，有两种方式恢复：
1. 使用 `git rebase –abort` 放弃此次操作，分支会回到 rebase 开始前的状态。
2. 使用 `git rebase –skip`，用 master 分支的取代当前 feature 分支。

:::{warning}
`git rebase` 会导致其他开发的 feature 分支和你的 feature 出现不一样的历史，因此在多人协同开发同个分支的情况下需要谨慎使用
:::




[^rebase]: 整洁的commit 之 git rebase 的使用, <https://codeantenna.com/a/GMKZ5jYmPZ>
[^gitrebase]: 学会git-rebase看这一篇就可以了, <https://segmentfault.com/a/1190000030688343>
