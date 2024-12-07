import numpy as np
from visualization import PlotTool
from cellular_automaton import get_rule, rule_vanilla, Automaton


# Define the system's  geometry.
# Number of sites.
N_SITES = 500
# Initial condition. We provide the indices of the sites with value 1.
INITIAL_COND = [250]
# Nearest neighbors used to update current site.
NEIGH = 1
digits = 2**(2 * NEIGH + 1) - 1
T_MAX = 1000
RULE_NUM = 110
l_rule = get_rule(RULE_NUM, digits)
rule_fn = rule_vanilla
rule_args = {"l_rule": l_rule, "digits": digits, "neigh": NEIGH}
XLABEL = "Time"
YLABEL = "Position"
DPI = 600
PICS_DIR = "../pics"
PLOT_TYPE = "image"
LABEL = None
FIGNAME = "cellular_automaton_1d"
l_times = np.arange(T_MAX)
automaton = Automaton(NEIGH, rule_fn, rule_args, N_SITES)
automaton.initialize(INITIAL_COND)
data = np.zeros((T_MAX, N_SITES))
data[0] = automaton.lattice.copy()
plot_evolution = PlotTool(XLABEL, YLABEL, PICS_DIR, DPI)
for time_ in l_times[1:]:
    automaton.update()
    data[time_] = automaton.get_configuration()
data = np.transpose(np.array(data))
plot_evolution.plot_figure(data, PLOT_TYPE, LABEL, FIGNAME)

