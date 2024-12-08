import numpy as np
import numpy.random as rnd
from visualization import PlotTool
from cellular_automaton import get_rule, Automaton


# Define the system's  geometry.
# Number of sites.
N_SITES = 200
# Initial condition. We provide the indices of the sites with value 1.
INITIAL_COND = [100]
# Nearest neighbors used to update current site.
NEIGH = 1
digits = 2**(2 * NEIGH + 1) - 1
T_MAX = 400
RULE_NUM = 110
l_rule = get_rule(RULE_NUM, digits)
rule_args = {"l_rule": l_rule, "digits": digits, "neigh": NEIGH}
XLABEL = "Position"
YLABEL = "Time"
DPI = 600
PICS_DIR = "../pics"
PLOT_TYPE = "image"
LABEL = None
FIGNAME = __file__.split("/")[-1].split(".py")[0]
l_times = np.arange(T_MAX)
automaton = Automaton(NEIGH, rule_args, N_SITES)
automaton.initialize(INITIAL_COND)
data = np.zeros((T_MAX, N_SITES))
data[0] = automaton.lattice.copy()
plot_evolution = PlotTool(XLABEL, YLABEL, PICS_DIR, DPI)
l_time_transition = np.arange(T_MAX // 10, T_MAX, T_MAX // 10)
RNG_SEED = 1960
rng = rnd.default_rng(RNG_SEED)
flip_digits = rng.choice(digits + 1, size=len(l_time_transition))
i_transition = 0
print(f"Initial rule {rule_args['l_rule']}")
for time_ in l_times[1:]:
    # Flip one digit from the l_rule binary string to simulate the
    # evolution of a rule.
    if time_ in l_time_transition:
        flip_ = flip_digits[i_transition]
        rule_args["l_rule"][flip_] = (l_rule[flip_] + 1) % 2
        print(f"New rule {rule_args['l_rule']}")
        automaton.update_rule(rule_args)
        i_transition +=1
    automaton.update()
    data[time_] = automaton.get_configuration()
plot_evolution.plot_figure(data, PLOT_TYPE, LABEL, FIGNAME)

