# -*- coding: utf-8 -*-
"""Untitled27.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1GntmqPzb5cI2copNx3WCyJj5dEb5i2k7
"""

import pandas as pd

df = pd.read_csv('covid.csv')

filtr=df[df["Country"] == "Afghanistan"]
print(filtr)

filtr=df[df["Country"] == "Albania"]
print(filtr)