import numpy as np
import matplotlib.pyplot as plt
from utilities import convert_to_decimal, flatten_list


class Automaton:
    """The cellular automaton class."""
    def __init__(self, update_rule, geometry, radius, n_states):
        # TODO: Avoid magic numbers.
        # TODO: Allow for generalization to multi-state.
        self.n_states = n_states
        self.update_rule = update_rule
        self.geometry = geometry
        self.lattice = self._create_lattice(geometry)
        self.radius = radius
        self.neighbors = self._find_neighbors()

    def _create_lattice(self, geometry):
        """
        Create the lattice  based on the given geometry.

        The geometry can be a list with the indices of each lattice
        site or a list with two tuples. The first tuple contain the
        lattice vectors. The second tuple contains the lattice's bounds.
        These tuples will be used to construct the lattice.

        :param: geometry list: Information about the lattice.
        :return: array lattic: Lattice.
        """
        if len(geometry) > 2:
            lattice = np.zeros_like(geometry)
            if len(geometry.shape) > 1:
                lattice_dim = geometry.shape[1]
            else:
                lattice_dim = 1
        else:
            # TODO: Under construction.
            lattice_vectors = geometry[0]
            lattice_bounds = geometry[1]
            # print(f"Lattice bounds {lattice_bounds}")
            lattice_dim = len(geometry[1])

            # Initial lattice site from which we will construct the rest.
            lattice = [[np.zeros(lattice_dim)]]
            # print("Lattice")
            # print(lattice)
            # Take the lattice sites generated last and create new sites.
            lattice_new = []
            for vector in lattice_vectors:
                site_new += vector
                # Variable that indicates if site is within lattice
                # bounds.
                bound_toggle = True
                # Check if the new site is within the lattice
                # bounds.
                for i_site, site_component in enumerate(site_new):
                    if site_component > lattice_bounds[i_site]:
                        bound_toggle = False
                if bound_toggle:
                    lattice_new.append(site_new)
            if len(lattice_new):
                lattice.append(lattice_new)
            # print(39 * "+")
            lattice = flatten_list(lattice)
        # print(79 * "=")
        # print("Lattice")
        # print(lattice)
        # print(79 * "=")
        
        return lattice

    def initialize(self, initial_cond):
        """
        Initialize the lattice.

        :param str initial_cond: Initial condition.
        """ 
        self.lattice[initial_cond] = 1

    def evolve(self, n_time):
        """
        Evolve the lattice over a period of time.

        :param: int n_time: Number of time steps.
        """
        evolution = [self.get_configuration()]
        for i_time in range(1, n_time):
            self.update()
            evolution.append(self.get_configuration())

        return evolution

    # TODO: Verify that this function actually works correctly.
    def update(self):
        """
        Update lattice configuration given the rule and current configuration.
        """
        past_config = self.get_configuration()
        for i_site, site_ in enumerate(past_config):
            cell_indices = self.neighbors[i_site]
            cell = past_config[cell_indices]
            neighbor_vals = np.array([
                past_config[(i_site + k) % len(self.lattice)]
                for k in range(-self.radius, self.radius + 1)]
            )
            # TODO: Turn this to a function.
            decimal_rep = convert_to_decimal(neighbor_vals,
                                             n_states=self.n_states)
            rule_ind = len(self.update_rule)- 1 - decimal_rep
            update_ = self.update_rule[rule_ind]
            self.lattice[i_site] = update_ 

    def _find_neighbors(self):
        """
        Find all sites within a certain radius from each lattice site.
        """
        neighbors = []
        for i_site, site in enumerate(self.lattice):
            cell = []
            for i_neighbor, neighbor in enumerate(self.lattice):
                diff = i_site - i_neighbor
                # TODO: Allow flexibility on boundary conditions.
                # Assuming periodic boundary conditions.
                # TODO: Generalize to more than one dimension.
                if diff > len(self.lattice) // 2:
                    diff -= len(self.lattice) // 2
                if np.linalg.norm(diff) <= self.radius:
                    cell.append(i_neighbor)
            neighbors.append(cell)

        return neighbors
            
    def visualize_lattice(self):
        """
        Visualize lattice.
        """
        lattice = self.get_configuration()
        if self.lattice_dim == 2:
            plt.scatter(lattice[:, 0], lattice[:, 1])
        plt.show()

    def get_configuration(self):
        """
        Get current lattice configuration.
        """
        current_config = self.lattice.copy()

        return current_config


def get_lookup_table(rule_num, cell, n_states=2):
    """
    Define update rule according to its numerical representation.
    
    Using Wolfram's numerical assignment to rules for 1D cellular
    automata that the cell's future value depends on the values of
    itself and its nearest neighbors. In the most common scenario, one
    constructs a 3-bit string that corresponds to the current value of
    the left neihbor(L), cell (C), and right neighbor (R). We denote
    this string as LCR. Each position in the 3-bit string can take
    values from the set {0, 1} thus there 2^3=8 differenr strings. Based
    on the present string, the cellular automato rule assigns
    a binary value to the cell. For every string there are two
    choices that can be assigned to the cell. This means that the
    cellular automaton rules that use finite strings and take values
    from a discrete set have a finite domain and range and can be
    descibed using a look-up table. For the LCR scenario, there are
    2^8=256 different rules. The way we construct the look-up table is
    by converting the decimal number representing the rule to its
    corresponding binary representation. Then each digit of the binary
    representation corresponds to the unique string configuration that
    its numerical representation is the digit's location. For instance,
    the rule 110 converts to the binary string 01101110. Then we derive 
    the following look-up table:
    LCR (Binary) | LCR (Decimal) -> Rule value at location LCR
    111 | 7 -> 0
    110 | 6 -> 1
    101 | 5 -> 1
    100 | 4 -> 0
    011 | 3 -> 1
    010 | 2 -> 1
    001 | 1 -> 1
    000 | 0 -> 0

    :param int rule_num: Decimal representation of the rule.
    :param int cell: Cell used to update cell's value.
    :param int n_states: The number of values the cell can take.
    :returns : look-up table
    :rtype list
    """
    # TODO: Raise an error when the number of states and the string
    # length string are not compatible.
    l_rule = np.zeros(n_states ** cell, dtype=int)
    for i_rule in range(n_states ** cell - 1, -1, -1):
        l_rule[i_rule] = rule_num // n_states ** i_rule
        rule_num %= (n_states ** i_rule)

    return l_rule

