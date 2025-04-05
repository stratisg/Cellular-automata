"""
Helper functions.
"""
import numpy as np


def flatten_list(list_original):
    """
    Shape an inhomogeneous list to one with shape (samples, dimensions).

    :param list_original list: Original list.
    :return list_flat list: Flatten list.
    """
    list_flat = []
    for list_item in list_original:
        for item in list_item:
            list_flat.append(item)

    return list_flat


def convert_representation(init_rep, n_exponent, base=2):
    """
    Convert a decimal number to its binary representation.

    :param int init_rep: Decimal representation.
    :param int n_exponent: Length of final representation.
    :param int base: Base of representation. 

    :returns str binary_rep: Binary representation.
    """
    if not n_exponent:
        n_exponent = int(np.log(init_rep) / np.log(base)) + 1
    binary_rep = np.zeros(n_exponent, dtype=int)
    for exponent in range(n_exponent - 1, -1, -1):
        val_ = base ** exponent
        binary_rep[n_exponent - 1 - exponent] = init_rep // val_
        init_rep %= val_

    return binary_rep


def convert_to_decimal(values_str, n_states):
    """
    Convert the number into its decimal representation.

    :param list values_str: List with values.
    :param int n_states: Number of possible states.
    :returns decimal_rep: Decimal representation.
    """
    # TODO: Raise an error when the number of states and the values in
    # the string are not compatible.
    decimal_rep = 0
    string_length= len(values_str) - 1
    for exponent in range(string_length, -1, -1):
        value = values_str[string_length - exponent]
        decimal_rep +=  n_states ** exponent * value 

    return decimal_rep

