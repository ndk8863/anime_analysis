
import pandas as pd
import numpy as np


class Parent_data_cleaner():
    def __init__(self,file_path):
        self.file_path = file_path

    def load_data(self):
        try:
            df = pd.read_csv(self.file_path,encoding='utf-8')
            print(f"データを読み込みました: {self.file_path}")
            return df
        except FileNotFoundError:
            print(f"ファイルが見つかりません: {self.file_path}")
            exit()
    def clean_data(df):
        try:
            return df
        except Exception as e:
            print(f"データの加工に失敗しました: {e}")
            exit()

    
    def save_data(self,df,save_file_path):
        try:
            df.to_csv(save_file_path,index=False,encoding='utf-8')
            print(f"データを保存しました: {save_file_path}")
        except Exception as e:
            print(f"データの保存に失敗しました: {e}")
            exit()