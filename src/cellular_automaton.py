import numpy as np


class Automaton:
    """The cellular automaton class."""
    def __init__(self, neigh, rule_fn, rule_args, geometry):
        self.neigh = neigh
        self.digits = 2**(2 * neigh + 1) - 1
        self.rule_fn = rule_fn
        self.rule_args = rule_args
        self.geometry = geometry
        self.lattice = np.zeros(self.geometry)

    def initialize(self, initial_cond):
        """
        Set value to one at all the indices in the array intial_cond.
        """ 
        self.lattice[initial_cond] = 1 

    def get_configuration(self):
        """
        Get current lattice configuration.
        """
        self.current_config = self.lattice.copy()

        return self.current_config

    def update_rule(self, rule_fn, rule_args):
        """Update the rule governing the cellular automaton."""
        self.rule_fn = rule_fn
        self.rule_args = rule_args

    def update(self):
        """
        Update lattice configuration given the rule and current configuration.
        """
        past_config = self.get_configuration()
        for i_site in range(self.geometry):
            neighbor_vals = np.array(
             [past_config[(i_site + k) % self.geometry]
              for k in range(-self.neigh, self.neigh + 1)]
            )
            self.lattice[i_site] = self.rule_fn(neighbor_vals,
                                                **self.rule_args)


def get_rule(rule_num, digits):
    """Define update rule according to its numerical representation."""
    l_rule = []
    for i in range(digits, -1, -1):
        l_rule.append(rule_num // 2**i)
        rule_num %= (2**i)

    return l_rule


def rule_vanilla(neighbor_vals, l_rule, digits, neigh):
    """
    The cellular automato governing rule.
    """
    # Convert the binary string of the neighboring data into a decimal
    # number. This decimal number corresponds to index of the binary
    # representation of the rule.
    exp = np.array([2**i for i in range(2 * neigh, -1, -1)])
    ind = int(np.sum(exp * neighbor_vals))
    a = l_rule[digits - ind]
    
    return a

