#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug  7 11:53:13 2024

@author: vdotsenko
"""

import pandas as pd

csv_path = "file1.csv"
df = pd.read_csv(csv_path)
df.head()
df.iloc[0,0]
df.loc[0,"name"]

df["name"].unique()

df_xls = pd.read_excel("file1.xlsx")