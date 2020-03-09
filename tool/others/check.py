import pandas as pd
import numpy as np

inp = pd.read_csv("../../dat/pof/wfpvam_foodprices.csv")


for i in range(100):
    print (inp[i])
