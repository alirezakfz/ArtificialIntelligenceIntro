# -*- coding: utf-8 -*-
"""
Created on Thu Aug 13 22:02:20 2020

@author: Admin
"""

import minimax_helpers_ver03

def terminal_test(gameState):
    """ Return True if the game is over for the active player
    and False otherwise.
    """
    # TODO: finish this function!
    return not bool(gameState.get_legal_moves())
    pass


def min_value(gameState):
    """ Return the value for a win (+1) if the game is over,
    otherwise return the minimum value over all legal child
    nodes.
    """
    # TODO: finish this function!
    if terminal_test(gameState):
        return 1
    value=float("inf")
    
    for move in gameState.get_legal_moves():
        value=min(value,max_value(gameState.forecast_move(move)))
    return value
    pass


def max_value(gameState):
    """ Return the value for a loss (-1) if the game is over,
    otherwise return the maximum value over all legal child
    nodes.
    """
    # TODO: finish this function!
    if terminal_test(gameState):
        return -1
    
    value=float("-inf")
    
    for move in gameState.get_legal_moves():
        value=max(value,min_value(gameState.forecast_move(move)))
    return value
    pass