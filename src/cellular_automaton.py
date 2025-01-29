import numpy as np
import matplotlib.pyplot as plt
from utilities import convert_to_decimal, flatten_list


class Automaton:
    """The cellular automaton class."""
    def __init__(self, update_rule, geometry, radius):
        self.update_rule = update_rule
        self.lattice = self.create_lattice(geometry)
        self.radius = radius
        self.find_neighbors()

    def create_lattice(self, geometry):
        """
        Create the lattice  based on the given geometry.

        The geometry can be a list with the indices of each lattice
        site or a list with two tuples that contain the lattice vectors
        and its bounds. These tuples will be used to construct the
        lattice.

        :param geometry list: Information about the lattice.
        """
        if len(geometry) > 2:
            lattice = geometry
            self.lattice_dim = lattice.shape[1]
        else:
            self.lattice_vectors = geometry[0]
            self.lattice_bounds = geometry[1]
            print(f"Lattice bounds {self.lattice_bounds}")
            self.lattice_dim = len(geometry[1])

            # Initial lattice site from which we will construct the rest.
            lattice = [[np.zeros(self.lattice_dim)]]
            print("Lattice")
            print(lattice)
            # Take the lattice sites generated last and create new sites.
            lattice_new = []
            for vector in self.lattice_vectors:
                site_new += vector
                # Variable that indicates if site is within lattice
                # bounds.
                bound_toggle = True
                # Check if the new site is within the lattice
                # bounds.
                for i_site, site_component in enumerate(site_new):
                    if site_component > self.lattice_bounds[i_site]:
                        bound_toggle = False
                if bound_toggle:
                    lattice_new.append(site_new)
            if len(lattice_new):
                lattice.append(lattice_new)
            print(39 * "+")
            lattice = flatten_list(lattice)
        print(79 * "=")
        print("Lattice")
        print(lattice)
        print(79 * "=")

        return lattice

    def visualize_lattice(self):
        """
        Visualize lattice.
        """
        lattice = self.get_configuration()
        if self.lattice_dim == 2:
            plt.scatter(lattice[:, 0], lattice[:, 1])
        plt.show()

    def initialize(self, initial_cond):
        """
        Set value to one at all the indices in the array intial_cond.
        """ 
        self.lattice[initial_cond] = 1 

    def find_neighbors(self):
        """
        Find all sites within a certain radius from each lattice site.
        """
        neighbors = [[] for _ in self.lattice]
        for i_site, site in enumerate(self.lattice):
            for i_neighbor, neighbor in enumerate(self.lattice):
                # Exclude the sites themselves.
                if i_site == i_neighbor:
                    continue
                diff = site - neighbor
                if np.linalg.norm(diff) <= self.radius:
                    neighbors[i_site].append(neighbor)

        self.neighbors = neighbors
            

    def get_configuration(self):
        """
        Get current lattice configuration.
        """
        current_config = self.lattice.copy()

        return current_config

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
            self.lattice[i_site] = self.rule_fn(
                neighbor_vals, **self._rule_args
            )


def get_lookup_table(rule_num, string_length, n_states=2):
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
    :param int string_length: String length used to update cell's value.
    :param int n_states: The number of values the cell can take.
    :returns : look-up table
    :rtype list
    """
    # TODO: Raise an error when the number of states and the string
    # length string are not compatible.
    l_rule = []
    for i in range(string_length, -1, -1):
        l_rule.append(rule_num // n_states**i)
        rule_num %= (n_states**i)

    return l_rule

