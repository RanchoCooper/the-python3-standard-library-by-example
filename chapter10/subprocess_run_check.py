#!/usr/bin/env python
# encoding: utf-8
import subprocess


if __name__ == '__main__':
    try:
        # check参数为true会检查退出码, 并产生CalledProcessError异常
        subprocess.run(['False'], check=True)
    except subprocess.CalledProcessError as err:
        print('ERROR:', err)

