#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 20 15:57:58 2018

@author: shariram
"""

import functools
import time

PLUGINS = dict()

def timer(func):
    @functools.wraps(func)
    def wrapper_timer(*args, **kwargs):
        start_time = time.perf_counter()
        value = func(*args, **kwargs)
        end_time = time.perf_counter()
        run_time = end_time - start_time
        print (f"Finished {func.__name__!r} in {run_time:.4f} secs")
        return value
    return wrapper_timer

def debug(func):
    @functools.wraps(func)
    def wrapper_debug(*args, **kwargs):
        args_repr = [repr(a) for a in args]
        kwargs_repr = [f"{k}={v}!r" for k, v in kwargs.items()]
        signature = ", ".join(args_repr + kwargs_repr)
        print (f"Calling {func.__name__}({signature})")
        value = func(*args, **kwargs)
        print (f"{func.__name__!r} returned {value!r}")
        return value
    return wrapper_debug

def register(func):
    """Register a function as a plug-in"""
    PLUGINS[func.__name__] = func
    return func

def singleton(cls):
    """Make a class a Singleton class (only one instance)"""
    @functools.wraps(cls)
    def wrapper_singleton(*args, **kwargs):
        if not wrapper_singleton.instance:
            wrapper_singleton.instance = cls(*args, **kwargs)
        return wrapper_singleton.instance
    wrapper_singleton.instance = None
    return wrapper_singleton

