
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import os
from pathlib import Path
import json
from pyspark.sql import SparkSession


def main():
    print("do data cleaning")

    with open('../../config/usrconfig.json', 'r') as f:
        usrconfg = json.load(f)
        # ファイルパスの設定
        load_file_path = '../'+usrconfg['final-animedataset']['load_file_path']
        # df = pd.read_csv(load_file_path)
        
        # del df

        spark = SparkSession.builder.appName('Anime data Analysis').getOrCreate()
        # encoding = cp932を追加
        df = spark.read.format("csv").option("ingerSchema","True").option("header","True").option("sep",",").load(load_file_path)
        print(df.show())

    print("done data cleaning")


if __name__ == "__main__":
    main()



