
import pandas as pd
import numpy as np


class Parent_data_cleaner():
    def __init__(self,file_path):
        self.file_path = file_path

    def load_data(self,ext:str,encording:str):
        try:
            if ext == 'csv':
                df = pd.read_csv(self.file_path,encoding=encording)
                print(f"データを読み込みました: {self.file_path}")
                return df
            elif ext == 'tsv':
                df = pd.read_csv(self.file_path,encoding=encording)
                print(f"データを読み込みました: {self.file_path}")
                return df
            elif ext == 'pkl':
                df = pd.read_pickle(self.file_path,encoding=encording)
                print(f"データを読み込みました: {self.file_path}")
                return df
            elif ext == 'pkl':
                df = pd.read_csv(self.file_path,encoding=encording)
                print(f"データを読み込みました: {self.file_path}")
                return df
            # parquetも作成する
            # jsonと
            elif ext == 'json':
                return 
            elif ext == 'xlsx':
                df = pd.read_excel(self.file_path,encoding=encording)
                print(f"データを読み込みました: {self.file_path}")
                return df
            
        except FileNotFoundError:
            print(f"ファイルが見つかりません: {self.file_path},ext:{ext}")
            exit()

    def clean_data(df):
        try:
            return df
        except Exception as e:
            print(f"データの加工に失敗しました: {e}")
            exit()

    
    def save_data(self,df,save_file_path,ext:str,encording:str):
        try:
            if ext == 'csv':
                df.to_csv(save_file_path,index=False,encoding=encording)
                print(f"データを保存しました: {save_file_path}")
            elif ext == 'tsv':
                df.to_csv(save_file_path,index=False,encoding=encording)
                print(f"データを保存しました: {save_file_path}")
            elif ext == 'pkl':
                df.to_pickle(save_file_path)
                print(f"データを保存しました: {save_file_path}")
            # parquet型も作成する
            elif ext == 'json':
                df.to_json(save_file_path)
                print(f"データを保存しました: {save_file_path}")
            elif ext == 'xlsx':
                df.to_excel(save_file_path,index=False,encoding=encording)
                print(f"データを保存しました: {save_file_path}")
            
        except Exception as e:
            print(f"データの保存に失敗しました: {e}")
            exit()