import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

import os
from pathlib import Path




folder_path ='../data/raw'
files = {}

for file in os.listdir(folder_path):
    # listdirでファイル名を取得し、フォルダのパスと結合することで、完全なファイルパスを作成
    if os.path.isfile(os.path.join(folder_path,file)):
        f = file.split('.')[0]
        files[f] = file
        print(f)


anime_df = pd.read_csv(os.path.join(folder_path,files['anime-dataset-2023']))
print(anime_df.head())
print(anime_df.info())
print(anime_df.describe())
print(anime_df.columns)


# print(df.head())
# print(df.info())
# print(df.describe())    






