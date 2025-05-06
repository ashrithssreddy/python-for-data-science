import os

os.getcwd()
import inspect
inspect.getargspec(os.getcwd) 

import pandas as pd
# inspect.getargspec(pd.read_csv)
inspect.signature(pd.read_csv)

# Del all user defined variables
for iii in dir():
    if not iii.startswith("_"):
        del globals()[iii]
    del iii






