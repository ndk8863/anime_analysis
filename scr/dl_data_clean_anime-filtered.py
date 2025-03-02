
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import os
from pathlib import Path
from Parent_data_cleaner import Parent_data_cleaner
import json

# クラスの定義
class Data_cleaner(Parent_data_cleaner):
    # 固有のデータ加工を記載
    def clean_data(self,df):
        try:
            return df
        except Exception as e:
            print(f"データの加工に失敗しました: {e}")
            exit()


def main():
    print("do data cleaning")

    with open('../config/usrconfig.json', 'r') as f:
        usrconfg = json.load(f)
        # ファイルパスの設定
        load_file_path = usrconfg['anime-filtered']['load_file_path']
        save_file_path = usrconfg['anime-filtered']['save_file_path']

        Data_Clenaer = Data_cleaner(load_file_path)
        df = Data_Clenaer.load_data()
        df = Data_Clenaer.clean_data(df)
        Data_Clenaer .save_data(df,save_file_path)

    print("done data cleaning")


if __name__ == "__main__":
    main()



