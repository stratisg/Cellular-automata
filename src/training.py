"""Training module."""
import numpy as np
import torch


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

datafile = f"{DATA_DIR}/rule_{RULE_NUM}"
data = np.load(datafile)
evolution = torch.tensor(data["evolution"])
initial_conds = data["initial_conds"]
breakpoint()
