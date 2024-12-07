import numpy as np
from visualization import PlotTool


# Define the system's  geometry.
# Number of sites.
SZ = 1000
# Initial condition. We provide the indices of the sites with value 1.
IC = (50)
# Nearest neighbors used to update current site.
NEIGH = 1
T_MAX = 2000
RULE = 110
XLABEL = "Time"
YLABEL = "Position"
DPI = 600
PICS_DIR = "../pics"
PLOT_TYPE = "image"
LABEL = None
FIGNAME = "cellular_automato_1d"
lattice = np.cwarange(SZ)
lattice
l_sample = np.arange(T_MAX + 1)
y = x
data = [x]
plot_evolution = PlotTool(XLABEL, YLABEL, PICS_DIR, DPI)
for sample in l_sample[1:]:
    y = [cell_rule(rule, NEIGH, x, i, SZ) for i in range(SZ)]
    x = y
    data.append(y)
data = np.transpose(np.array(data))
plot_evolution.plot_figure(data, PLOT_TYPE, LABEL, FIGNAME)

