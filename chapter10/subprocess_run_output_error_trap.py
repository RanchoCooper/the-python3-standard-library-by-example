#!/usr/bin/env python
# encoding: utf-8
import subprocess

if __name__ == '__main__':
    try:
        completed = subprocess.run(
            'echo to stdout; echo to stderr 1>&2; exit 1',
            shell=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
        )
    except subprocess.CalledProcessError as err:
        print('ERROR:', err)
    else:
        print('return code:', completed.returncode)
        print('have {} bytes in stdout: {!r}'.format(len(completed.stdout), completed.stdout.decode('utf-8')))
        print('have {} bytes in stderr: {!r}'.format(len(completed.stderr), completed.stderr.decode('utf-8')))
