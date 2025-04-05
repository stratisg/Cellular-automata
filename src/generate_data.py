"""Generate data with a cellular automaton."""
import os
import numpy as np
import numpy.random as rnd
from cellular_automaton import Automaton, get_lookup_table
from utilities import convert_representation
from visualization import PlotTool


# CONSTANTS.
DATA_DIR = "../data"
if not os.path.isdir(DATA_DIR):
    os.mkdir(DATA_DIR)
PICS_DIR = "../pics"
if not os.path.isdir(PICS_DIR):
    os.mkdir(PICS_DIR)
RULE_NUM = 110
DATA_DIR = f"{DATA_DIR}/rule_{RULE_NUM}"
if not os.path.isdir(DATA_DIR):
    os.mkdir(DATA_DIR)
PICS_DIR = f"{PICS_DIR}/rule_{RULE_NUM}"
if not os.path.isdir(PICS_DIR):
    os.mkdir(PICS_DIR)
DPI = 600
PLOT_TYPE = "image"
PLOT_TOGGLE = False
STRING_LENGTH = 100
N_STATES = 2
GEOMETRY = np.arange(STRING_LENGTH)
RADIUS = 1
SEED_INIT_COND = 1960
MAX_INIT_COND = int(5e4)
N_INIT_COND = int(1e1)
N_TIME = int(5e2)
CELL_SIZE = 3
XLABEL, YLABEL = "Location", "Time"

plot_tool = PlotTool(XLABEL, YLABEL, PICS_DIR, DPI)
update_rule = convert_representation(RULE_NUM, N_STATES ** CELL_SIZE, N_STATES)
rng = rnd.default_rng(SEED_INIT_COND)
l_initial_cond = rng.choice(MAX_INIT_COND, size=N_INIT_COND, replace=False)
evolution = []
for i_cond, init_cond in enumerate(l_initial_cond):
    print(f"Iteration {i_cond:03d}")
    automaton = Automaton(update_rule, GEOMETRY, RADIUS, N_STATES)
    # Convert init_cond from decimal to binary.
    binary_init_cond = convert_representation(init_cond, STRING_LENGTH)
    # List with indices where the lattice is equal to one.
    l_init_cond = np.where(binary_init_cond == 1)
    automaton.initialize(l_init_cond)
    data = automaton.evolve(N_TIME)
    if PLOT_TOGGLE:
        figname = f"initial_cond_{i_cond:03}"
        plot_tool.plot_figure(data, PLOT_TYPE, label=None, figname=figname)
    evolution.append(data)
evolution = np.array(evolution)
datafile = f"{DATA_DIR}/rule_{RULE_NUM}"
np.savez(datafile, evolution=evolution, initial_conds=l_initial_cond)

