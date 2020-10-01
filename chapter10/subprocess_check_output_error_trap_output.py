#!/usr/bin/env python
# encoding: utf-8
import subprocess

if __name__ == '__main__':
    try:
        completed = subprocess.run(
            'echo to stdout; echo to stderr 1>&2',
            shell=True,
            check=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
        )
    except subprocess.CalledProcessError as err:
        print('ERROR:', err)
    else:
        print('have {} bytes in output: {!r}'.format(len(completed.stdout), completed.stdout .decode('utf-8')))
