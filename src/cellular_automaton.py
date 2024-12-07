import numpy as np


def get_rule(rule_num, digits):
    """Define update rule according to its numerical representation."""
    rule = []
    for i in range(digits, -1, -1):
        rule.append(rule_num // 2**i)
        rule_num %= (2**i)

    return rule


def cell_rule(neighbor_vals, rule, digits, neigh):
    """
    The cellular automato governing rule.
    """
    # Convert the binary string of the neighbring data into a decimal
    # number. This decimal number corresponds to index of the binary
    # representation of the rule.
    exp = np.array([2**i for i in range(2 * neigh, -1, -1)])
    ind = int(np.sum(exp * neighbor_vals))
    a = rule[digits - ind]
    
    return a

