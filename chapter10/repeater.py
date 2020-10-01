#!/usr/bin/env python
# encoding: utf-8
import sys

if __name__ == '__main__':
    sys.stderr.write('repeater.py: starting\n')
    sys.stderr.flush()

    while True:
        next_line = sys.stdin.readline()
        sys.stderr.flush()
        if not next_line:
            break
        sys.stdout.write(next_line)
        sys.stdout.flush()

    sys.stderr.write('repeater.py: exiting\n')
    sys.stderr.flush()
