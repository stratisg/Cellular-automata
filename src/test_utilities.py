"""
Test module for functions in utilities script.
"""
from utilities import flatten_list
from utilities import convert_to_decimal


test_success = 0
test_fail = 0

# Test flattening a list.
test_list = [[], [1], [1, 2], [1, 2, 3]]
flatten_list = flatten_list(test_list)
print("Original list")
print(test_list)
print("Flatten list")
print(flatten_list)
print(39 * "=")
if flatten_list == [1, 1, 2, 1, 2, 3]:
    print("Success flattening list!")
    test_success += 1
else:
    print("Failure flattening list!")
    test_fail += 1

# Test coverting a n-ary string to decimal representation.
values_str = [1, 0, 0]
n_states = 2
decimal_rep = convert_to_decimal(values_str, n_states)
print(39 * "=")
if decimal_rep == 4:
    print("Success converting binary string!")
    test_success += 1
else:
    print("Failure converting binary string!")
    test_fail += 1
values_str = [1, 0, 1]
n_states = 3
decimal_rep = convert_to_decimal(values_str, n_states)
print(39 * "=")
if decimal_rep == 10:
    print("Success converting 3-ary string!")
    test_success += 1
else:
    print("Failure converting 3-ary string!")
    test_fail += 1

print(f"Succesful tests: {test_success}")
print(f"Failed tests: {test_fail}")
print(39 * "=")
