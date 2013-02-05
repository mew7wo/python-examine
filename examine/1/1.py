#!/usr/bin/env python

import random

def makeData():
    #return [random.randint(1, 100) for i in range(20)]
    #return [1, 3, 5, 7, 8, 25, 4, 20]
    #return []
    #return [0, 0, 0]
    #return [-1, 1, -1]
    return [-1, 23, -1]

def getBalance(data):
    data_sum = sum(data)
    left_sum = 0
    indexs = []
    for i in range(len(data)):
        data_sum -= data[i]
        if left_sum == data_sum:
            indexs.append(i)
        left_sum += data[i]

    return indexs

def main():
    for i in range(10):
        data = makeData()
        print data
        print getBalance(data)

if __name__ == '__main__':
    main()
