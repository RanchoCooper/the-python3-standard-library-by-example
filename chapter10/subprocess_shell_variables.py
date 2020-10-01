#!/usr/bin/env python
# encoding: utf-8
import subprocess


if __name__ == '__main__':
    # shell参数设置为true会创建中间shell进程
    completed = subprocess.run('echo $HOME', shell=True)
    print('return code:', completed.returncode)
