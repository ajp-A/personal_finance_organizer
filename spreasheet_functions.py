import pandas as pd
import requests


def find_file_map():
    df = pd.read_csv()
    col1 = df["col1"]
    col2 = df["col2"]
    empty_rng = df["col3"]
    for i in col1:
        for j in empty_rng:
            if i == "":
                j = "empty"


            