#!/usr/bin/python3

"""
Module docstring and general information
"""

__author__='Juan David Arias'
__copyright__='Copyright 2016, Juan David Arias'
__credits__='Some credits if necessary'
__license__='GPL'
__version__='1.0'
__maintainer__='Juan David Arias'
__email__='juasda96@gmail.com'
__status__='developer'

def hello_world():
    print('hello world')

def say_hi():
    name = input('enter your name ==> ')
    print('hi ' + name + ', I hope your feeling nice!')

        
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show_person_data(self):
        return self.name, self.age