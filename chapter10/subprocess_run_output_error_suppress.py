#!/usr/bin/env python
# encoding: utf-8
import subprocess

if __name__ == '__main__':
    try:
        # 使用DEVNULL抑制输出
        completed = subprocess.run(
            'echo to stdout; echo to stderr 1>&2',
            shell=True,
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL,
        )
    except subprocess.CalledProcessError as err:
        print('ERROR:', err)
    else:
        print('return code:', completed.returncode)
        print('stdout is {!r}'.format(completed.stdout))
        print('stderr is {!r}'.format(completed.stderr))

