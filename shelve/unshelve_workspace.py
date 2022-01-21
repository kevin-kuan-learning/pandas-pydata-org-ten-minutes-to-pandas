import shelve
import pandas as pd
import numpy as np

# Please execute in workspace

with shelve.open("shelve\\current_python_workspace.out") as shelve:
    for key in shelve:
        globals()[key] = shelve[key]