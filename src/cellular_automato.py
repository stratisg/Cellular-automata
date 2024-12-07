import numpy as np
from visualization import PlotTool


# TODO: Change variable names to meaningful names.
def cell_rule(num, neigh, x, index, sz):
    """
    The cellular automato governing rule.
    """
    data = np.array([x[(index + k) % sz] for k in range(-neigh, neigh + 1)])
    rule = []
    digits = 2**(2 * neigh + 1) - 1
    exp = np.array([2**i for i in range(2 * neigh, -1, -1)])
    for i in range(digits, -1, -1):
        rule.append(num // 2**i)
        num = num % (2**i)
    ind = int(np.sum(exp * data))
    a = rule[digits - ind]
    
    return a

if __name__ == "__main__":
    SZ = int(1e3)
    IC = 50
    NEIGH = 1
    x = []
    for i in range(SZ - 1, -1, -1): 
        x.append(IC // 2**i)
        IC = IC % (2**i) 
    x = np.array(x)
    LATTICE = np.arange(SZ)
    T_MAX = int(2e3)
    l_moment = np.linspace(0, T_MAX, T_MAX + 1)
    y = x
    data = [x]
    num = 110
    XLABEL = "Time"
    YLABEL = "Position"
    DPI = 600
    PICS_DIR = "../pics"
    plot_evolution = PlotTool(XLABEL, YLABEL, PICS_DIR, DPI)
    for moment in l_moment[1:]:
        y = [cell_rule(num, NEIGH, x, i, SZ) for i in range(SZ)]
        x = y
        data.append(y)
    PLOT_TYPE = "image"
    LABEL = None
    FIGNAME = "cellular_automato_1d"
    data = np.transpose(np.array(data))
    plot_evolution.plot_figure(data, PLOT_TYPE, LABEL, FIGNAME)

