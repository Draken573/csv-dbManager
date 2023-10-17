# file_utils.py

import os
import pandas as pd


class FileUtils:
    def read_csv(self, file_path):
        try:
            return pd.read_csv(file_path)
        except pd.errors.ParserError as error:
            print(f"Erro ao ler o arquivo CSV: {error}")
            return None
