"""
Test module cellular_automaton.
"""
import numpy as np
from cellular_automaton import Automaton
from cellular_automaton import get_lookup_table


test_success = 0
test_fail = 0

# Test look-up table function.
rule_num = 110
string_length = 3
n_states = 2
lookup_table = get_lookup_table(rule_num, string_length, n_states)
print("Look-up table")
print(lookup_table)

# Use the indices of the lattice sites as the geometry.
GEOMETRY = np.array([[x0, x1]
                    for x0 in np.arange(5) for x1 in np.arange(5)])
RADIUS = 1
automaton = Automaton(lookup_table, GEOMETRY, RADIUS)
automaton.visualize_lattice()
print("Neighbors to each lattice site.")
print(automaton.neighbors)
# Use the geometry info.
# GEOMETRY = (((1, 0), (0, 1)), (5, 5))
# RADIUS = 1
# automaton = Automaton(lookup_table, GEOMETRY, RADIUS)
# automaton.visualize_lattice()
print(f"Succesful tests: {test_success}")
print(f"Failed tests: {test_fail}")
print(39 * "=")
