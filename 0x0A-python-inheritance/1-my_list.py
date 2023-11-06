#!/usr/bin/python3
'''
    Class inheritance from list
'''


class MyList(list):
    '''
        print a list sorted
    '''
    def print_sorted(self):
        '''prints a list in ascending order'''
        sorted_list = sorted(self)
        print(sorted_list)
