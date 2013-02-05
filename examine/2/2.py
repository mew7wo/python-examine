#!/usr/bin/env python
#coding:utf-8

class Singleton(object):
    ''' singleton pattern'''
    def __new__(cls, *arg, **kargs):
        instance = cls.__dict__.get('__it__')
        if instance is not None:
            return instance
        cls.__it__ = instance = object.__new__(cls)
        return instance


def main():
    a = Singleton()
    b = Singleton()

    if a == b:
        print 'ok'


if __name__ == '__main__':
    main()





