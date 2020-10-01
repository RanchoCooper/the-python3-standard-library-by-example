#!/usr/bin/env python
# encoding: utf-8
import subprocess


if __name__ == '__main__':
    completed = subprocess.run(
        ['ls', '-1'],
        stdout=subprocess.PIPE,
    )
    print('return code:', completed.returncode)
    print('have {} bytes in stdout:\n{}'.format(len(completed.stdout), completed.stdout.decode('utf-8')))
