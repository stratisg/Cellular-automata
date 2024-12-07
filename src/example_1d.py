import numpy as np
from visualization import PlotTool
from cellular_automaton import get_rule, cell_rule


# Define the system's  geometry.
# Number of sites.
N_SITES = 100
# Initial condition. We provide the indices of the sites with value 1.
IC = [50]
# Nearest neighbors used to update current site.
NEIGH = 1
digits = 2**(2 * NEIGH + 1) - 1
T_MAX = 500
RULE_NUM = 110
rule = get_rule(RULE_NUM, digits)
XLABEL = "Time"
YLABEL = "Position"
DPI = 600
PICS_DIR = "../pics"
PLOT_TYPE = "image"
LABEL = None
FIGNAME = "cellular_automato_1d"
l_times = np.arange(T_MAX)
data = np.zeros((T_MAX, N_SITES))
# Fill with ones at the locations indicated by the array IC.
for i_occupied in IC:
    data[0, i_occupied] = 1 
plot_evolution = PlotTool(XLABEL, YLABEL, PICS_DIR, DPI)
for time_ in l_times[1:]:
    for i_site in range(N_SITES):
        neighbor_vals = np.array([data[time_ - 1, (i_site + k) % N_SITES]
                                  for k in range(-NEIGH, NEIGH + 1)])
        data[time_, i_site] = cell_rule(neighbor_vals, rule, digits, NEIGH)
data = np.transpose(np.array(data))
plot_evolution.plot_figure(data, PLOT_TYPE, LABEL, FIGNAME)

