#!/usr/bin/env python
# encoding: utf-8
import subprocess

if __name__ == '__main__':
    print('popen2:')
    proc = subprocess.Popen(
        ['cat', '-'],
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE,
    )
    msg = 'through stdin to stdout'.encode('utf-8')
    stdout_value = proc.communicate(msg)[0].decode('utf-8')
    print('pass through:', repr(stdout_value))
