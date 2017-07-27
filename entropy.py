#!/usr/bin/env python3

from math import log

def entropy(data):
    if isinstance(data, str):
        data = data.encode()
    if not isinstance(data, bytes):
        raise Exception('entropy: entropy: error: data needs to be either a str or a bytes.')
    ret = 0.0
    length = len(data)
    byteCount = [0] * (1 << 8)
    for byte in data:
        byteCount[byte] += 1
    for count in byteCount:
        if count > 0:
            p = count / length
            ret -= p * log(p, 256)
    return ret

def test():
    while True:
        data = input('Input a string to calculate its entropy: ')
        if len(data) > 0:
            print(entropy(data))
        else:
            break

if __name__ == '__main__':
    test()
