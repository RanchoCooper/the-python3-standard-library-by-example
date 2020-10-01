#!/usr/bin/env python
# encoding: utf-8
import subprocess


if __name__ == '__main__':
    completed = subprocess.run(['ls', '-1'])
    print('return code:', completed.returncode)
