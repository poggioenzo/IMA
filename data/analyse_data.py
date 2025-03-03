#! /usr/bin/env python3
# -*- coding: utf-8 -*-
from collections import defaultdict as dd
from collections import Counter
import matplotlib.pyplot as plt
import pandas as pd
import os
import json
from pprint import pprint
import time
import numpy as np
import math


by_vid = dd(lambda: dd(int))
by_usr = dd(lambda: dd(int))


for f in sorted(os.listdir("evals")):
    a = pd.read_csv("evals/" + f).values.tolist()
    for b in a:
        by_usr[b[1]][b[0]] = b[2]
        if b[3]:
            by_vid[b[1]]["funny"] += 1
        else:
            by_vid[b[1]]["notFunny"] += 1

pprint(by_vid)

funny = []
not_funny = []

for key in sorted(by_vid.keys()):
    funny.append(by_vid[key]["funny"])
    not_funny.append(by_vid[key]["notFunny"])

labels = sorted(by_vid.keys())
indexes = np.arange(len(labels))
bar_width = 0.75
plt.xticks(indexes + bar_width / 2, labels)
plt.style.use('seaborn-deep')
data = np.vstack([funny, not_funny]).T
bins = np.linspace(0, 19, 20)
plt.hist(data, bins, alpha=0.7, label=['funny', 'not_funny'])
plt.legend(loc='upper right')
# plt.show()
