# -*- coding: utf-8 -*-

def mol_calc(name,FW,liters,molarity):
    '''Returns the amount of chemical required to prepare a solution of desired 
    molarity'''
    grams = (FW / (1/liters)) / (1/molarity) 
    print 'To prepare', liters, 'liters of', molarity, 'M', name, ':', grams, \
    'grams required!'
    return grams

grams = mol_calc('SeO2',110.96,0.05,0.001)
