# -*- coding: utf-8 -*-
"""
Created on Thu Aug 13 22:00:34 2020

@author: Admin
"""

import minimax_helpers_ver03

from gamestate_ver03 import *

g = GameState()

print("Calling min_value on an empty board...")
v = minimax_helpers_ver03.min_value(g)

if v == -1:
    print("min_value() returned the expected score!")
else:
    print("Uh oh! min_value() did not return the expected score.")