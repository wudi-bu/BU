#!/usr/bin/env python
# AUTHOR DiWu wudi@bu.edu
import copy
import itertools
import sys
from collections import defaultdict
dict = defaultdict(lambda: defaultdict(list))


def Calculate_short(Word_Pool, Word_Count):
    b = []
    result = set()
    for x in Word_Pool:
        b.append(x)
    for subset in itertools.combinations(b, Word_Count):
        subset = ''.join(subset)
        for i in dict[Word_Count][''.join(sorted(subset.strip()))]:
            result.add(i)
    return sorted(result)


def Calculate_long(Word_Pool, Word_Count):
    result = set()
    ele = [0] * 26
    for x in Word_Pool:
        ele[ord(x)-ord('a')] += 1
    for i in dict[Word_Count].keys():
        ele1 = copy.deepcopy(ele)
        flag = True
        for n in i:
            ele1[ord(n) - ord('a')] -= 1
            if(ele1[ord(n) - ord('a')] < 0):
                flag = False
                break
        if(flag):
            for m in dict[Word_Count][i]:
                result.add(m)
    return sorted(result)


def Print_out(Input_list):
    for i in Input_list:
        print(i)
    print('.')


def main():
    for x in open(sys.argv[1], 'r').readlines():
        dict[len(x.strip())][''.join(sorted(x.strip()))].append(x.strip())
    while(True):
        key = input().split()
        if(int(key[1]) == 0):
            break
        if(int(key[1]) > 8):
            Print_out(Calculate_long(key[0], int(key[1])))
        else:
            Print_out(Calculate_short(key[0], int(key[1])))
if __name__ == "__main__":
    main()
